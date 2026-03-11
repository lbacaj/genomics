"""Reproduce Johnny's ASPS genomic analysis using AlphaGenome."""

import os
import sys

# Remove cwd from path to avoid local alphagenome/ dir shadowing the package
sys.path = [p for p in sys.path if p not in ('', '.', os.getcwd())]

# Load API key
with open('/Users/lbacaj/genomics/.env') as f:
    for line in f:
        if '=' in line:
            k, v = line.strip().split('=', 1)
            os.environ[k] = v

from alphagenome.models import dna_client
from alphagenome.models import variant_scorers
from alphagenome.data import genome
import pandas as pd

print("Connecting to AlphaGenome API...")
dna_model = dna_client.create(os.environ['ALPHA_GENOME_API_KEY'])
print("Connected.\n")

# Breakpoint coordinates in hg38 (from johnny-details.md)
targets = [
    {'name': 'ASPSCR1',    'chrom': 'chr17', 'pos': 82010811},
    {'name': 'TFE3',       'chrom': 'chrX',  'pos': 49043986},
    {'name': 'DNMT1_chr1', 'chrom': 'chr1',  'pos': 31048832},
    {'name': 'DNMT1_chr19','chrom': 'chr19', 'pos': 10160241},
]

variant_scorer = variant_scorers.RECOMMENDED_VARIANT_SCORERS['RNA_SEQ']
print(f"Variant scorer: {variant_scorer}\n")

all_results = {}

for target in targets:
    name = target['name']
    chrom = target['chrom']
    pos = target['pos']

    print("=" * 60)
    print(f"ANALYSIS OF TARGET: {name}")
    print(f"Location: {chrom}:{pos:,}")
    print("=" * 60)

    # Create 1MB interval centered on breakpoint
    interval = genome.Interval(chrom, pos, pos + 1).resize(dna_client.SEQUENCE_LENGTH_1MB)
    print(f"Interval: {interval}")

    # Define a variant at the breakpoint position.
    # For translocation breakpoint analysis, we score a substitution
    # to measure the regulatory sensitivity at this locus.
    # reference_bases can differ from actual ref genome base per the API docs.
    variant = genome.Variant(
        chromosome=chrom,
        position=pos,
        reference_bases='A',
        alternate_bases='G',
    )

    print(f"Scoring variant {variant}...")
    try:
        scores = dna_model.score_variant(
            interval=interval,
            variant=variant,
            variant_scorers=[variant_scorer],
        )

        # Tidy the scores
        tidy = variant_scorers.tidy_scores(scores, match_gene_strand=True)

        # Sort by absolute raw score to find highest impact tissues
        tidy['abs_score'] = tidy['raw_score'].abs()
        top = tidy.nlargest(10, 'abs_score')

        print(f"\nTop 10 tissues by impact:")
        display_cols = ['biosample_name', 'name', 'raw_score', 'quantile_score']
        available = [c for c in display_cols if c in top.columns]
        print(top[available].to_string(index=False))
        print()

        all_results[name] = tidy

    except Exception as e:
        print(f"ERROR: {e}\n")
        continue

# Summary
print("\n" + "=" * 60)
print("SUMMARY: Top impact per target")
print("=" * 60)
for name, tidy in all_results.items():
    tidy['abs_score'] = tidy['raw_score'].abs()
    top_row = tidy.nlargest(1, 'abs_score').iloc[0]
    print(f"  {name}: {top_row.get('biosample_name', 'N/A')} "
          f"(Score: {top_row['raw_score']:.4f})")
