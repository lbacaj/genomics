"""Extension 4: Splicing and 3D contact analysis at breakpoints.

Translocations disrupt splicing at the breakpoint exons.
This script analyzes:
1. Splice site predictions at each breakpoint
2. Variant effects on splicing
3. Chromatin accessibility (DNASE/ATAC) to assess regulatory openness
"""

import os
import sys
sys.path = [p for p in sys.path if p not in ('', '.', os.getcwd())]

with open('/Users/lbacaj/genomics/.env') as f:
    for line in f:
        if '=' in line:
            k, v = line.strip().split('=', 1)
            os.environ[k] = v

from alphagenome.models import dna_client
from alphagenome.models import variant_scorers
from alphagenome.data import genome
from alphagenome.data import gene_annotation
from alphagenome.data import transcript as transcript_utils
import pandas as pd
import numpy as np
import json

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

targets = [
    {'name': 'ASPSCR1',     'chrom': 'chr17', 'pos': 82010811},
    {'name': 'TFE3',        'chrom': 'chrX',  'pos': 49043986},
    {'name': 'DNMT1_chr1',  'chrom': 'chr1',  'pos': 31048832},
    {'name': 'DNMT1_chr19', 'chrom': 'chr19', 'pos': 10160241},
]

# Splice-relevant ontology terms
splice_tissues = [
    'UBERON:0002048',  # Lung
    'UBERON:0000955',  # Brain
    'UBERON:0002107',  # Liver
    'UBERON:0000948',  # Heart
    'UBERON:0001157',  # Transverse colon
]

all_results = {}

for target in targets:
    name = target['name']
    chrom = target['chrom']
    pos = target['pos']

    print("=" * 70)
    print(f"SPLICING & ACCESSIBILITY: {name} ({chrom}:{pos:,})")
    print("=" * 70)

    # --- SPLICE SITE PREDICTIONS ---
    print("\n  1. Splice site predictions:")
    interval = genome.Interval(chrom, pos, pos + 1).resize(
        dna_client.SEQUENCE_LENGTH_1MB
    )

    try:
        output = dna_model.predict_interval(
            interval=interval,
            requested_outputs=[dna_client.OutputType.SPLICE_SITES],
        )

        splice = output.splice_sites
        values = splice.values
        metadata = splice.metadata

        print(f"     Shape: {values.shape}")
        print(f"     Tracks: {len(metadata)}")

        # Look at splice signal in 1kb window around breakpoint
        center = values.shape[0] // 2
        window = 500
        center_vals = values[center - window:center + window, :]

        # Find positions with high splice site scores
        for i, (_, row) in enumerate(metadata.iterrows()):
            col = center_vals[:, i]
            top_positions = np.argsort(col)[-5:][::-1]
            top_scores = col[top_positions]

            print(f"     Track: {row.get('name', 'unknown')}")
            for p, s in zip(top_positions, top_scores):
                genome_pos = pos - window + p
                dist = genome_pos - pos
                if s > 0.01:
                    print(f"       Position {genome_pos} (breakpoint{dist:+d}): score={s:.4f}")

        all_results[f'{name}_splice'] = {
            'shape': list(values.shape),
            'n_tracks': len(metadata),
        }

    except Exception as e:
        print(f"     ERROR: {e}")

    # --- CHROMATIN ACCESSIBILITY ---
    print(f"\n  2. Chromatin accessibility (DNASE + ATAC):")

    for modality, mod_name in [
        (dna_client.OutputType.DNASE, 'DNASE'),
        (dna_client.OutputType.ATAC, 'ATAC'),
    ]:
        try:
            output = dna_model.predict_interval(
                interval=interval,
                requested_outputs=[modality],
                ontology_terms=splice_tissues,
            )

            track_data = getattr(output, mod_name.lower())
            values = track_data.values
            metadata = track_data.metadata

            center = values.shape[0] // 2
            window = 500

            print(f"\n     {mod_name} - {len(metadata)} tracks")
            print(f"     Signal in 1kb around breakpoint:")

            track_info = []
            for i, (_, row) in enumerate(metadata.iterrows()):
                col = values[center - window:center + window, i]
                track_info.append({
                    'target': name,
                    'modality': mod_name,
                    'track_name': row.get('name', ''),
                    'biosample_name': row.get('biosample_name', ''),
                    'center_1kb_mean': float(np.mean(col)),
                    'center_1kb_max': float(np.max(col)),
                    'at_breakpoint': float(values[center, i]),
                })
                print(f"       {row.get('name', ''):50s} mean={np.mean(col):.4f}  "
                      f"max={np.max(col):.4f}  at_bp={values[center, i]:.4f}")

            all_results[f'{name}_{mod_name}'] = track_info

        except Exception as e:
            print(f"     {mod_name} ERROR: {e}")

    # --- SPLICING VARIANT SCORING ---
    print(f"\n  3. Variant effect on splicing:")

    splice_scorer = variant_scorers.RECOMMENDED_VARIANT_SCORERS.get('SPLICE_SITE_USAGE')
    if splice_scorer is None:
        # Try to find any splice-related scorer
        available = list(variant_scorers.RECOMMENDED_VARIANT_SCORERS.keys())
        print(f"     Available scorers: {available}")
        splice_keys = [k for k in available if 'SPLICE' in k.upper()]
        if splice_keys:
            splice_scorer = variant_scorers.RECOMMENDED_VARIANT_SCORERS[splice_keys[0]]
            print(f"     Using scorer: {splice_keys[0]}")
        else:
            print(f"     No splice scorer available, using CenterMaskScorer on SPLICE_SITES")
            splice_scorer = variant_scorers.CenterMaskScorer(
                requested_output=dna_client.OutputType.SPLICE_SITES,
                width=501,
                aggregation_type=variant_scorers.AggregationType.DIFF_MEAN,
            )

    for alt in ['A', 'C', 'G', 'T']:
        variant = genome.Variant(
            chromosome=chrom,
            position=pos,
            reference_bases='N',
            alternate_bases=alt,
        )

        try:
            scores = dna_model.score_variant(
                interval=interval,
                variant=variant,
                variant_scorers=[splice_scorer],
            )

            adata = scores[0]
            vals = adata.X.flatten()
            max_effect = float(np.max(np.abs(vals)))
            actual_var = adata.uns.get('variant', variant)

            if max_effect > 0.001:
                print(f"     {actual_var}: max splice effect = {max_effect:.6f}")

            all_results[f'{name}_splice_variant_{alt}'] = {
                'variant': str(actual_var),
                'max_effect': max_effect,
                'mean_effect': float(np.mean(np.abs(vals))),
            }

        except Exception as e:
            print(f"     ERROR ({alt}): {e}")

    # --- GENE TRANSCRIPTS AT BREAKPOINT ---
    print(f"\n  4. Transcripts at breakpoint:")
    try:
        transcripts = transcript_extractor.extract(interval)
        # Find transcripts near the breakpoint
        for t in transcripts:
            if hasattr(t, 'start') and hasattr(t, 'end'):
                if t.start <= pos <= t.end:
                    print(f"     BREAKPOINT WITHIN: {t}")
                elif abs(t.start - pos) < 50000 or abs(t.end - pos) < 50000:
                    print(f"     NEARBY (<50kb): {t}")
    except Exception as e:
        print(f"     ERROR: {e}")

# Save
output_path = '/Users/lbacaj/genomics/splicing_accessibility_results.json'
with open(output_path, 'w') as f:
    json.dump(all_results, f, indent=2, default=str)
print(f"\nResults saved to {output_path}")
