"""Extension 2: Drug target accessibility analysis.

For each drug in the current Triple Blockade, score the relevant
target genes to understand how the tumor's breakpoints affect
expression of the genes these drugs act on.

Drugs and their molecular targets:
- Doxycycline: MMP genes (MMP2, MMP9, MMP14), mitochondrial ribosomes (MRPS, MRPL genes)
- Hydroxychloroquine: Autophagy/lysosomal genes (ATG5, ATG7, LAMP1, LAMP2, CTSD, SQSTM1/p62)
- Cimetidine: Histamine receptors (HRH1, HRH2, HRH4), angiogenesis (VEGFA, VEGFB, KDR/VEGFR2)

Also score key immune checkpoint and signaling genes relevant to
the identified immune targets.
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
import pandas as pd
import numpy as np
import json

print("Connecting to AlphaGenome API...")
dna_model = dna_client.create(os.environ['ALPHA_GENOME_API_KEY'])
print("Connected.\n")

# Load GTF for gene locations
print("Loading gene annotations...")
gtf = pd.read_feather(
    'https://storage.googleapis.com/alphagenome/reference/gencode/'
    'hg38/gencode.v46.annotation.gtf.gz.feather'
)
print(f"Loaded {len(gtf)} annotation records.\n")

# Drug target genes organized by therapeutic mechanism
drug_targets = {
    'DOXYCYCLINE_MMP': [
        'MMP2', 'MMP9', 'MMP14', 'MMP7', 'MMP1', 'MMP3',
    ],
    'DOXYCYCLINE_MITO': [
        'MRPS12', 'MRPS15', 'MRPL11', 'MRPL13', 'MT-CO1', 'MT-ND1',
    ],
    'HCQ_AUTOPHAGY': [
        'ATG5', 'ATG7', 'ATG12', 'BECN1', 'SQSTM1', 'MAP1LC3B',
    ],
    'HCQ_LYSOSOME': [
        'LAMP1', 'LAMP2', 'CTSD', 'CTSL', 'TFEB', 'ATP6V1A',
    ],
    'CIMETIDINE_HISTAMINE': [
        'HRH1', 'HRH2', 'HRH4', 'HDC',
    ],
    'CIMETIDINE_ANGIOGENESIS': [
        'VEGFA', 'VEGFB', 'VEGFC', 'KDR', 'FLT1', 'ANGPT2',
    ],
    'IMMUNE_CHECKPOINT': [
        'PDCD1', 'CD274', 'CTLA4', 'LAG3', 'HAVCR2', 'TIGIT',
    ],
    'IMMUNE_ACTIVATION': [
        'IFNG', 'TNF', 'IL2', 'PRF1', 'GZMB', 'CD8A', 'CD4',
    ],
    'TFE3_PATHWAY': [
        'TFE3', 'TFEB', 'MITF', 'FLCN', 'FNIP1', 'MTOR', 'RPTOR',
    ],
    'DNMT1_PATHWAY': [
        'DNMT1', 'DNMT3A', 'DNMT3B', 'TET1', 'TET2', 'IDH1', 'IDH2',
    ],
}

# Breakpoints
breakpoints = [
    {'name': 'ASPSCR1',     'chrom': 'chr17', 'pos': 82010811},
    {'name': 'TFE3',        'chrom': 'chrX',  'pos': 49043986},
    {'name': 'DNMT1_chr1',  'chrom': 'chr1',  'pos': 31048832},
    {'name': 'DNMT1_chr19', 'chrom': 'chr19', 'pos': 10160241},
]

# For each drug target gene, predict its expression across tissues
# using predict_interval centered on the gene
gene_scorer = variant_scorers.RECOMMENDED_VARIANT_SCORERS['RNA_SEQ']

# Confirmed-working UBERON terms for predict_interval RNA_SEQ
key_tissues = [
    'UBERON:0002048',   # Lung
    'UBERON:0002107',   # Liver
    'UBERON:0000948',   # Heart
    'UBERON:0000955',   # Brain
    'UBERON:0001157',   # Transverse colon
]

all_results = {}

for category, genes in drug_targets.items():
    print("=" * 70)
    print(f"CATEGORY: {category}")
    print("=" * 70)

    for gene_symbol in genes:
        try:
            gene_interval = gene_annotation.get_gene_interval(
                gtf, gene_symbol=gene_symbol
            )
        except Exception as e:
            print(f"  {gene_symbol}: Gene not found in GTF - {e}")
            continue

        interval = gene_interval.resize(dna_client.SEQUENCE_LENGTH_1MB)

        print(f"\n  {gene_symbol} ({gene_interval.chromosome}:"
              f"{gene_interval.start:,}-{gene_interval.end:,}, "
              f"strand={gene_interval.strand})")

        try:
            output = dna_model.predict_interval(
                interval=interval,
                requested_outputs=[dna_client.OutputType.RNA_SEQ],
                ontology_terms=key_tissues,
            )

            rna = output.rna_seq
            values = rna.values
            metadata = rna.metadata

            # Get expression within the gene body
            gene_start_offset = gene_interval.start - interval.start
            gene_end_offset = gene_interval.end - interval.start
            gene_start_offset = max(0, gene_start_offset)
            gene_end_offset = min(values.shape[0], gene_end_offset)

            gene_vals = values[gene_start_offset:gene_end_offset, :]

            track_stats = []
            for i, (_, row) in enumerate(metadata.iterrows()):
                col_vals = gene_vals[:, i]
                strand = row.get('strand', '.')
                # For stranded data, only count matching strand
                track_stats.append({
                    'category': category,
                    'gene': gene_symbol,
                    'gene_strand': gene_interval.strand,
                    'track_name': row.get('name', ''),
                    'track_strand': strand,
                    'biosample_name': row.get('biosample_name', ''),
                    'gene_body_mean': float(np.mean(col_vals)),
                    'gene_body_max': float(np.max(col_vals)),
                })

            df = pd.DataFrame(track_stats)

            # Filter to matching strand if stranded
            if gene_interval.strand in ('+', '-'):
                strand_match = df[
                    (df['track_strand'] == gene_interval.strand) |
                    (df['track_strand'] == '.')
                ]
                if len(strand_match) > 0:
                    df = strand_match

            df = df.sort_values('gene_body_mean', ascending=False)
            top = df.head(5)

            print(f"    Top 5 expressing tissues (predicted):")
            for _, r in top.iterrows():
                print(f"      {r['biosample_name']:45s} mean={r['gene_body_mean']:.4f}  "
                      f"max={r['gene_body_max']:.4f}")

            all_results[f'{category}_{gene_symbol}'] = df

        except Exception as e:
            print(f"    ERROR: {e}")
            continue

# Save
output_path = '/Users/lbacaj/genomics/drug_target_results.json'
serializable = {}
for key, df in all_results.items():
    serializable[key] = df.to_dict(orient='records')
with open(output_path, 'w') as f:
    json.dump(serializable, f, indent=2)
print(f"\nResults saved to {output_path}")

# Summary by drug
print("\n" + "=" * 70)
print("DRUG TARGET EXPRESSION SUMMARY")
print("=" * 70)

for category, genes in drug_targets.items():
    print(f"\n{category}:")
    for gene in genes:
        key = f'{category}_{gene}'
        if key in all_results:
            df = all_results[key]
            top = df.nlargest(1, 'gene_body_mean').iloc[0]
            bottom = df.nsmallest(1, 'gene_body_mean').iloc[0]
            print(f"  {gene:12s} Highest: {top['biosample_name']:35s} ({top['gene_body_mean']:.4f})  "
                  f"Lowest: {bottom['biosample_name']:35s} ({bottom['gene_body_mean']:.4f})")
