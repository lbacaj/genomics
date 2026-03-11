"""Comprehensive reproduction of Johnny's ASPS analysis using AlphaGenome.

Three approaches:
1. All 3 substitutions at each breakpoint (GeneMaskLFCScorer)
2. CenterMaskScorer with different aggregations
3. ISM around each breakpoint
"""

import os
import sys

# Avoid local alphagenome/ dir shadowing the installed package
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
import pickle

print("Connecting to AlphaGenome API...")
dna_model = dna_client.create(os.environ['ALPHA_GENOME_API_KEY'])
print("Connected.\n")

# Breakpoint coordinates in hg38
targets = [
    {'name': 'ASPSCR1',     'chrom': 'chr17', 'pos': 82010811},
    {'name': 'TFE3',        'chrom': 'chrX',  'pos': 49043986},
    {'name': 'DNMT1_chr1',  'chrom': 'chr1',  'pos': 31048832},
    {'name': 'DNMT1_chr19', 'chrom': 'chr19', 'pos': 10160241},
]

ALT_BASES = ['A', 'C', 'G', 'T']

all_results = {}

# ============================================================
# APPROACH 1: All 3 substitutions with GeneMaskLFCScorer
# ============================================================
print("=" * 70)
print("APPROACH 1: All substitutions with GeneMaskLFCScorer (recommended)")
print("=" * 70)

gene_scorer = variant_scorers.RECOMMENDED_VARIANT_SCORERS['RNA_SEQ']

for target in targets:
    name = target['name']
    chrom = target['chrom']
    pos = target['pos']

    print(f"\n--- {name} ({chrom}:{pos:,}) ---")

    interval = genome.Interval(chrom, pos, pos + 1).resize(
        dna_client.SEQUENCE_LENGTH_1MB
    )

    best_scores_per_tissue = {}

    for alt in ALT_BASES:
        variant = genome.Variant(
            chromosome=chrom,
            position=pos,
            reference_bases='N',  # placeholder; API uses actual ref genome
            alternate_bases=alt,
        )

        try:
            scores = dna_model.score_variant(
                interval=interval,
                variant=variant,
                variant_scorers=[gene_scorer],
            )
            tidy = variant_scorers.tidy_scores(scores, match_gene_strand=True)

            # Track max absolute score per tissue across substitutions
            for _, row in tidy.iterrows():
                tissue = row.get('biosample_name', row.get('name', 'unknown'))
                score = abs(row['raw_score'])
                key = (tissue, row.get('name', ''))
                if key not in best_scores_per_tissue or score > best_scores_per_tissue[key]['abs_score']:
                    best_scores_per_tissue[key] = {
                        'biosample_name': tissue,
                        'name': row.get('name', ''),
                        'raw_score': row['raw_score'],
                        'abs_score': score,
                        'alt_base': alt,
                        'quantile_score': row.get('quantile_score', None),
                    }

            actual_variant = scores[0].uns.get('variant', variant)
            print(f"  Scored {actual_variant} - {len(tidy)} tissue-gene pairs")

        except Exception as e:
            print(f"  ERROR with alt={alt}: {e}")
            continue

    # Show top 10 by max absolute score across all substitutions
    if best_scores_per_tissue:
        df = pd.DataFrame(best_scores_per_tissue.values())
        top = df.nlargest(10, 'abs_score')
        print(f"\n  Top 10 tissues (max across substitutions):")
        for _, r in top.iterrows():
            print(f"    {r['biosample_name']:50s} Score: {r['raw_score']:+.6f}  (alt={r['alt_base']})")
        all_results[f'approach1_{name}'] = df


# ============================================================
# APPROACH 2: CenterMaskScorer (different aggregations)
# ============================================================
print("\n\n" + "=" * 70)
print("APPROACH 2: CenterMaskScorer (DIFF_MEAN, width=501)")
print("=" * 70)

center_scorer = variant_scorers.CenterMaskScorer(
    requested_output=dna_client.OutputType.RNA_SEQ,
    width=501,
    aggregation_type=variant_scorers.AggregationType.DIFF_MEAN,
)

