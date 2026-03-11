"""Splice Site Usage & Splice Junction Analysis at each breakpoint.

Uses AlphaGenome's SPLICE_SITE_USAGE and SPLICE_JUNCTIONS output types
(not just SPLICE_SITES used previously) to predict:
1. Which splice sites are actively used at each breakpoint
2. Split-read junction counts (which exon-exon junctions are formed)
3. Whether aberrant splice products form near translocation breakpoints

Clinically relevant for neoantigen prediction — aberrant splice products
at the fusion junction could generate novel peptide sequences targetable
by the immune system.
"""

import os
import sys
sys.path = [p for p in sys.path if p not in ('', '.', os.getcwd())]

with open('/Users/lbacaj/genomics/.env') as f:
    for line in f:
        if '=' in line:
            k, v = line.strip().split('=', 1)
            os.environ[k] = v

import matplotlib
matplotlib.use('Agg')

from alphagenome.models import dna_client
from alphagenome.data import genome
from alphagenome.data import gene_annotation
from alphagenome.data import transcript as transcript_utils
from alphagenome.visualization import plot_components
import matplotlib.pyplot as plt
import numpy as np
import json
import pandas as pd

print("Connecting to AlphaGenome API...")
dna_model = dna_client.create(os.environ['ALPHA_GENOME_API_KEY'])
print("Connected.\n")

# Load GTF
print("Loading gene annotations...")
gtf = pd.read_feather(
    'https://storage.googleapis.com/alphagenome/reference/gencode/'
    'hg38/gencode.v46.annotation.gtf.gz.feather'
)
gtf_transcripts = gene_annotation.filter_protein_coding(gtf)
gtf_transcripts = gene_annotation.filter_to_mane_select_transcript(gtf_transcripts)
transcript_extractor = transcript_utils.TranscriptExtractor(gtf_transcripts)
print("Done.\n")

OUTPUT_DIR = '/Users/lbacaj/genomics/splice_junctions'
os.makedirs(OUTPUT_DIR, exist_ok=True)

targets = [
    {'name': 'ASPSCR1',     'chrom': 'chr17', 'pos': 82010811,
     'label': 'ASPSCR1 (chr17:82,010,811)', 'gene': 'ASPSCR1'},
    {'name': 'TFE3',        'chrom': 'chrX',  'pos': 49043986,
     'label': 'TFE3 (chrX:49,043,986)', 'gene': 'TFE3'},
    {'name': 'DNMT1_chr1',  'chrom': 'chr1',  'pos': 31048832,
     'label': 'DNMT1 partner (chr1:31,048,832)', 'gene': 'LAPTM5'},
    {'name': 'DNMT1_chr19', 'chrom': 'chr19', 'pos': 10160241,
     'label': 'DNMT1 primary (chr19:10,160,241)', 'gene': 'DNMT1'},
]

# Tissues for splice site usage
ontology_terms = [
    'UBERON:0002048',  # Lung
    'UBERON:0000955',  # Brain
    'UBERON:0002107',  # Liver
    'UBERON:0001157',  # Transverse colon
    'UBERON:0002106',  # Spleen
]

all_results = {}

