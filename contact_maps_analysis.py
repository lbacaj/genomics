"""Contact Maps / 3D Chromatin Structure analysis at each breakpoint.

Predicts Hi-C-like contact maps using AlphaGenome to reveal:
1. TAD (Topologically Associating Domain) boundaries at each breakpoint
2. Enhancer-promoter loops that the translocation disrupts
3. Insulation scores to quantify boundary strength

Uses multiple cell lines (IMR90, HFFc6, HCT116, HepG2) where Hi-C data
is available via the 4D Nucleome project.

Generates PNG heatmap images for each breakpoint.
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
matplotlib.use('Agg')  # Non-interactive backend for saving images

from alphagenome.models import dna_client
from alphagenome.data import genome
from alphagenome.data import gene_annotation
from alphagenome.data import transcript as transcript_utils
from alphagenome.visualization import plot_components
import matplotlib.pyplot as plt
import numpy as np
import json
from scipy.signal import argrelextrema

print("Connecting to AlphaGenome API...")
dna_model = dna_client.create(os.environ['ALPHA_GENOME_API_KEY'])
print("Connected.\n")

# Load GTF for gene annotations
print("Loading gene annotations...")
import pandas as pd
gtf = pd.read_feather(
    'https://storage.googleapis.com/alphagenome/reference/gencode/'
    'hg38/gencode.v46.annotation.gtf.gz.feather'
)
gtf_transcripts = gene_annotation.filter_protein_coding(gtf)
gtf_transcripts = gene_annotation.filter_to_mane_select_transcript(gtf_transcripts)
transcript_extractor = transcript_utils.TranscriptExtractor(gtf_transcripts)
print("Done.\n")

targets = [
    {'name': 'ASPSCR1',     'chrom': 'chr17', 'pos': 82010811,
     'label': 'ASPSCR1 (chr17:82,010,811)'},
    {'name': 'TFE3',        'chrom': 'chrX',  'pos': 49043986,
     'label': 'TFE3 (chrX:49,043,986)'},
    {'name': 'DNMT1_chr1',  'chrom': 'chr1',  'pos': 31048832,
     'label': 'DNMT1 partner (chr1:31,048,832)'},
    {'name': 'DNMT1_chr19', 'chrom': 'chr19', 'pos': 10160241,
     'label': 'DNMT1 primary (chr19:10,160,241)'},
]

# Cell lines with actual Hi-C contact map data in AlphaGenome (4DN project)
contact_map_terms = [
    ('EFO:0001196', 'IMR90'),       # IMR90 fibroblast - best for normal tissue baseline
    ('EFO:0009318', 'HFFc6'),       # HFFc6 foreskin fibroblast - 2 tracks
    ('EFO:0002824', 'HCT116'),      # HCT116 colon cancer - 2 tracks
    ('EFO:0001187', 'HepG2'),       # HepG2 liver cancer
]

OUTPUT_DIR = '/Users/lbacaj/genomics/contact_maps'
os.makedirs(OUTPUT_DIR, exist_ok=True)

all_results = {}


def compute_insulation_score(mat, window_size):
    """Compute insulation score along the diagonal of a contact matrix."""
    n = mat.shape[0]
    insulation = np.zeros(n)
    for i in range(window_size, n - window_size):
        # Diamond insulation: mean of contacts within window on one side
        upstream = mat[i - window_size:i, i - window_size:i]
        downstream = mat[i:i + window_size, i:i + window_size]
        cross = mat[i - window_size:i, i:i + window_size]
        insulation[i] = np.mean(cross) / (np.mean(upstream) + np.mean(downstream) + 1e-10)
    return insulation


def find_tad_boundaries(insulation, order=10):
    """Find TAD boundaries as local minima in insulation score."""
    # Boundaries are where insulation drops (fewer cross-boundary contacts)
    minima = argrelextrema(insulation, np.less, order=order)[0]
    # Filter to positions with actual signal
    valid = minima[insulation[minima] > 0]
    if len(valid) == 0:
        return minima
    # Keep only significant boundaries (below median insulation)
    threshold = np.median(insulation[insulation > 0])
    significant = valid[insulation[valid] < threshold]
    return significant if len(significant) > 0 else valid


def find_nearby_genes(gtf, chrom, pos, window=500000):
    """Find genes near a position."""
    genes = gtf[
        (gtf['Chromosome'] == chrom) &
        (gtf['Feature'] == 'gene') &
        (gtf['Start'] <= pos + window) &
        (gtf['End'] >= pos - window)
    ].copy()
    if 'gene_name' in genes.columns:
        genes = genes.rename(columns={'Start': 'start', 'End': 'end', 'Strand': 'strand'})
        genes = genes.sort_values('start')
        return genes[['gene_name', 'start', 'end', 'strand']].drop_duplicates('gene_name')
    return pd.DataFrame()


for target in targets:
    name = target['name']
    chrom = target['chrom']
    pos = target['pos']
    label = target['label']

    print("=" * 70)
    print(f"CONTACT MAP: {label}")
    print("=" * 70)

    # Use 1MB context for maximum range (512x512 at 2048bp resolution)
    interval = genome.Interval(chrom, pos, pos + 1).resize(
        dna_client.SEQUENCE_LENGTH_1MB
    )
    resolution = interval.width / 512  # 2048bp per bin
    print(f"  Interval: {interval}")
    print(f"  Resolution: {resolution:.0f}bp per bin")

    # Extract transcripts for gene annotation
    transcripts = transcript_extractor.extract(interval)

    # Find nearby genes for the report
    nearby = find_nearby_genes(gtf, chrom, pos, window=interval.width // 2)
    if len(nearby) > 0:
        print(f"  Genes in window: {len(nearby)}")
        # Find genes closest to breakpoint
        nearby['distance'] = nearby.apply(
            lambda r: min(abs(r['start'] - pos), abs(r['end'] - pos)), axis=1
        )
        closest = nearby.nsmallest(5, 'distance')
        print(f"  5 closest genes:")
        for _, g in closest.iterrows():
            print(f"    {g['gene_name']:15s} {g['start']:>12,}-{g['end']:>12,} "
                  f"({g['distance']:>8,}bp away)")

    # Collect all contact maps across cell lines
    for term, cell_line in contact_map_terms:
        print(f"\n  --- Cell line: {cell_line} ({term}) ---")

        try:
            output = dna_model.predict_interval(
                interval=interval,
                requested_outputs=[dna_client.OutputType.CONTACT_MAPS],
                ontology_terms=[term],
            )

            contact = output.contact_maps
            values = contact.values
            metadata = contact.metadata

            n_tracks = values.shape[2] if len(values.shape) == 3 else 0
            print(f"  Shape: {values.shape}, tracks: {n_tracks}")

            if n_tracks == 0:
                print(f"  No tracks for {cell_line}, skipping.")
                continue

            for _, row in metadata.iterrows():
                print(f"    Track: {row.get('name', 'unknown')} | "
                      f"{row.get('biosample_name', 'unknown')}")

            # =============================================
            # IMAGE 1: AlphaGenome built-in visualization
            # =============================================
            try:
                plot_components.plot(
                    components=[
                        plot_components.TranscriptAnnotation(
                            transcripts, fig_height=0.15
                        ),
                        plot_components.ContactMaps(
                            contact, track_height=12.0
                        ),
                    ],
                    interval=interval,
                    annotations=[
                        plot_components.VariantAnnotation(
                            [genome.Variant(chrom, pos, 'N', 'N')],
                            alpha=0.8,
                        ),
                    ],
                    fig_width=22,
                )
                plt.suptitle(
                    f'Contact Map: {label} | {cell_line}\n'
                    f'Breakpoint marked with vertical line | '
                    f'Resolution: {resolution:.0f}bp/bin',
                    fontsize=13, y=1.02
                )
                fname = f'{OUTPUT_DIR}/{name}_{cell_line}_builtin.png'
                plt.savefig(fname, dpi=150, bbox_inches='tight',
                            facecolor='white')
                plt.close('all')
                print(f"  Saved: {fname}")
            except Exception as e:
                print(f"  Built-in plot error: {e}")

            # =============================================
            # IMAGE 2: Manual heatmap + insulation + TADs
            # for each track
            # =============================================
            for track_idx in range(n_tracks):
                cmap_matrix = values[:, :, track_idx]
                track_name = metadata.iloc[track_idx].get(
                    'biosample_name',
                    metadata.iloc[track_idx].get('name', f'track_{track_idx}')
                )
                track_id = metadata.iloc[track_idx].get('name', f'track_{track_idx}')

                n = cmap_matrix.shape[0]
                bp_bin = n // 2  # breakpoint is centered

                # Make symmetric
                mat = cmap_matrix.copy()
                mat = mat + mat.T - np.diag(np.diag(mat))

                # Compute insulation score
                window = min(25, n // 20)  # ~50kb window at 2048bp resolution
                insulation = compute_insulation_score(mat, window)

                # Normalize
                ins_max = np.max(insulation)
                insulation_norm = insulation / ins_max if ins_max > 0 else insulation

                # Find TAD boundaries
                tad_boundaries = find_tad_boundaries(insulation, order=max(5, window))

                print(f"\n  Track {track_idx}: {track_id}")
                print(f"  Matrix: {n}x{n}, window={window} bins ({window * resolution:.0f}bp)")
                print(f"  TAD boundaries found: {len(tad_boundaries)}")
                print(f"  Insulation at breakpoint: {insulation_norm[bp_bin]:.4f}")

                # Check if breakpoint is at a TAD boundary
                at_boundary = False
                nearest_dist_bp = None
                if len(tad_boundaries) > 0:
                    distances = np.abs(tad_boundaries - bp_bin)
                    nearest_idx = np.argmin(distances)
                    nearest_dist_bp = int(distances[nearest_idx] * resolution)
                    at_boundary = distances[nearest_idx] <= window
                    print(f"  Nearest TAD boundary: {nearest_dist_bp:,}bp from breakpoint")
                    if at_boundary:
                        print(f"  ** BREAKPOINT IS AT/NEAR A TAD BOUNDARY **")

                # Map TAD boundaries to genomic positions
                tad_genomic = []
                for tb in tad_boundaries:
                    gpos = interval.start + int(tb * resolution)
                    tad_genomic.append(gpos)
                    dist = abs(gpos - pos)
                    # Find genes at this boundary
                    boundary_genes = nearby[
                        (nearby['start'] <= gpos + 50000) &
                        (nearby['end'] >= gpos - 50000)
                    ] if len(nearby) > 0 else pd.DataFrame()
                    gene_str = ', '.join(boundary_genes['gene_name'].tolist()[:3]) if len(boundary_genes) > 0 else 'none'
                    print(f"    Boundary at {chrom}:{gpos:,} "
                          f"({dist:,}bp from breakpoint) | genes: {gene_str}")

                # ---- Generate the figure ----
                fig = plt.figure(figsize=(18, 20))
                gs = fig.add_gridspec(3, 1, height_ratios=[5, 1.2, 1.2],
                                      hspace=0.25)

                # Panel 1: Contact map heatmap
                ax1 = fig.add_subplot(gs[0])
                mat_log = np.log1p(np.clip(mat, 0, None))
                im = ax1.imshow(mat_log, cmap='YlOrRd', aspect='equal',
                                interpolation='nearest',
                                origin='upper')

                # Mark breakpoint with crosshair
                ax1.axvline(bp_bin, color='cyan', linewidth=2.5,
                            linestyle='--', alpha=0.9, label='Breakpoint')
                ax1.axhline(bp_bin, color='cyan', linewidth=2.5,
                            linestyle='--', alpha=0.9)

                # Mark TAD boundaries
                for i, tb in enumerate(tad_boundaries):
                    lbl = 'TAD boundaries' if i == 0 else None
                    ax1.axvline(tb, color='#4444FF', linewidth=1.5,
                                linestyle=':', alpha=0.6, label=lbl)
                    ax1.axhline(tb, color='#4444FF', linewidth=1.5,
                                linestyle=':', alpha=0.6)

                # Tick labels as genomic positions
                n_ticks = 9
                tick_pos = np.linspace(0, n - 1, n_ticks).astype(int)
                tick_labs = [f"{(interval.start + int(tp * resolution)) / 1e6:.2f}M"
                             for tp in tick_pos]
                ax1.set_xticks(tick_pos)
                ax1.set_xticklabels(tick_labs, rotation=45, fontsize=9)
                ax1.set_yticks(tick_pos)
                ax1.set_yticklabels(tick_labs, fontsize=9)
                ax1.set_title(
                    f'Hi-C Contact Map: {label}\n'
                    f'{cell_line} ({track_id}) | Resolution: {resolution:.0f}bp/bin',
                    fontsize=14, fontweight='bold', pad=15
                )
                ax1.legend(loc='upper right', fontsize=11,
                           framealpha=0.9, edgecolor='black')
                cbar = plt.colorbar(im, ax=ax1,
                                    label='log(1 + contact frequency)',
                                    shrink=0.7, pad=0.02)

                # Panel 2: Insulation score
                ax2 = fig.add_subplot(gs[1])
                x = np.arange(n)
                ax2.fill_between(x, insulation_norm, alpha=0.3, color='gray')
                ax2.plot(x, insulation_norm, color='black', linewidth=1.5)
                ax2.axvline(bp_bin, color='cyan', linewidth=2.5,
                            linestyle='--', alpha=0.9, label='Breakpoint')
                for i, tb in enumerate(tad_boundaries):
                    lbl = 'TAD boundaries' if i == 0 else None
                    ax2.axvline(tb, color='#4444FF', linewidth=1.5,
                                linestyle=':', alpha=0.6, label=lbl)
                ax2.scatter(tad_boundaries,
                            insulation_norm[tad_boundaries] if len(tad_boundaries) > 0 else [],
                            color='red', s=60, zorder=5,
                            label='Boundary positions', edgecolors='black')
                ax2.set_xlim(0, n)
                ax2.set_xticks(tick_pos)
                ax2.set_xticklabels(tick_labs, rotation=45, fontsize=9)
                ax2.set_ylabel('Insulation\nScore', fontsize=11)
                ax2.set_title('TAD Boundary Detection '
                              '(minima = domain boundaries)', fontsize=12)
                ax2.legend(loc='upper right', fontsize=9)

                # Panel 3: Contact frequency at breakpoint row
                ax3 = fig.add_subplot(gs[2])
                bp_row = mat[bp_bin, :]
                ax3.fill_between(x, bp_row, alpha=0.3, color='orange')
                ax3.plot(x, bp_row, color='darkorange', linewidth=1.5)
                ax3.axvline(bp_bin, color='cyan', linewidth=2.5,
                            linestyle='--', alpha=0.9, label='Breakpoint')
                for i, tb in enumerate(tad_boundaries):
                    lbl = 'TAD boundaries' if i == 0 else None
                    ax3.axvline(tb, color='#4444FF', linewidth=1.5,
                                linestyle=':', alpha=0.6, label=lbl)
                ax3.set_xlim(0, n)
                ax3.set_xticks(tick_pos)
                ax3.set_xticklabels(tick_labs, rotation=45, fontsize=9)
                ax3.set_ylabel('Contact\nFrequency', fontsize=11)
                ax3.set_xlabel(f'Genomic Position ({chrom})', fontsize=12)
                ax3.set_title('Contact frequency profile at breakpoint '
                              '(row slice through matrix)', fontsize=12)
                ax3.legend(loc='upper right', fontsize=9)

                safe = f"{cell_line}_t{track_idx}"
                fname = f'{OUTPUT_DIR}/{name}_{safe}_analysis.png'
                plt.savefig(fname, dpi=150, bbox_inches='tight',
                            facecolor='white')
                plt.close('all')
                print(f"  Saved: {fname}")

                # Store results
                result_key = f'{name}_{cell_line}_t{track_idx}'
                all_results[result_key] = {
                    'target': name,
                    'cell_line': cell_line,
                    'track_id': track_id,
                    'matrix_shape': [n, n],
                    'resolution_bp': float(resolution),
                    'n_tad_boundaries': int(len(tad_boundaries)),
                    'tad_boundary_bins': [int(tb) for tb in tad_boundaries],
                    'tad_boundary_genomic': [int(g) for g in tad_genomic],
                    'breakpoint_bin': int(bp_bin),
                    'breakpoint_at_tad_boundary': bool(at_boundary),
                    'nearest_boundary_distance_bp': int(nearest_dist_bp) if nearest_dist_bp is not None else None,
                    'insulation_at_breakpoint': float(insulation_norm[bp_bin]),
                }

        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback
            traceback.print_exc()
            continue

    print()

# Save structured results
output_path = '/Users/lbacaj/genomics/contact_map_results.json'
with open(output_path, 'w') as f:
    json.dump(all_results, f, indent=2)
print(f"\nStructured results saved to {output_path}")

# =============================================
# SUMMARY
# =============================================
print("\n" + "=" * 70)
print("CONTACT MAP ANALYSIS SUMMARY")
print("=" * 70)
for target in targets:
    tname = target['name']
    label = target['label']
    matching = {k: v for k, v in all_results.items() if k.startswith(tname + '_')}
    if not matching:
        print(f"\n  {label}: No data")
        continue

    print(f"\n  {label}:")
    for key, data in matching.items():
        cl = data['cell_line']
        n_tads = data['n_tad_boundaries']
        at_bd = data['breakpoint_at_tad_boundary']
        ins = data['insulation_at_breakpoint']
        nearest = data.get('nearest_boundary_distance_bp')
        nearest_str = f"{nearest:,}bp" if nearest is not None else "N/A"
        print(f"    {cl:10s} | TADs: {n_tads:2d} | "
              f"At boundary: {'YES' if at_bd else 'no ':3s} | "
              f"Nearest: {nearest_str:>10s} | "
              f"Insulation: {ins:.4f}")

print(f"\nAll images saved to {OUTPUT_DIR}/")
print("Done.")
