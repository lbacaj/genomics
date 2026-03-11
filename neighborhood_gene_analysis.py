"""Wider Neighborhood Gene Effects Analysis.

For each breakpoint, identifies all genes within 500kb and characterizes:
1. Gene identity, distance from breakpoint, strand, and biotype
2. Whether the gene is in the same TAD as the breakpoint (from contact map data)
3. Predicted expression level across tissues (via AlphaGenome RNA_SEQ)
4. Functional annotation and pathway relevance

No new variant scoring — this is a neighborhood mapping exercise that
identifies collateral damage from the translocations.
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
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
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
print(f"Loaded {len(gtf)} annotation records.\n")

OUTPUT_DIR = '/Users/lbacaj/genomics/neighborhood_analysis'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Breakpoints
breakpoints = [
    {'name': 'ASPSCR1',     'chrom': 'chr17', 'pos': 82010811,
     'gene': 'ASPSCR1', 'label': 'ASPSCR1 (chr17:82,010,811)'},
    {'name': 'TFE3',        'chrom': 'chrX',  'pos': 49043986,
     'gene': 'TFE3', 'label': 'TFE3 (chrX:49,043,986)'},
    {'name': 'DNMT1_chr1',  'chrom': 'chr1',  'pos': 31048832,
     'gene': 'LAPTM5', 'label': 'DNMT1 partner (chr1:31,048,832)'},
    {'name': 'DNMT1_chr19', 'chrom': 'chr19', 'pos': 10160241,
     'gene': 'DNMT1', 'label': 'DNMT1 primary (chr19:10,160,241)'},
]

# TAD boundary positions from contact map analysis
# Extracted from contact_map_results.json
tad_boundaries = {
    'ASPSCR1': {
        'nearest_boundary_dist': 12000,  # ~12kb
        'boundary_genes': ['SLC16A3', 'ASPSCR1'],
    },
    'TFE3': {
        'nearest_boundary_dist': 0,  # at boundary
        'boundary_genes': ['TFE3', 'RLIM'],
    },
    'DNMT1_chr1': {
        'nearest_boundary_dist': 0,  # at boundary
        'boundary_genes': ['LAPTM5', 'SDC3'],
    },
    'DNMT1_chr19': {
        'nearest_boundary_dist': 0,  # at boundary
        'boundary_genes': ['DNMT1', 'ABHD8'],
    },
}

# Tissues for expression profiling
key_tissues = [
    'UBERON:0002048',   # Lung
    'UBERON:0002107',   # Liver
    'UBERON:0000955',   # Brain
    'UBERON:0001157',   # Transverse colon
    'UBERON:0002106',   # Spleen
]

WINDOW = 500000  # 500kb radius

# Known gene functions (curated for relevance)
gene_functions = {
    'ASPSCR1': 'Alveolar soft part sarcoma locus; UBX domain',
    'TFE3': 'Transcription factor E3; MiT/TFE family; lysosomal biogenesis master regulator',
    'DNMT1': 'DNA methyltransferase 1; maintenance methylation',
    'LAPTM5': 'Lysosomal protein transmembrane 5; T-cell/NK-cell cytotoxicity',
    'SLC16A3': 'MCT4; monocarboxylate transporter 4; lactate exporter',
    'SLC16A1': 'MCT1; monocarboxylate transporter 1; lactate importer',
    'FOXJ1': 'Forkhead box J1; ciliogenesis; immune regulation',
    'EFCAB13': 'EF-hand calcium binding domain 13',
    'SDC3': 'Syndecan-3; cell surface proteoglycan; neural development',
    'MATN1': 'Matrilin-1; cartilage matrix protein',
    'COL9A2': 'Collagen type IX alpha 2; cartilage component',
    'RLIM': 'Ring finger protein; X-linked; ubiquitin ligase',
    'ABCB7': 'ATP-binding cassette transporter; iron-sulfur cluster transport',
    'UPRT': 'Uracil phosphoribosyltransferase',
    'ZDHHC15': 'Zinc finger DHHC-type palmitoyl transferase 15',
    'ABHD8': 'Alpha/beta hydrolase domain 8',
    'ARHGEF18': 'Rho guanine nucleotide exchange factor 18',
    'MAP2K2': 'MEK2; MAPK pathway; cancer signaling',
    'CREB3L3': 'CREB/ATF family; hepatic lipid metabolism',
    'SIRT6': 'Sirtuin 6; chromatin regulation; DNA repair',
    'ANKLE1': 'Ankyrin repeat and LEM domain 1; DNA damage response',
    'GCDH': 'Glutaryl-CoA dehydrogenase; lysine metabolism',
}

all_neighborhood_data = {}

for bp in breakpoints:
    name = bp['name']
    chrom = bp['chrom']
    pos = bp['pos']
    label = bp['label']

    print("=" * 70)
    print(f"NEIGHBORHOOD: {label}")
    print("=" * 70)

    # Find all protein-coding genes within WINDOW of the breakpoint
    gene_records = gtf[
        (gtf['Chromosome'] == chrom) &
        (gtf['Feature'] == 'gene') &
        (gtf['Start'] < pos + WINDOW) &
        (gtf['End'] > pos - WINDOW)
    ].copy()

    # Extract gene attributes from proper columns
    genes_near = []
    for _, row in gene_records.iterrows():
        gene_name = row.get('gene_name', '') or ''
        gene_type = row.get('gene_type', '') or ''
        gene_id = row.get('gene_id', '') or ''

        start = int(row['Start'])
        end = int(row['End'])
        strand = row.get('Strand', '.')

        # Distance from breakpoint
        if start <= pos <= end:
            dist = 0  # breakpoint is inside the gene
            position = 'inside'
        elif pos < start:
            dist = start - pos
            position = 'downstream' if strand == '+' else 'upstream'
        else:
            dist = pos - end
            position = 'upstream' if strand == '+' else 'downstream'

        genes_near.append({
            'gene_name': gene_name,
            'gene_id': gene_id,
            'gene_type': gene_type,
            'chrom': chrom,
            'start': start,
            'end': end,
            'strand': strand,
            'length': end - start,
            'distance': dist,
            'position': position,
            'function': gene_functions.get(gene_name, ''),
        })

    genes_df = pd.DataFrame(genes_near)

    # Filter to protein-coding and well-annotated genes
    protein_coding = genes_df[genes_df['gene_type'] == 'protein_coding'].copy()
    protein_coding = protein_coding.sort_values('distance')

    print(f"\n  Total genes within {WINDOW//1000}kb: {len(genes_df)}")
    print(f"  Protein-coding: {len(protein_coding)}")

    # Show nearest genes
    print(f"\n  Nearest protein-coding genes:")
    for _, g in protein_coding.head(20).iterrows():
        dist_str = f"{g['distance']:,}bp" if g['distance'] > 0 else "AT BREAKPOINT"
        func = f" — {g['function']}" if g['function'] else ''
        print(f"    {g['gene_name']:15s} {g['strand']:2s}  "
              f"{g['chrom']}:{g['start']:,}-{g['end']:,}  "
              f"dist={dist_str} ({g['position']}){func}")

    # Get expression for the nearest 15 protein-coding genes
    print(f"\n  Profiling expression for nearest genes...")
    expression_data = []
    genes_to_profile = protein_coding.head(15)

    for _, gene_row in genes_to_profile.iterrows():
        gene_symbol = gene_row['gene_name']
        if not gene_symbol:
            continue

        try:
            gene_interval = gene_annotation.get_gene_interval(
                gtf, gene_symbol=gene_symbol
            )
            interval = gene_interval.resize(dna_client.SEQUENCE_LENGTH_1MB)

            output = dna_model.predict_interval(
                interval=interval,
                requested_outputs=[dna_client.OutputType.RNA_SEQ],
                ontology_terms=key_tissues,
            )

            rna = output.rna_seq
            values = rna.values
            metadata = rna.metadata

            gene_start_offset = max(0, gene_interval.start - interval.start)
            gene_end_offset = min(values.shape[0], gene_interval.end - interval.start)
            gene_vals = values[gene_start_offset:gene_end_offset, :]

            # Per-tissue expression on matching strand
            tissue_expr = {}
            for i, (_, mrow) in enumerate(metadata.iterrows()):
                track_strand = mrow.get('strand', '.')
                tissue = mrow.get('biosample_name', '')
                if track_strand == gene_interval.strand or track_strand == '.':
                    key = tissue
                    if key not in tissue_expr or gene_vals[:, i].mean() > tissue_expr[key]:
                        tissue_expr[key] = float(gene_vals[:, i].mean())

            overall_mean = float(np.mean(list(tissue_expr.values()))) if tissue_expr else 0
            top_tissue = max(tissue_expr, key=tissue_expr.get) if tissue_expr else 'N/A'
            top_expr = tissue_expr.get(top_tissue, 0)

            expression_data.append({
                'gene': gene_symbol,
                'distance': int(gene_row['distance']),
                'strand': gene_row['strand'],
                'overall_mean': overall_mean,
                'top_tissue': top_tissue,
                'top_tissue_expr': top_expr,
                'tissue_expr': tissue_expr,
            })

            print(f"    {gene_symbol:15s} dist={gene_row['distance']:>8,}  "
                  f"mean={overall_mean:.4f}  top={top_tissue} ({top_expr:.4f})")

        except Exception as e:
            print(f"    {gene_symbol:15s} ERROR: {e}")
            expression_data.append({
                'gene': gene_symbol,
                'distance': int(gene_row['distance']),
                'strand': gene_row['strand'],
                'overall_mean': 0,
                'top_tissue': 'ERROR',
                'top_tissue_expr': 0,
                'tissue_expr': {},
            })

    all_neighborhood_data[name] = {
        'all_genes': genes_near,
        'protein_coding_genes': protein_coding.to_dict(orient='records'),
        'expression_profiles': expression_data,
        'tad_info': tad_boundaries.get(name, {}),
    }

    # Visualization: neighborhood map
    fig, ax = plt.subplots(figsize=(20, max(4, len(protein_coding.head(20)) * 0.4 + 2)))

    display_genes = protein_coding.head(20)
    y_positions = range(len(display_genes))

    for i, (_, g) in enumerate(display_genes.iterrows()):
        # Color by distance
        if g['distance'] == 0:
            color = '#e74c3c'  # red = at breakpoint
        elif g['distance'] < 50000:
            color = '#e67e22'  # orange = very near
        elif g['distance'] < 200000:
            color = '#f1c40f'  # yellow = near
        else:
            color = '#2ecc71'  # green = distant

        # Find expression data
        expr_val = 0
        for ed in expression_data:
            if ed['gene'] == g['gene_name']:
                expr_val = ed['overall_mean']
                break

        bar_width = max(0.01, expr_val)
        ax.barh(i, bar_width, color=color, alpha=0.8, height=0.7)

        dist_str = f"{g['distance']:,}bp" if g['distance'] > 0 else "AT BP"
        label = f"{g['gene_name']} ({g['strand']}) — {dist_str}"
        if g['function']:
            label += f" | {g['function'][:40]}"
        ax.text(bar_width + 0.01, i, label, va='center', fontsize=8)

    ax.set_yticks(y_positions)
    ax.set_yticklabels([g['gene_name'] for _, g in display_genes.iterrows()], fontsize=9)
    ax.set_xlabel('Mean RNA-seq Expression', fontsize=11)
    ax.set_title(f'Gene Neighborhood: {label}\n'
                 f'Nearest 20 protein-coding genes | Color = distance from breakpoint',
                 fontsize=13, fontweight='bold')
    ax.invert_yaxis()

    legend_elements = [
        mpatches.Patch(color='#e74c3c', label='At breakpoint (0bp)'),
        mpatches.Patch(color='#e67e22', label='<50kb'),
        mpatches.Patch(color='#f1c40f', label='50-200kb'),
        mpatches.Patch(color='#2ecc71', label='>200kb'),
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=8)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/{name}_neighborhood.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close('all')
    print(f"  Saved: {OUTPUT_DIR}/{name}_neighborhood.png")
    print()

# Save all data
output_path = f'{OUTPUT_DIR}/neighborhood_results.json'
with open(output_path, 'w') as f:
    json.dump(all_neighborhood_data, f, indent=2, default=str)
print(f"\nResults saved to {output_path}")

# Summary across breakpoints
print("\n" + "=" * 70)
print("NEIGHBORHOOD GENE ANALYSIS SUMMARY")
print("=" * 70)

for bp in breakpoints:
    name = bp['name']
    if name in all_neighborhood_data:
        data = all_neighborhood_data[name]
        pc = data['protein_coding_genes']
        expr = data['expression_profiles']

        print(f"\n  {bp['label']}:")
        print(f"    Total nearby genes: {len(data['all_genes'])}")
        print(f"    Protein-coding: {len(pc)}")

        # Most expressed neighbors
        if expr:
            expr_sorted = sorted(expr, key=lambda x: x['overall_mean'], reverse=True)
            print(f"    Top expressed neighbors:")
            for e in expr_sorted[:5]:
                print(f"      {e['gene']:15s} mean={e['overall_mean']:.4f}  "
                      f"dist={e['distance']:,}  top={e['top_tissue']}")

print(f"\nAll images saved to {OUTPUT_DIR}/")
print("Done.")
