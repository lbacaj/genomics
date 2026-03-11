"""OXPHOS / Metabolic Gene Panel Analysis.

Extends the drug target analysis to profile the full metabolic machinery
relevant to the Reverse Warburg hypothesis and mitochondrial addiction
finding (vulnerability score 13.6).

Gene panels:
- OXPHOS Complex I-V
- TCA Cycle enzymes
- Lactate Transport (MCT1/MCT4 — the Reverse Warburg fuel line)
- Glucose Transport (GLUT1/GLUT4)
- Fatty Acid Oxidation
- Mitochondrial Dynamics (fission/fusion)

SLC16A3/MCT4 appearing at a TAD boundary near ASPSCR1 (contact map analysis)
makes the lactate transport genes especially important.
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

OUTPUT_DIR = '/Users/lbacaj/genomics/metabolic_analysis'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Metabolic gene panels
metabolic_panels = {
    'OXPHOS_COMPLEX_I': [
        'NDUFB8', 'NDUFS1', 'NDUFS2', 'NDUFV1', 'NDUFA9',
    ],
    'OXPHOS_COMPLEX_II': [
        'SDHB', 'SDHA', 'SDHC', 'SDHD',
    ],
    'OXPHOS_COMPLEX_III': [
        'UQCRC2', 'UQCRC1', 'UQCRFS1',
    ],
    'OXPHOS_COMPLEX_IV': [
        'COX4I1', 'COX5A', 'COX6B1', 'COX7A2',
    ],
    'OXPHOS_COMPLEX_V': [
        'ATP5F1A', 'ATP5F1B', 'ATP5MC1', 'ATP5PO',
    ],
    'TCA_CYCLE': [
        'CS', 'ACO2', 'IDH2', 'OGDH', 'SUCLA2', 'FH', 'MDH2', 'DLST',
    ],
    'LACTATE_TRANSPORT': [
        'SLC16A1',  # MCT1 — lactate importer (tumor side)
        'SLC16A3',  # MCT4 — lactate exporter (fibroblast side, at TAD boundary)
        'SLC16A7',  # MCT2
        'LDHA',     # Lactate dehydrogenase A (pyruvate -> lactate)
        'LDHB',     # Lactate dehydrogenase B (lactate -> pyruvate)
    ],
    'GLUCOSE_TRANSPORT': [
        'SLC2A1',   # GLUT1
        'SLC2A4',   # GLUT4
        'SLC2A3',   # GLUT3
        'HK2',      # Hexokinase 2 (first glycolysis step)
        'PKM',      # Pyruvate kinase (last glycolysis step)
    ],
    'FATTY_ACID_OXIDATION': [
        'CPT1A', 'CPT2', 'ACADM', 'HADHA', 'ACAD9',
    ],
    'MITO_DYNAMICS': [
        'MFN1',     # Mitofusin 1 (fusion)
        'MFN2',     # Mitofusin 2 (fusion)
        'OPA1',     # Optic atrophy 1 (inner membrane fusion)
        'DRP1',     # Dynamin-related protein 1 (fission) — gene symbol DNM1L
        'FIS1',     # Fission 1
    ],
}

# Map common names to actual gene symbols where needed
gene_symbol_map = {
    'DRP1': 'DNM1L',
}

# Tissues
key_tissues = [
    'UBERON:0002048',   # Lung
    'UBERON:0002107',   # Liver
    'UBERON:0000948',   # Heart
    'UBERON:0000955',   # Brain
    'UBERON:0001157',   # Transverse colon
    'UBERON:0002106',   # Spleen
]

all_results = {}
gene_expression_summary = []

for panel_name, genes in metabolic_panels.items():
    print("=" * 70)
    print(f"PANEL: {panel_name}")
    print("=" * 70)

    for gene_symbol in genes:
        # Map to actual symbol if needed
        actual_symbol = gene_symbol_map.get(gene_symbol, gene_symbol)

        try:
            gene_interval = gene_annotation.get_gene_interval(
                gtf, gene_symbol=actual_symbol
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
                track_stats.append({
                    'panel': panel_name,
                    'gene': gene_symbol,
                    'actual_symbol': actual_symbol,
                    'gene_strand': gene_interval.strand,
                    'gene_chr': gene_interval.chromosome,
                    'gene_start': gene_interval.start,
                    'gene_end': gene_interval.end,
                    'track_name': row.get('name', ''),
                    'track_strand': strand,
                    'biosample_name': row.get('biosample_name', ''),
                    'gene_body_mean': float(np.mean(col_vals)),
                    'gene_body_max': float(np.max(col_vals)),
                    'gene_body_median': float(np.median(col_vals)),
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
                print(f"      {r['biosample_name']:40s} mean={r['gene_body_mean']:.4f}  "
                      f"max={r['gene_body_max']:.4f}")

            # Store for summary
            overall_mean = float(df['gene_body_mean'].mean())
            overall_max = float(df['gene_body_max'].max())
            top_tissue = df.iloc[0]['biosample_name'] if len(df) > 0 else 'N/A'
            top_mean = float(df.iloc[0]['gene_body_mean']) if len(df) > 0 else 0

            gene_expression_summary.append({
                'panel': panel_name,
                'gene': gene_symbol,
                'actual_symbol': actual_symbol,
                'chr': gene_interval.chromosome,
                'strand': gene_interval.strand,
                'overall_mean': overall_mean,
                'overall_max': overall_max,
                'top_tissue': top_tissue,
                'top_tissue_mean': top_mean,
            })

            all_results[f'{panel_name}_{gene_symbol}'] = df.to_dict(orient='records')

        except Exception as e:
            print(f"    ERROR: {e}")
            continue

    print()

# Save all results
output_path = f'{OUTPUT_DIR}/metabolic_results.json'
with open(output_path, 'w') as f:
    json.dump(all_results, f, indent=2, default=str)
print(f"\nResults saved to {output_path}")

# Save summary
summary_df = pd.DataFrame(gene_expression_summary)
summary_path = f'{OUTPUT_DIR}/metabolic_summary.csv'
summary_df.to_csv(summary_path, index=False)
print(f"Summary saved to {summary_path}")

# =============================================
# Generate visualizations
# =============================================
print("\nGenerating visualizations...")

# 1. Panel-level heatmap: mean expression by gene x tissue
for panel_name, genes in metabolic_panels.items():
    panel_data = []
    for gene_symbol in genes:
        actual_symbol = gene_symbol_map.get(gene_symbol, gene_symbol)
        key = f'{panel_name}_{gene_symbol}'
        if key in all_results:
            records = all_results[key]
            for r in records:
                panel_data.append(r)

    if not panel_data:
        continue

    pdf = pd.DataFrame(panel_data)

    # Pivot: gene x tissue, values = gene_body_mean
    pivot = pdf.pivot_table(
        index='gene', columns='biosample_name',
        values='gene_body_mean', aggfunc='mean'
    )

    if pivot.empty:
        continue

    fig, ax = plt.subplots(figsize=(12, max(3, len(pivot) * 0.6 + 1)))
    im = ax.imshow(pivot.values, aspect='auto', cmap='YlOrRd')
    ax.set_yticks(range(len(pivot.index)))
    ax.set_yticklabels(pivot.index, fontsize=10)
    ax.set_xticks(range(len(pivot.columns)))
    ax.set_xticklabels(pivot.columns, fontsize=9, rotation=45, ha='right')

    # Annotate cells
    for i in range(len(pivot.index)):
        for j in range(len(pivot.columns)):
            val = pivot.values[i, j]
            color = 'white' if val > pivot.values.max() * 0.6 else 'black'
            ax.text(j, i, f'{val:.3f}', ha='center', va='center',
                    fontsize=8, color=color)

    plt.colorbar(im, ax=ax, label='Mean RNA-seq (gene body)')
    ax.set_title(f'{panel_name}\nPredicted Gene Expression by Tissue',
                 fontsize=13, fontweight='bold')
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/{panel_name}_heatmap.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close('all')
    print(f"  Saved: {OUTPUT_DIR}/{panel_name}_heatmap.png")

# 2. Reverse Warburg comparison: MCT1 vs MCT4 vs LDHA vs LDHB
warburg_genes = ['SLC16A1', 'SLC16A3', 'LDHA', 'LDHB']
warburg_labels = ['MCT1\n(tumor importer)', 'MCT4\n(fibroblast exporter)',
                  'LDHA\n(pyruvate→lactate)', 'LDHB\n(lactate→pyruvate)']
warburg_data = []
for gene in warburg_genes:
    key = f'LACTATE_TRANSPORT_{gene}'
    if key in all_results:
        records = all_results[key]
        for r in records:
            warburg_data.append(r)

if warburg_data:
    wdf = pd.DataFrame(warburg_data)
    tissues = sorted(wdf['biosample_name'].unique())

    fig, axes = plt.subplots(1, len(warburg_genes),
                             figsize=(5 * len(warburg_genes), 6),
                             sharey=True)

    for i, (gene, label) in enumerate(zip(warburg_genes, warburg_labels)):
        ax = axes[i]
        gdf = wdf[wdf['gene'] == gene].sort_values('gene_body_mean', ascending=True)
        colors = ['#e74c3c' if 'lung' in t.lower() or 'spleen' in t.lower()
                  else '#3498db' for t in gdf['biosample_name']]
        ax.barh(range(len(gdf)), gdf['gene_body_mean'], color=colors, alpha=0.8)
        ax.set_yticks(range(len(gdf)))
        ax.set_yticklabels(gdf['biosample_name'], fontsize=9)
        ax.set_xlabel('Mean RNA-seq', fontsize=10)
        ax.set_title(f'{gene}\n{label}', fontsize=11, fontweight='bold')

    plt.suptitle('Reverse Warburg Lactate Pathway\nPredicted Expression by Tissue',
                 fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/reverse_warburg_comparison.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close('all')
    print(f"  Saved: {OUTPUT_DIR}/reverse_warburg_comparison.png")

# 3. Overall metabolic heatmap — all genes grouped by panel
if gene_expression_summary:
    sdf = pd.DataFrame(gene_expression_summary)
    sdf = sdf.sort_values(['panel', 'overall_mean'], ascending=[True, False])

    fig, ax = plt.subplots(figsize=(10, max(6, len(sdf) * 0.35)))
    colors = []
    panel_colors = {
        'OXPHOS_COMPLEX_I': '#e74c3c',
        'OXPHOS_COMPLEX_II': '#e67e22',
        'OXPHOS_COMPLEX_III': '#f1c40f',
        'OXPHOS_COMPLEX_IV': '#2ecc71',
        'OXPHOS_COMPLEX_V': '#1abc9c',
        'TCA_CYCLE': '#3498db',
        'LACTATE_TRANSPORT': '#9b59b6',
        'GLUCOSE_TRANSPORT': '#e91e63',
        'FATTY_ACID_OXIDATION': '#795548',
        'MITO_DYNAMICS': '#607d8b',
    }

    for _, row in sdf.iterrows():
        colors.append(panel_colors.get(row['panel'], '#95a5a6'))

    ax.barh(range(len(sdf)), sdf['overall_mean'], color=colors, alpha=0.8)
    ax.set_yticks(range(len(sdf)))
    ax.set_yticklabels([f"{r['gene']} ({r['panel'].split('_', 1)[-1][:15]})"
                        for _, r in sdf.iterrows()], fontsize=8)
    ax.set_xlabel('Mean RNA-seq across all tissues', fontsize=11)
    ax.set_title('Metabolic Gene Panel — Overall Expression',
                 fontsize=13, fontweight='bold')

    # Add panel legend
    from matplotlib.patches import Patch
    legend_elements = [Patch(facecolor=c, label=p.replace('_', ' '))
                       for p, c in panel_colors.items() if p in sdf['panel'].values]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=7,
              title='Panel', title_fontsize=8)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/metabolic_overview.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close('all')
    print(f"  Saved: {OUTPUT_DIR}/metabolic_overview.png")

# Print final summary
print("\n" + "=" * 70)
print("METABOLIC GENE PANEL SUMMARY")
print("=" * 70)

for panel_name in metabolic_panels:
    panel_genes = [s for s in gene_expression_summary if s['panel'] == panel_name]
    if panel_genes:
        panel_genes_sorted = sorted(panel_genes, key=lambda x: x['overall_mean'], reverse=True)
        print(f"\n  {panel_name}:")
        for g in panel_genes_sorted:
            print(f"    {g['gene']:12s} overall_mean={g['overall_mean']:.4f}  "
                  f"max={g['overall_max']:.4f}  top_tissue={g['top_tissue']}")

print(f"\nAll images saved to {OUTPUT_DIR}/")
print("Done.")
