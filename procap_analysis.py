"""PROCAP Deep Dive Analysis.

PROCAP (Precision Run-On sequencing) measures transcription initiation
at single-nucleotide resolution — it shows exactly where RNA polymerase
begins transcribing.

At each breakpoint, PROCAP pinpoints the exact transcription start sites.
We compare PROCAP to CAGE data for cross-validation and look for:
1. Cryptic promoters activated near breakpoints
2. Transcription initiation shifts compared to normal
3. Whether the fusion is driven solely by the ASPSCR1 promoter
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

OUTPUT_DIR = '/Users/lbacaj/genomics/procap_analysis'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Breakpoints
breakpoints = [
    {'name': 'ASPSCR1',     'chrom': 'chr17', 'pos': 82010811,
     'gene': 'ASPSCR1', 'strand': '+',
     'label': 'ASPSCR1 (chr17:82,010,811)'},
    {'name': 'TFE3',        'chrom': 'chrX',  'pos': 49043986,
     'gene': 'TFE3', 'strand': '-',
     'label': 'TFE3 (chrX:49,043,986)'},
    {'name': 'DNMT1_chr1',  'chrom': 'chr1',  'pos': 31048832,
     'gene': 'PUM1', 'strand': '-',
     'label': 'DNMT1 partner (chr1:31,048,832)'},
    {'name': 'DNMT1_chr19', 'chrom': 'chr19', 'pos': 10160241,
     'gene': 'DNMT1', 'strand': '-',
     'label': 'DNMT1 primary (chr19:10,160,241)'},
]

# PROCAP data is only available for K562 cell line
procap_terms = ['EFO:0002067']  # K562

# Tissues for CAGE comparison
cage_terms = [
    'UBERON:0002048',  # Lung
    'UBERON:0000955',  # Brain
    'UBERON:0002107',  # Liver
    'UBERON:0001157',  # Transverse colon
    'UBERON:0002106',  # Spleen
]

all_results = {}

for bp in breakpoints:
    name = bp['name']
    chrom = bp['chrom']
    pos = bp['pos']
    label = bp['label']
    gene_strand = bp['strand']

    print("=" * 70)
    print(f"PROCAP ANALYSIS: {label}")
    print("=" * 70)

    # Use 100KB context for focused analysis
    interval = genome.Interval(chrom, pos, pos + 1).resize(
        dna_client.SEQUENCE_LENGTH_100KB
    )

    bp_results = {}

    # =============================================
    # 1. PROCAP predictions
    # =============================================
    print("\n  1. PROCAP predictions...")
    try:
        output_procap = dna_model.predict_interval(
            interval=interval,
            requested_outputs=[dna_client.OutputType.PROCAP],
            ontology_terms=procap_terms,
        )

        procap = output_procap.procap
        vals_p = procap.values
        meta_p = procap.metadata

        print(f"     Shape: {vals_p.shape}")
        print(f"     Tracks: {len(meta_p)}")

        for _, row in meta_p.iterrows():
            print(f"       {row.get('name', '')} | "
                  f"{row.get('biosample_name', '')} | "
                  f"strand={row.get('strand', '.')}")

        center = vals_p.shape[0] // 2

        # Analyze PROCAP signal at multiple windows
        for w_name, w in [('2kb', 1000), ('5kb', 2500), ('10kb', 5000)]:
            print(f"\n     PROCAP within {w_name} of breakpoint:")

            w_vals = vals_p[center - w:center + w, :]

            for i, (_, row) in enumerate(meta_p.iterrows()):
                col = w_vals[:, i]
                tissue = row.get('biosample_name', '')
                strand = row.get('strand', '.')

                max_val = float(np.max(col))
                mean_val = float(np.mean(col))
                sum_val = float(np.sum(col))

                # Find peaks (local maxima above threshold)
                threshold = max_val * 0.3 if max_val > 0.01 else 0.01
                peaks = []
                for j in range(1, len(col) - 1):
                    if col[j] > threshold and col[j] > col[j-1] and col[j] > col[j+1]:
                        gpos = interval.start + center - w + j
                        dist = gpos - pos
                        peaks.append((gpos, dist, float(col[j])))

                if max_val > 0.001 or w_name == '10kb':
                    print(f"       {tissue:30s} ({strand}): "
                          f"max={max_val:.4f}, mean={mean_val:.6f}, "
                          f"sum={sum_val:.2f}, peaks={len(peaks)}")

                    # Show top peaks
                    if peaks and w_name == '5kb':
                        peaks.sort(key=lambda x: x[2], reverse=True)
                        for gpos, dist, score in peaks[:3]:
                            print(f"         peak at {chrom}:{gpos:,} "
                                  f"(bp{dist:+,}): score={score:.4f}")

        bp_results['procap'] = {
            'shape': list(vals_p.shape),
            'n_tracks': len(meta_p),
            'track_names': [row.get('name', '') for _, row in meta_p.iterrows()],
        }

    except Exception as e:
        print(f"     PROCAP ERROR: {e}")
        import traceback
        traceback.print_exc()
        bp_results['procap'] = {'error': str(e)}

    # =============================================
    # 2. CAGE predictions (for comparison)
    # =============================================
    print("\n  2. CAGE predictions (comparison)...")
    try:
        output_cage = dna_model.predict_interval(
            interval=interval,
            requested_outputs=[dna_client.OutputType.CAGE],
            ontology_terms=cage_terms,
        )

        cage = output_cage.cage
        vals_c = cage.values
        meta_c = cage.metadata

        print(f"     Shape: {vals_c.shape}")
        print(f"     Tracks: {len(meta_c)}")

        center_c = vals_c.shape[0] // 2

        # Compare CAGE and PROCAP in 5kb window
        print(f"\n     CAGE within 5kb of breakpoint:")
        w = 2500

        for i, (_, row) in enumerate(meta_c.iterrows()):
            col = vals_c[center_c - w:center_c + w, i]
            tissue = row.get('biosample_name', '')
            strand = row.get('strand', '.')
            max_val = float(np.max(col))
            mean_val = float(np.mean(col))

            if max_val > 0.01:
                print(f"       {tissue:30s} ({strand}): "
                      f"max={max_val:.4f}, mean={mean_val:.6f}")

        bp_results['cage'] = {
            'shape': list(vals_c.shape),
            'n_tracks': len(meta_c),
        }

    except Exception as e:
        print(f"     CAGE ERROR: {e}")
        bp_results['cage'] = {'error': str(e)}

    # =============================================
    # 3. Visualization: PROCAP vs CAGE comparison
    # =============================================
    print("\n  3. Generating comparison visualization...")

    try:
        # Count PROCAP and CAGE tracks
        n_procap = vals_p.shape[1]
        n_cage = vals_c.shape[1]
        n_total = n_procap + n_cage

        zoom = 5000  # 10kb window

        fig, axes = plt.subplots(n_total, 1,
                                 figsize=(20, 1.8 * n_total),
                                 sharex=True)

        x = np.arange(center - zoom, center + zoom)

        # Plot PROCAP tracks
        for i in range(n_procap):
            ax = axes[i]
            y = vals_p[center - zoom:center + zoom, i]
            ax.plot(x, y, color='darkblue', linewidth=0.5)
            ax.fill_between(x, y, alpha=0.3, color='blue')
            ax.axvline(center, color='red', linewidth=2,
                       linestyle='--', alpha=0.8)
            tissue = meta_p.iloc[i].get('biosample_name', '')
            strand = meta_p.iloc[i].get('strand', '.')
            ax.set_ylabel(f'PROCAP\n{tissue}\n({strand})', fontsize=7)
            ax.set_ylim(bottom=0)

        # Plot CAGE tracks
        for i in range(n_cage):
            ax = axes[n_procap + i]
            y = vals_c[center_c - zoom:center_c + zoom, i]
            ax.plot(x, y, color='darkgreen', linewidth=0.5)
            ax.fill_between(x, y, alpha=0.3, color='green')
            ax.axvline(center, color='red', linewidth=2,
                       linestyle='--', alpha=0.8)
            tissue = meta_c.iloc[i].get('biosample_name', '')
            strand = meta_c.iloc[i].get('strand', '.')
            ax.set_ylabel(f'CAGE\n{tissue}\n({strand})', fontsize=7)
            ax.set_ylim(bottom=0)

        axes[0].set_title(
            f'PROCAP vs CAGE: {label}\n'
            f'Red line = breakpoint | 10kb window\n'
            f'Blue = PROCAP (transcription initiation) | '
            f'Green = CAGE (5\' cap mapping)',
            fontsize=12, fontweight='bold')
        axes[-1].set_xlabel('Position in interval', fontsize=10)
        plt.tight_layout()
        plt.savefig(f'{OUTPUT_DIR}/{name}_procap_vs_cage.png',
                    dpi=150, bbox_inches='tight', facecolor='white')
        plt.close('all')
        print(f"     Saved: {OUTPUT_DIR}/{name}_procap_vs_cage.png")

        # Zoomed comparison: 2kb window, just matching strand
        fig, axes = plt.subplots(2, 1, figsize=(20, 6), sharex=True)

        zoom2 = 1000
        x2 = np.arange(center - zoom2, center + zoom2)

        # Sum matching-strand PROCAP
        procap_sum = np.zeros(2 * zoom2)
        procap_count = 0
        for i, (_, row) in enumerate(meta_p.iterrows()):
            strand = row.get('strand', '.')
            if strand == gene_strand or strand == '.':
                procap_sum += vals_p[center - zoom2:center + zoom2, i]
                procap_count += 1
        if procap_count > 0:
            procap_sum /= procap_count

        # Sum matching-strand CAGE
        cage_sum = np.zeros(2 * zoom2)
        cage_count = 0
        for i, (_, row) in enumerate(meta_c.iterrows()):
            strand = row.get('strand', '.')
            if strand == gene_strand or strand == '.':
                cage_sum += vals_c[center_c - zoom2:center_c + zoom2, i]
                cage_count += 1
        if cage_count > 0:
            cage_sum /= cage_count

        axes[0].plot(x2, procap_sum, color='darkblue', linewidth=1)
        axes[0].fill_between(x2, procap_sum, alpha=0.3, color='blue')
        axes[0].axvline(center, color='red', linewidth=2, linestyle='--')
        axes[0].set_ylabel(f'PROCAP\n(mean {gene_strand} strand)', fontsize=10)
        axes[0].set_ylim(bottom=0)
        axes[0].set_title(
            f'Transcription Initiation: {label}\n'
            f'{gene_strand} strand | 2kb window | Red = breakpoint',
            fontsize=12, fontweight='bold')

        axes[1].plot(x2, cage_sum, color='darkgreen', linewidth=1)
        axes[1].fill_between(x2, cage_sum, alpha=0.3, color='green')
        axes[1].axvline(center, color='red', linewidth=2, linestyle='--')
        axes[1].set_ylabel(f'CAGE\n(mean {gene_strand} strand)', fontsize=10)
        axes[1].set_ylim(bottom=0)
        axes[1].set_xlabel('Position in interval', fontsize=10)

        plt.tight_layout()
        plt.savefig(f'{OUTPUT_DIR}/{name}_initiation_zoom.png',
                    dpi=150, bbox_inches='tight', facecolor='white')
        plt.close('all')
        print(f"     Saved: {OUTPUT_DIR}/{name}_initiation_zoom.png")

    except Exception as e:
        print(f"     Visualization error: {e}")

    all_results[name] = bp_results
    print()

# Save results
output_path = f'{OUTPUT_DIR}/procap_results.json'
with open(output_path, 'w') as f:
    json.dump(all_results, f, indent=2, default=str)
print(f"\nResults saved to {output_path}")

# Summary
print("\n" + "=" * 70)
print("PROCAP ANALYSIS SUMMARY")
print("=" * 70)
print(f"\nAll images saved to {OUTPUT_DIR}/")
print("Done.")