for target in targets:
    name = target['name']
    chrom = target['chrom']
    pos = target['pos']
    label = target['label']

    print("=" * 70)
    print(f"SPLICE ANALYSIS: {label}")
    print("=" * 70)

    # Use 1MB context for full gene coverage
    interval = genome.Interval(chrom, pos, pos + 1).resize(
        dna_client.SEQUENCE_LENGTH_1MB
    )
    transcripts = transcript_extractor.extract(interval)

    target_results = {}

    # =============================================
    # 1. SPLICE_SITE_USAGE — fraction of time each
    #    splice site is used
    # =============================================
    print(f"\n  1. SPLICE_SITE_USAGE predictions...")

    try:
        output = dna_model.predict_interval(
            interval=interval,
            requested_outputs=[dna_client.OutputType.SPLICE_SITE_USAGE],
            ontology_terms=ontology_terms,
        )

        ssu = output.splice_site_usage
        vals = ssu.values
        meta = ssu.metadata

        print(f"     Shape: {vals.shape}")
        print(f"     Tracks: {len(meta)}")
        for _, row in meta.iterrows():
            print(f"       {row.get('name', '')} | "
                  f"{row.get('biosample_name', '')} | "
                  f"strand={row.get('strand', '.')}")

        # Analyze splice site usage near breakpoint
        center = vals.shape[0] // 2
        windows = [1000, 5000, 25000]  # 1kb, 5kb, 25kb

        for w in windows:
            w_slice = slice(center - w, center + w)
            w_vals = vals[w_slice, :]

            print(f"\n     Within {w // 1000}kb of breakpoint:")
            for i, (_, row) in enumerate(meta.iterrows()):
                col = w_vals[:, i]
                tissue = row.get('biosample_name', row.get('name', ''))
                strand = row.get('strand', '.')

                # Find positions with high usage
                high = np.where(col > 0.1)[0]
                if len(high) > 0:
                    max_score = float(np.max(col))
                    mean_high = float(np.mean(col[high]))
                    print(f"       {tissue:30s} (strand {strand}): "
                          f"{len(high)} active sites, "
                          f"max={max_score:.4f}, mean={mean_high:.4f}")

                    # Detail the top sites
                    if w == 5000:  # Only detail for 5kb window
                        top_positions = np.argsort(col)[-5:][::-1]
                        for p in top_positions:
                            score = col[p]
                            if score > 0.05:
                                gpos = interval.start + center - w + p
                                dist = gpos - pos
                                print(f"         {chrom}:{gpos:,} "
                                      f"(bp{dist:+,}): usage={score:.4f}")

        target_results['splice_site_usage'] = {
            'shape': list(vals.shape),
            'n_tracks': len(meta),
        }

        # Generate visualization
        print(f"\n     Generating splice site usage visualization...")
        fig, axes = plt.subplots(len(meta), 1,
                                 figsize=(20, 2.5 * len(meta)),
                                 sharex=True)
        if len(meta) == 1:
            axes = [axes]

        zoom = 25000
        x = np.arange(center - zoom, center + zoom)

        for i, (_, row) in enumerate(meta.iterrows()):
            ax = axes[i]
            y = vals[center - zoom:center + zoom, i]
            ax.plot(x, y, color='darkgreen', linewidth=0.8)
            ax.fill_between(x, y, alpha=0.3, color='green')
            ax.axvline(center, color='red', linewidth=2,
                       linestyle='--', alpha=0.8)
            tissue = row.get('biosample_name', row.get('name', ''))
            strand = row.get('strand', '.')
            ax.set_ylabel(f'{tissue}\n({strand})', fontsize=9)
            ax.set_ylim(bottom=0)

        axes[0].set_title(
            f'Splice Site Usage: {label}\n'
            f'Red line = breakpoint | 50kb window',
            fontsize=13, fontweight='bold')
        axes[-1].set_xlabel('Position in interval', fontsize=11)
        plt.tight_layout()
        plt.savefig(f'{OUTPUT_DIR}/{name}_splice_usage.png',
                    dpi=150, bbox_inches='tight', facecolor='white')
        plt.close('all')
        print(f"     Saved: {OUTPUT_DIR}/{name}_splice_usage.png")

    except Exception as e:
        print(f"     ERROR: {e}")
        import traceback
        traceback.print_exc()

    # =============================================
    # 2. SPLICE_JUNCTIONS — split-read counts
    # =============================================
    print(f"\n  2. SPLICE_JUNCTIONS predictions...")

    try:
        output_sj = dna_model.predict_interval(
            interval=interval,
            requested_outputs=[dna_client.OutputType.SPLICE_JUNCTIONS],
            ontology_terms=ontology_terms,
        )

        sj = output_sj.splice_junctions
        print(f"     Type: {type(sj)}")

        # Splice junctions may return JunctionData instead of TrackData
        if hasattr(sj, 'values') and hasattr(sj, 'metadata'):
            vals_sj = sj.values
            meta_sj = sj.metadata
            print(f"     Shape: {vals_sj.shape}")
            print(f"     Tracks: {len(meta_sj)}")

            # Look for junctions near breakpoint
            if len(vals_sj.shape) == 2:
                center_sj = vals_sj.shape[0] // 2
                w = 25000
                w_vals = vals_sj[center_sj - w:center_sj + w, :]

                print(f"\n     Junction signal within 25kb of breakpoint:")
                for i, (_, row) in enumerate(meta_sj.iterrows()):
                    col = w_vals[:, i]
                    tissue = row.get('biosample_name', row.get('name', ''))
                    strand = row.get('strand', '.')
                    nonzero = np.count_nonzero(col)
                    max_val = float(np.max(col)) if nonzero > 0 else 0
                    sum_val = float(np.sum(col))
                    if nonzero > 0:
                        print(f"       {tissue:30s} (strand {strand}): "
                              f"{nonzero} junctions, "
                              f"max={max_val:.4f}, sum={sum_val:.4f}")

                target_results['splice_junctions_track'] = {
                    'shape': list(vals_sj.shape),
                    'n_tracks': len(meta_sj),
                }

                # Visualization
                n_tracks_sj = min(len(meta_sj), 10)
                fig, axes = plt.subplots(n_tracks_sj, 1,
                                         figsize=(20, 2.5 * n_tracks_sj),
                                         sharex=True)
                if n_tracks_sj == 1:
                    axes = [axes]

                for i in range(n_tracks_sj):
                    ax = axes[i]
                    y = vals_sj[center_sj - w:center_sj + w, i]
                    x = np.arange(center_sj - w, center_sj + w)
                    ax.plot(x, y, color='purple', linewidth=0.8)
                    ax.fill_between(x, y, alpha=0.3, color='purple')
                    ax.axvline(center_sj, color='red', linewidth=2,
                               linestyle='--', alpha=0.8)
                    tissue = meta_sj.iloc[i].get('biosample_name',
                             meta_sj.iloc[i].get('name', ''))
                    strand = meta_sj.iloc[i].get('strand', '.')
                    ax.set_ylabel(f'{tissue}\n({strand})', fontsize=9)

                axes[0].set_title(
                    f'Splice Junctions: {label}\n'
                    f'Red line = breakpoint | 50kb window',
                    fontsize=13, fontweight='bold')
                axes[-1].set_xlabel('Position in interval', fontsize=11)
                plt.tight_layout()
                plt.savefig(f'{OUTPUT_DIR}/{name}_splice_junctions.png',
                            dpi=150, bbox_inches='tight', facecolor='white')
                plt.close('all')
                print(f"     Saved: {OUTPUT_DIR}/{name}_splice_junctions.png")

        elif hasattr(sj, 'junctions'):
            # JunctionData format
            junctions = sj.junctions
            print(f"     Number of junctions: {len(junctions)}")

            # Find junctions near breakpoint
            near_bp = []
            for j in junctions:
                if hasattr(j, 'start') and hasattr(j, 'end'):
                    if abs(j.start - pos) < 50000 or abs(j.end - pos) < 50000:
                        near_bp.append(j)

            print(f"     Junctions within 50kb of breakpoint: {len(near_bp)}")
            for j in near_bp[:20]:
                print(f"       {j}")

            target_results['splice_junctions_list'] = {
                'total_junctions': len(junctions),
                'near_breakpoint': len(near_bp),
            }

        else:
            # Unknown format - inspect
            print(f"     Attributes: {[a for a in dir(sj) if not a.startswith('_')]}")
            if hasattr(sj, 'to_dict'):
                print(f"     Dict keys: {list(sj.to_dict().keys())[:10]}")

    except Exception as e:
        print(f"     SPLICE_JUNCTIONS ERROR: {e}")
        import traceback
        traceback.print_exc()

    # =============================================
    # 3. Variant effect on splice site usage
    # =============================================
    print(f"\n  3. Variant effects on splice site usage...")

    try:
        # Check available scorers
        available = list(variant_scorers_module.RECOMMENDED_VARIANT_SCORERS.keys())
        print(f"     Available recommended scorers: {available}")
    except:
        pass

    from alphagenome.models import variant_scorers as vs_mod

    # Try SPLICE_SITE_USAGE scorer
    splice_usage_scorer = vs_mod.CenterMaskScorer(
        requested_output=dna_client.OutputType.SPLICE_SITE_USAGE,
        width=501,
        aggregation_type=vs_mod.AggregationType.DIFF_MEAN,
    )

    alt_bases = ['A', 'C', 'G', 'T']
    variant_effects = []

    for alt in alt_bases:
        variant = genome.Variant(
            chromosome=chrom, position=pos,
            reference_bases='N', alternate_bases=alt,
        )

        try:
            scores = dna_model.score_variant(
                interval=interval,
                variant=variant,
                variant_scorers=[splice_usage_scorer],
            )

            adata = scores[0]
            vals_v = adata.X.flatten()
            meta_v = adata.var
            actual_var = adata.uns.get('variant', variant)
            max_effect = float(np.max(np.abs(vals_v)))

            if max_effect > 0.001:
                print(f"     {actual_var}: max splice usage effect = "
                      f"{max_effect:.6f}")

                # Top affected tracks
                top_idx = np.argsort(np.abs(vals_v))[-5:][::-1]
                for idx in top_idx:
                    if abs(vals_v[idx]) > 0.001:
                        tissue = meta_v.iloc[idx].get(
                            'biosample_name',
                            meta_v.iloc[idx].get('name', ''))
                        print(f"       {tissue:40s} "
                              f"effect={vals_v[idx]:+.6f}")

            variant_effects.append({
                'variant': str(actual_var),
                'max_effect': max_effect,
                'mean_abs_effect': float(np.mean(np.abs(vals_v))),
            })

        except Exception as e:
            print(f"     ERROR ({alt}): {e}")

    target_results['variant_splice_effects'] = variant_effects

    # =============================================
    # 4. SPLICE_SITES (standard) with visualization
    #    including transcript annotation
    # =============================================
    print(f"\n  4. Standard splice sites with gene context...")

    try:
        output_ss = dna_model.predict_interval(
            interval=interval,
            requested_outputs=[dna_client.OutputType.SPLICE_SITES],
            ontology_terms=None,
        )

        ss = output_ss.splice_sites
        vals_ss = ss.values
        meta_ss = ss.metadata

        center_ss = vals_ss.shape[0] // 2

        # Built-in AlphaGenome visualization with transcripts
        try:
            # Zoomed view: 20kb around breakpoint
            zoom_interval = genome.Interval(
                chrom, pos - 10000, pos + 10000
            )

            plot_components.plot(
                components=[
                    plot_components.TranscriptAnnotation(
                        transcripts, fig_height=0.2),
                    plot_components.Tracks(ss, fig_height=0.8),
                ],
                interval=zoom_interval,
                annotations=[
                    plot_components.VariantAnnotation(
                        [genome.Variant(chrom, pos, 'N', 'N')],
                        alpha=0.8,
                    ),
                ],
                fig_width=22,
            )
            plt.suptitle(
                f'Splice Sites with Gene Context: {label}\n'
                f'20kb window | Breakpoint marked',
                fontsize=13, y=1.02)
            plt.savefig(f'{OUTPUT_DIR}/{name}_splice_sites_context.png',
                        dpi=150, bbox_inches='tight', facecolor='white')
            plt.close('all')
            print(f"     Saved: {OUTPUT_DIR}/{name}_splice_sites_context.png")
        except Exception as e:
            print(f"     Context plot error: {e}")

        # Count splice sites near breakpoint
        for w in [500, 2000, 10000]:
            w_vals = vals_ss[center_ss - w:center_ss + w, :]
            donors = 0
            acceptors = 0
            for i, (_, row) in enumerate(meta_ss.iterrows()):
                col = w_vals[:, i]
                high = np.sum(col > 0.5)
                track_name = row.get('name', '')
                if 'donor' in track_name.lower():
                    donors += high
                elif 'acceptor' in track_name.lower():
                    acceptors += high

            print(f"     Within {w}bp: {donors} donors, "
                  f"{acceptors} acceptors (score > 0.5)")

        target_results['splice_sites_near_bp'] = {
            'within_500bp': int(np.sum(vals_ss[center_ss-500:center_ss+500, :] > 0.5)),
            'within_2kb': int(np.sum(vals_ss[center_ss-2000:center_ss+2000, :] > 0.5)),
            'within_10kb': int(np.sum(vals_ss[center_ss-10000:center_ss+10000, :] > 0.5)),
        }

    except Exception as e:
        print(f"     SPLICE_SITES ERROR: {e}")
        import traceback
        traceback.print_exc()

    all_results[name] = target_results
    print()

# Save results
output_path = f'{OUTPUT_DIR}/splice_junction_results.json'
with open(output_path, 'w') as f:
    json.dump(all_results, f, indent=2, default=str)
print(f"\nResults saved to {output_path}")

# Summary
print("\n" + "=" * 70)
print("SPLICE JUNCTION ANALYSIS SUMMARY")
print("=" * 70)
for target in targets:
    name = target['name']
    label = target['label']
    if name in all_results:
        data = all_results[name]
        ss_near = data.get('splice_sites_near_bp', {})
        print(f"\n  {label}:")
        print(f"    Splice sites within 500bp: {ss_near.get('within_500bp', 'N/A')}")
        print(f"    Splice sites within 2kb: {ss_near.get('within_2kb', 'N/A')}")
        print(f"    Splice sites within 10kb: {ss_near.get('within_10kb', 'N/A')}")
        ve = data.get('variant_splice_effects', [])
        if ve:
            max_eff = max(v['max_effect'] for v in ve)
            print(f"    Max variant splice effect: {max_eff:.6f}")

print(f"\nAll images saved to {OUTPUT_DIR}/")
print("Done.")
