"""Extension 3: Deep ISM at the critical ASPSCR1 position.

The initial ISM identified chr17:82,010,800 as the most functionally
critical position near the ASPSCR1 breakpoint. This script runs a wider
256bp ISM window to map the full regulatory element, and also runs ISM
at each of the other breakpoints with a wider window.

Also runs DNASE ISM to map chromatin accessibility sensitivity.
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
from alphagenome.interpretation import ism
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

# ISM scorers - RNA_SEQ and DNASE
rna_scorer = variant_scorers.CenterMaskScorer(
    requested_output=dna_client.OutputType.RNA_SEQ,
    width=501,
    aggregation_type=variant_scorers.AggregationType.DIFF_MEAN,
)

dnase_scorer = variant_scorers.CenterMaskScorer(
    requested_output=dna_client.OutputType.DNASE,
    width=501,
    aggregation_type=variant_scorers.AggregationType.DIFF_MEAN,
)

all_results = {}

for target in targets:
    name = target['name']
    chrom = target['chrom']
    pos = target['pos']

    print("=" * 70)
    print(f"DEEP ISM: {name} ({chrom}:{pos:,})")
    print("=" * 70)

    # 16KB context, 256bp ISM window centered on breakpoint
    sequence_interval = genome.Interval(chrom, pos, pos + 1).resize(
        dna_client.SEQUENCE_LENGTH_16KB
    )
    ism_interval = genome.Interval(chrom, pos - 128, pos + 128)

    print(f"  Context: {sequence_interval}")
    print(f"  ISM window: {ism_interval} ({ism_interval.width}bp)")
    print(f"  Total variants: {ism_interval.width * 3}")

    for scorer, scorer_name in [(rna_scorer, 'RNA_SEQ'), (dnase_scorer, 'DNASE')]:
        print(f"\n  Scorer: {scorer_name}")

        try:
            ism_scores = dna_model.score_ism_variants(
                interval=sequence_interval,
                ism_interval=ism_interval,
                variant_scorers=[scorer],
            )

            print(f"  Scored {len(ism_scores)} variants")

            # Aggregate: find max effect per tissue across all positions
            tissue_effects = {}
            # Also track per-position max for positional map
            position_max = {}

            for var_scores in ism_scores:
                adata = var_scores[0]
                vals = adata.X.flatten()
                meta = adata.var
                variant_str = str(adata.uns.get('variant', ''))

                # Parse position from variant string
                parts = variant_str.split(':')
                if len(parts) >= 2:
                    try:
                        var_pos = int(parts[1])
                    except ValueError:
                        var_pos = 0
                else:
                    var_pos = 0

                # Track max absolute effect at each position
                max_abs = float(np.max(np.abs(vals)))
                if var_pos not in position_max or max_abs > position_max[var_pos]['abs_score']:
                    position_max[var_pos] = {
                        'position': var_pos,
                        'abs_score': max_abs,
                        'variant': variant_str,
                    }

                # Track per-tissue max
                for i, (_, row) in enumerate(meta.iterrows()):
                    tissue = row.get('biosample_name', row.get('name', 'unknown'))
                    score = abs(vals[i])
                    key = (tissue, row.get('name', ''))
                    if key not in tissue_effects or score > tissue_effects[key]['abs_score']:
                        tissue_effects[key] = {
                            'biosample_name': tissue,
                            'name': row.get('name', ''),
                            'max_score': float(vals[i]),
                            'abs_score': score,
                            'variant': variant_str,
                        }

            # Top tissues
            if tissue_effects:
                df_tissues = pd.DataFrame(tissue_effects.values())
                top = df_tissues.nlargest(15, 'abs_score')
                print(f"\n  Top 15 tissues by max ISM effect ({scorer_name}):")
                for _, r in top.iterrows():
                    print(f"    {r['biosample_name']:50s} Score: {r['max_score']:+.6f}  ({r['variant']})")
                all_results[f'{name}_{scorer_name}_tissues'] = df_tissues

            # Top positions (most sensitive bases)
            if position_max:
                df_pos = pd.DataFrame(position_max.values())
                df_pos = df_pos.sort_values('abs_score', ascending=False)
                top_pos = df_pos.head(10)
                print(f"\n  Top 10 most sensitive positions ({scorer_name}):")
                for _, r in top_pos.iterrows():
                    dist = r['position'] - pos
                    direction = f"+{dist}" if dist >= 0 else str(dist)
                    print(f"    Position {r['position']}  (breakpoint{direction:>5s})  "
                          f"max_effect={r['abs_score']:.6f}  ({r['variant']})")
                all_results[f'{name}_{scorer_name}_positions'] = df_pos

        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback
            traceback.print_exc()
            continue

# Save
output_path = '/Users/lbacaj/genomics/deep_ism_results.json'
serializable = {}
for key, df in all_results.items():
    serializable[key] = df.to_dict(orient='records')
with open(output_path, 'w') as f:
    json.dump(serializable, f, indent=2)
print(f"\nResults saved to {output_path}")