for target in targets:
    name = target['name']
    chrom = target['chrom']
    pos = target['pos']

    print(f"\n--- {name} ({chrom}:{pos:,}) ---")

    interval = genome.Interval(chrom, pos, pos + 1).resize(
        dna_client.SEQUENCE_LENGTH_1MB
    )

    best_scores = {}

    for alt in ALT_BASES:
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
                variant_scorers=[center_scorer],
            )

            adata = scores[0]
            # CenterMaskScorer returns shape (1, num_tracks)
            vals = adata.X.flatten()
            meta = adata.var

            for i, (_, row) in enumerate(meta.iterrows()):
                tissue = row.get('biosample_name', row.get('name', 'unknown'))
                score = abs(vals[i])
                key = (tissue, row.get('name', ''))
                if key not in best_scores or score > best_scores[key]['abs_score']:
                    best_scores[key] = {
                        'biosample_name': tissue,
                        'name': row.get('name', ''),
                        'raw_score': float(vals[i]),
                        'abs_score': score,
                        'alt_base': alt,
                    }

            actual_variant = adata.uns.get('variant', variant)
            print(f"  Scored {actual_variant} - {len(vals)} tracks")

        except Exception as e:
            print(f"  ERROR with alt={alt}: {e}")
            continue

    if best_scores:
        df = pd.DataFrame(best_scores.values())
        top = df.nlargest(10, 'abs_score')
        print(f"\n  Top 10 tissues (CenterMask, max across subs):")
        for _, r in top.iterrows():
            print(f"    {r['biosample_name']:50s} Score: {r['raw_score']:+.6f}  (alt={r['alt_base']})")
        all_results[f'approach2_{name}'] = df


# ============================================================
# APPROACH 3: ISM around each breakpoint
# ============================================================
print("\n\n" + "=" * 70)
print("APPROACH 3: In Silico Mutagenesis (ISM)")
print("  Using 16KB context, 64bp ISM window around each breakpoint")
print("=" * 70)

ism_scorer = variant_scorers.CenterMaskScorer(
    requested_output=dna_client.OutputType.RNA_SEQ,
    width=501,
    aggregation_type=variant_scorers.AggregationType.DIFF_MEAN,
)

for target in targets:
    name = target['name']
    chrom = target['chrom']
    pos = target['pos']

    print(f"\n--- {name} ({chrom}:{pos:,}) ---")

    # Use 16KB context for speed
    sequence_interval = genome.Interval(chrom, pos, pos + 1).resize(
        dna_client.SEQUENCE_LENGTH_16KB
    )

    # ISM over 64bp centered on breakpoint
    ism_interval = genome.Interval(chrom, pos - 32, pos + 32)

    print(f"  Context: {sequence_interval}")
    print(f"  ISM window: {ism_interval}")
    print(f"  Scoring {ism_interval.width * 3} variants...")

    try:
        ism_scores = dna_model.score_ism_variants(
            interval=sequence_interval,
            ism_interval=ism_interval,
            variant_scorers=[ism_scorer],
        )

        # Aggregate ISM results - find which tissues show max sensitivity
        # Each entry in ism_scores is a list of AnnData (one per scorer)
        tissue_max_effects = {}

        for var_scores in ism_scores:
            adata = var_scores[0]
            vals = adata.X.flatten()  # shape (1, num_tracks) -> (num_tracks,)
            meta = adata.var

            for i, (_, row) in enumerate(meta.iterrows()):
                tissue = row.get('biosample_name', row.get('name', 'unknown'))
                score = abs(vals[i])
                key = (tissue, row.get('name', ''))
                if key not in tissue_max_effects or score > tissue_max_effects[key]['abs_score']:
                    tissue_max_effects[key] = {
                        'biosample_name': tissue,
                        'name': row.get('name', ''),
                        'max_ism_score': float(vals[i]),
                        'abs_score': score,
                        'variant': str(adata.uns.get('variant', '')),
                    }

        if tissue_max_effects:
            df = pd.DataFrame(tissue_max_effects.values())
            top = df.nlargest(10, 'abs_score')
            print(f"\n  Top 10 tissues by max ISM effect:")
            for _, r in top.iterrows():
                print(f"    {r['biosample_name']:50s} Score: {r['max_ism_score']:+.6f}  ({r['variant']})")
            all_results[f'approach3_{name}'] = df

        print(f"  Completed: {len(ism_scores)} variants scored")

    except Exception as e:
        print(f"  ERROR: {e}")
        import traceback
        traceback.print_exc()
        continue

# Save all results
output_path = '/Users/lbacaj/genomics/reproduction_results.pkl'
with open(output_path, 'wb') as f:
    pickle.dump(all_results, f)
print(f"\nAll results saved to {output_path}")

print("\n" + "=" * 70)
print("DONE")
print("=" * 70)
