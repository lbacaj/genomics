"""Extension 1: Multi-modal analysis at each breakpoint.

Score each breakpoint across ALL output types (not just RNA_SEQ):
DNASE, ATAC, CAGE, CHIP_HISTONE, CHIP_TF, SPLICE_SITES
This reveals the full regulatory landscape at each translocation site.
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
import pandas as pd
import numpy as np
import json

print("Connecting to AlphaGenome API...")
dna_model = dna_client.create(os.environ['ALPHA_GENOME_API_KEY'])
print("Connected.\n")

targets = [
    {'name': 'ASPSCR1',     'chrom': 'chr17', 'pos': 82010811},
    {'name': 'TFE3',        'chrom': 'chrX',  'pos': 49043986},
    {'name': 'DNMT1_chr1',  'chrom': 'chr1',  'pos': 31048832},
    {'name': 'DNMT1_chr19', 'chrom': 'chr19', 'pos': 10160241},
]

# All modalities to test
modalities = [
    dna_client.OutputType.DNASE,
    dna_client.OutputType.ATAC,
    dna_client.OutputType.CAGE,
    dna_client.OutputType.CHIP_HISTONE,
    dna_client.OutputType.CHIP_TF,
    dna_client.OutputType.SPLICE_SITES,
    dna_client.OutputType.PROCAP,
]

# Use only UBERON tissue terms (broadly supported across modalities)
# CL: cell ontology terms are not supported for all modalities
ontology_terms = [
    'UBERON:0002048',  # Lung
    'UBERON:0000955',  # Brain
    'UBERON:0002107',  # Liver
    'UBERON:0000948',  # Heart
    'UBERON:0001157',  # Transverse colon
    'UBERON:0002113',  # Kidney
    'UBERON:0002106',  # Spleen
    'UBERON:0002370',  # Thymus
]

all_results = {}

for target in targets:
    name = target['name']
    chrom = target['chrom']
    pos = target['pos']

    print("=" * 70)
    print(f"TARGET: {name} ({chrom}:{pos:,})")
    print("=" * 70)

    interval = genome.Interval(chrom, pos, pos + 1).resize(
        dna_client.SEQUENCE_LENGTH_1MB
    )

    for modality in modalities:
        mod_name = modality.name
        print(f"\n  Modality: {mod_name}")

        try:
            # Some modalities (SPLICE_SITES, CONTACT_MAPS) don't use ontology terms
            # Others may only support certain terms. Try with terms first, fall back without.
            try:
                output = dna_model.predict_interval(
                    interval=interval,
                    requested_outputs=[modality],
                    ontology_terms=ontology_terms,
                )
            except Exception:
                print(f"    Retrying without ontology terms...")
                output = dna_model.predict_interval(
                    interval=interval,
                    requested_outputs=[modality],
                )

            # Get the track data for this modality
            attr_name = mod_name.lower()
            track_data = getattr(output, attr_name, None)

            if track_data is None:
                print(f"    No data returned for {mod_name}")
                continue

            values = track_data.values
            metadata = track_data.metadata

            print(f"    Predictions shape: {values.shape}")
            print(f"    Tracks: {len(metadata)}")

            # Compute per-track statistics in the center 10kb around breakpoint
            center = values.shape[0] // 2
            window = 5000  # 5kb each side
            center_vals = values[center - window:center + window, :]

            track_stats = []
            for i, (_, row) in enumerate(metadata.iterrows()):
                col_vals = center_vals[:, i]
                track_stats.append({
                    'target': name,
                    'modality': mod_name,
                    'track_name': row.get('name', ''),
                    'biosample_name': row.get('biosample_name', ''),
                    'center_mean': float(np.mean(col_vals)),
                    'center_max': float(np.max(col_vals)),
                    'center_sum': float(np.sum(col_vals)),
                })

            df = pd.DataFrame(track_stats)
            df = df.sort_values('center_mean', ascending=False)
            top = df.head(5)

            print(f"    Top 5 tracks by mean signal in 10kb center window:")
            for _, r in top.iterrows():
                print(f"      {r['track_name']:55s} mean={r['center_mean']:.4f}  max={r['center_max']:.4f}")

            all_results[f'{name}_{mod_name}'] = df

        except Exception as e:
            print(f"    ERROR: {e}")
            continue

# Save results
output_path = '/Users/lbacaj/genomics/multimodal_results.json'
serializable = {}
for key, df in all_results.items():
    serializable[key] = df.to_dict(orient='records')
with open(output_path, 'w') as f:
    json.dump(serializable, f, indent=2)

print(f"\n\nResults saved to {output_path}")

# Print summary
print("\n" + "=" * 70)
print("MULTI-MODAL SUMMARY")
print("=" * 70)

for target in targets:
    name = target['name']
    print(f"\n{name}:")
    for mod in modalities:
        key = f'{name}_{mod.name}'
        if key in all_results:
            df = all_results[key]
            top = df.nlargest(1, 'center_mean').iloc[0]
            print(f"  {mod.name:20s} -> Top: {top['track_name'][:45]:45s} (mean={top['center_mean']:.4f})")
