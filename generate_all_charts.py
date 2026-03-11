#!/usr/bin/env python3
"""
Generate all remaining charts for Johnny ASPS Genomic Analysis
Based on AlphaGenome data from Queries 1-9 and drug target reports
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from scipy.interpolate import PchipInterpolator
import os

CHARTS_DIR = '/Users/lbacaj/genomics/charts'

# ============================================================
# CHART 5: Drug Target Expression Radar Chart
# ============================================================
def chart_drug_target_radar():
    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor('#f0f0f0')

    # Key drug targets with max expression across tissues
    targets = {
        'CTSD\n(Lysosomal)': 4.972,
        'VEGFB\n(Angiogenic)': 2.004,
        'IDH2\n(Metabolic)': 1.747,
        'CTSL\n(Lysosomal)': 1.458,
        'VEGFA\n(Angiogenic)': 1.484,
        'MRPS12\n(Mito Ribo)': 1.435,
        'MMP14\n(ECM)': 1.289,
        'IDH1\n(Metabolic)': 1.348,
        'MAP1LC3B\n(Autophagy)': 1.117,
        'SQSTM1/p62\n(Autophagy)': 1.156,
        'MT-CO1\n(ETC)': 0.893,
        'LAMP1\n(Lysosomal)': 0.743,
        'MRPS15\n(Mito Ribo)': 0.731,
        'TFE3\n(Fusion)': 0.586,
        'MT-ND1\n(ETC)': 0.554,
        'MMP7\n(ECM)': 0.506,
    }

    labels = list(targets.keys())
    values = list(targets.values())
    N = len(labels)

    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    values_plot = values + [values[0]]
    angles_plot = angles + [angles[0]]

    ax.set_facecolor('#f5f5f5')
    ax.fill(angles_plot, values_plot, color='#1a5c1a', alpha=0.15)
    ax.plot(angles_plot, values_plot, color='#1a5c1a', linewidth=2.5, marker='o',
            markersize=6, markerfacecolor='#1a5c1a', markeredgecolor='white',
            markeredgewidth=1.5)

    # Color code by drug
    drug_colors = {
        'CTSD': '#cc4400',  # HCQ
        'CTSL': '#cc4400',
        'LAMP1': '#cc4400',
        'MAP1LC3B': '#cc4400',
        'SQSTM1': '#cc4400',
        'VEGFB': '#2255aa',  # Cimetidine
        'VEGFA': '#2255aa',
        'MMP14': '#1a5c1a',  # Doxycycline
        'MMP7': '#1a5c1a',
        'MRPS12': '#1a5c1a',
        'MRPS15': '#1a5c1a',
        'MT-CO1': '#1a5c1a',
        'MT-ND1': '#1a5c1a',
        'IDH1': '#666666',  # Pathway
        'IDH2': '#666666',
        'TFE3': '#8b1a1a',  # Fusion
    }

    ax.set_xticks(angles)
    ax.set_xticklabels(labels, fontsize=8, fontweight='bold')

    # Color the tick labels
    for label, angle in zip(ax.get_xticklabels(), angles):
        txt = label.get_text().split('\n')[0].replace('/p62', '')
        if txt in drug_colors:
            label.set_color(drug_colors[txt])

    ax.set_ylim(0, 5.5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(['1.0', '2.0', '3.0', '4.0', '5.0'], fontsize=8, color='gray')

    # Add threshold line
    threshold_angles = np.linspace(0, 2*np.pi, 100)
    ax.plot(threshold_angles, [0.5]*100, color='red', linewidth=1, linestyle='--', alpha=0.4)
    ax.text(0, 0.65, 'High expr threshold (0.5)', fontsize=7, color='red', alpha=0.6)

    ax.set_title('Drug Target Expression Landscape\n(Gene Body Mean — Peak Tissue)',
                 fontsize=14, fontweight='bold', pad=25)

    # Legend
    legend_elements = [
        mpatches.Patch(color='#1a5c1a', label='Doxycycline targets'),
        mpatches.Patch(color='#cc4400', label='HCQ targets'),
        mpatches.Patch(color='#2255aa', label='Cimetidine targets'),
        mpatches.Patch(color='#8b1a1a', label='Fusion driver'),
        mpatches.Patch(color='#666666', label='Metabolic pathway'),
    ]
    ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1.35, 1.1),
              fontsize=9, framealpha=0.95, edgecolor='gray')

    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, 'drug_target_radar.png'), dpi=200,
                bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print("Chart saved: drug_target_radar.png")


# ============================================================
# CHART 6: Sequential vs. Simultaneous Priming
# ============================================================
def chart_priming_comparison():
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))
    fig.patch.set_facecolor('#f0f0f0')

    for ax in [ax1, ax2]:
        ax.set_facecolor('#f5f5f5')
        ax.grid(True, alpha=0.3, linestyle='-', color='gray')
        ax.set_axisbelow(True)

    # Sequential data from Query 6
    seq_days = [0, 30, 45, 60, 75, 90, 120]
    seq_total = [520, 470, 340, 252, 179, 127, 66]

    # Simultaneous data from Query 6
    sim_days = [0, 15, 30, 45, 60, 90, 120]
    sim_total = [520, 445, 360, 280, 214, 140, 73]

    # Normalize
    seq_pct = [v/520*100 for v in seq_total]
    sim_pct = [v/520*100 for v in sim_total]

    days_sm = np.linspace(0, 120, 300)
    seq_interp = PchipInterpolator(seq_days, seq_pct)
    sim_interp = PchipInterpolator(sim_days, sim_pct)

    # Left: Overall trajectory
    ax1.plot(days_sm, np.clip(seq_interp(days_sm), 0, 100),
             color='#1a5c1a', linewidth=3, label='Sequential (Doxy 30d → Triple)')
    ax1.plot(days_sm, np.clip(sim_interp(days_sm), 0, 100),
             color='#8b1a1a', linewidth=3, linestyle='--', dashes=(8,4),
             label='Simultaneous (All Day 1)')

    ax1.axvspan(0, 30, alpha=0.06, color='blue', zorder=0)
    ax1.text(15, 102, 'Doxy\nPriming', fontsize=8, ha='center', color='#333',
             fontweight='bold', path_effects=[pe.withStroke(linewidth=2, foreground='white')])

    # Difference annotation
    ax1.annotate(f'Sequential wins\nby ~10% at Day 120',
                 xy=(120, seq_pct[-1]), xytext=(85, 25),
                 fontsize=9, fontweight='bold', color='#1a5c1a',
                 arrowprops=dict(arrowstyle='->', color='#1a5c1a', lw=2),
                 path_effects=[pe.withStroke(linewidth=2, foreground='white')])

    ax1.scatter(seq_days, seq_pct, color='#1a5c1a', s=50, zorder=6,
                edgecolors='white', linewidth=1.5)
    ax1.scatter(sim_days, sim_pct, color='#8b1a1a', s=50, zorder=6,
                edgecolors='white', linewidth=1.5)

    ax1.set_xlim(0, 125)
    ax1.set_ylim(0, 105)
    ax1.set_xlabel('Days', fontsize=12, fontweight='bold')
    ax1.set_ylabel('Total Tumor Score (% of Baseline)', fontsize=12, fontweight='bold')
    ax1.set_title('Total Tumor Score: Sequential vs. Simultaneous', fontsize=13, fontweight='bold')
    ax1.legend(loc='upper right', fontsize=10, framealpha=0.95)

    # Right: Domain-by-domain at Day 120
    domains = ['Metabolic', 'Stromal', 'Vascular', 'Immune\nEvasion', 'Waste\nMgmt', 'Adaptive']
    seq_120 = [10, 5, 10, 20, 3, 18]
    sim_120 = [12, 8, 12, 18, 5, 18]

    x = np.arange(len(domains))
    w = 0.35
    bars_s = ax2.bar(x - w/2, seq_120, w, label='Sequential (Day 120)',
                      color='#1a5c1a', alpha=0.9, edgecolor='white', linewidth=1.5)
    bars_m = ax2.bar(x + w/2, sim_120, w, label='Simultaneous (Day 120)',
                      color='#8b1a1a', alpha=0.9, edgecolor='white', linewidth=1.5)

    for bars in [bars_s, bars_m]:
        for bar in bars:
            h = bar.get_height()
            ax2.text(bar.get_x() + bar.get_width()/2., h + 0.3,
                     f'{int(h)}', ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax2.set_xticks(x)
    ax2.set_xticklabels(domains, fontsize=10)
    ax2.set_ylabel('Remaining Score (lower = better)', fontsize=12, fontweight='bold')
    ax2.set_title('Domain Scores at Day 120', fontsize=13, fontweight='bold')
    ax2.legend(loc='upper left', fontsize=10, framealpha=0.95)
    ax2.set_ylim(0, 28)

    # Totals
    ax2.text(0.98, 0.95, f'Totals:\nSequential: 66/520\nSimultaneous: 73/520',
             transform=ax2.transAxes, fontsize=10, va='top', ha='right',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='white', alpha=0.9, edgecolor='gray'))

    plt.suptitle('Sequential Priming vs. Simultaneous Start', fontsize=15,
                 fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, 'priming_comparison.png'), dpi=200,
                bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print("Chart saved: priming_comparison.png")


# ============================================================
# CHART 7: Checkpoint Expression Waterfall
# ============================================================
def chart_checkpoint_waterfall():
    fig, ax = plt.subplots(figsize=(12, 6))
    fig.patch.set_facecolor('#f0f0f0')
    ax.set_facecolor('#f5f5f5')
    ax.grid(True, alpha=0.3, axis='x', linestyle='-', color='gray')
    ax.set_axisbelow(True)

    checkpoints = ['LAG3', 'TIM-3\n(HAVCR2)', 'PD-L1\n(CD274)', 'PD-1\n(PDCD1)',
                   'CTLA-4', 'TIGIT']
    values = [0.1112, 0.0645, 0.0519, 0.0173, 0.0059, 0.0035]
    colors = ['#cc2200', '#cc6600', '#dd8800', '#ddaa00', '#aabb00', '#88aa44']

    y_pos = np.arange(len(checkpoints))
    bars = ax.barh(y_pos, values, color=colors, edgecolor='white', linewidth=2, height=0.6)

    for bar, val in zip(bars, values):
        ax.text(bar.get_width() + 0.002, bar.get_y() + bar.get_height()/2,
                f'{val:.4f}', va='center', fontsize=11, fontweight='bold')

    # Highlight LAG3 as top target
    ax.annotate('HIGHEST — Primary\ncheckpoint target',
                xy=(0.1112, 0), xytext=(0.14, 0.8),
                fontsize=10, fontweight='bold', color='#cc2200',
                arrowprops=dict(arrowstyle='->', color='#cc2200', lw=2),
                path_effects=[pe.withStroke(linewidth=2, foreground='white')])

    # Ratio annotation
    ax.text(0.14, 4.5, 'LAG3 is 2.1x PD-L1\nand 6.4x PD-1',
            fontsize=10, fontweight='bold', color='#333',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#fff3cc', alpha=0.9, edgecolor='#cc6600'))

    ax.set_yticks(y_pos)
    ax.set_yticklabels(checkpoints, fontsize=12, fontweight='bold')
    ax.set_xlabel('Gene Body Mean Expression (Top Tissue)', fontsize=12, fontweight='bold')
    ax.set_title('Immune Checkpoint Expression Ranking — Case for Anti-LAG3',
                 fontsize=14, fontweight='bold', pad=15)
    ax.invert_yaxis()
    ax.set_xlim(0, 0.18)

    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, 'checkpoint_waterfall.png'), dpi=200,
                bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print("Chart saved: checkpoint_waterfall.png")


# ============================================================
# CHART 8: Toxicity Head-to-Head
# ============================================================
def chart_toxicity_comparison():
    fig, axes = plt.subplots(1, 3, figsize=(16, 6))
    fig.patch.set_facecolor('#f0f0f0')

    for ax in axes:
        ax.set_facecolor('#f5f5f5')
        ax.set_axisbelow(True)

    # Panel 1: Grade 3-4 Events
    ax1 = axes[0]
    approaches = ['Triple\nBlockade', 'Nivo/Ipi/Cabo', 'Hybrid\n(A+LAG3)']
    grade34 = [5, 50, 10]  # percentage
    colors = ['#1a5c1a', '#8b1a1a', '#2255aa']
    bars = ax1.bar(approaches, grade34, color=colors, edgecolor='white', linewidth=2, width=0.6)
    for bar, val in zip(bars, grade34):
        ax1.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
                 f'{val}%', ha='center', fontsize=13, fontweight='bold')
    ax1.set_ylabel('Patients (%)', fontsize=11, fontweight='bold')
    ax1.set_title('Grade 3-4 Adverse Events', fontsize=12, fontweight='bold')
    ax1.set_ylim(0, 65)
    ax1.grid(True, alpha=0.3, axis='y')

    # Panel 2: Treatment Discontinuation
    ax2 = axes[1]
    discont = [5, 35, 8]
    bars2 = ax2.bar(approaches, discont, color=colors, edgecolor='white', linewidth=2, width=0.6)
    for bar, val in zip(bars2, discont):
        ax2.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 1,
                 f'{val}%', ha='center', fontsize=13, fontweight='bold')
    ax2.set_ylabel('Patients (%)', fontsize=11, fontweight='bold')
    ax2.set_title('Treatment Discontinuation', fontsize=12, fontweight='bold')
    ax2.set_ylim(0, 50)
    ax2.grid(True, alpha=0.3, axis='y')

    # Panel 3: Multi-factor comparison
    ax3 = axes[2]
    factors = ['Life-threat\nrisk', 'Permanent\nside effects', 'QoL\nimpact', 'Cost']

    # Score 1-5 (1=best, 5=worst)
    a_scores = [1, 1.5, 1, 1]
    b_scores = [3.5, 4, 4, 5]
    h_scores = [1.5, 1.5, 1.5, 2.5]

    x = np.arange(len(factors))
    w = 0.25
    ax3.bar(x - w, a_scores, w, color='#1a5c1a', alpha=0.9, edgecolor='white',
            linewidth=1.5, label='Triple Blockade')
    ax3.bar(x, b_scores, w, color='#8b1a1a', alpha=0.9, edgecolor='white',
            linewidth=1.5, label='Nivo/Ipi/Cabo')
    ax3.bar(x + w, h_scores, w, color='#2255aa', alpha=0.9, edgecolor='white',
            linewidth=1.5, label='Hybrid')

    ax3.set_xticks(x)
    ax3.set_xticklabels(factors, fontsize=9)
    ax3.set_ylabel('Severity (1=lowest, 5=highest)', fontsize=10, fontweight='bold')
    ax3.set_title('Risk Factor Comparison', fontsize=12, fontweight='bold')
    ax3.legend(fontsize=8, framealpha=0.95)
    ax3.set_ylim(0, 6)
    ax3.grid(True, alpha=0.3, axis='y')

    plt.suptitle('Toxicity & Side Effect Comparison', fontsize=15, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, 'toxicity_comparison.png'), dpi=200,
                bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print("Chart saved: toxicity_comparison.png")


# ============================================================
# CHART 9: ISM Heatmap Across Breakpoints
# ============================================================
def chart_ism_heatmap():
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.patch.set_facecolor('#f0f0f0')

    # Data: top 10 positions per breakpoint (DNase-seq absolute scores)
    breakpoints = {
        'ASPSCR1 (chr17)\nRNA-seq': {
            'offsets': [+58, +59, +57, +56, -11, -10, +62, -12, -9, -21],
            'scores': [0.8251, 0.8198, 0.8097, 0.7767, 0.7175, 0.6939, 0.5939, 0.5726, 0.5377, 0.4957],
        },
        'TFE3 (chrX)\nDNase-seq': {
            'offsets': [-93, -98, -97, -96, -94, -99, -95, -88, -3, -100],
            'scores': [3.2928, 3.2021, 3.2014, 3.1858, 3.0908, 3.0826, 3.0251, 2.7839, 2.1433, 1.8828],
        },
        'DNMT1-chr1\nDNase-seq': {
            'offsets': [+125, -102, -57, -108, -112, +99, +102, +100, -100, -103],
            'scores': [0.0316, 0.0256, 0.0230, 0.0222, 0.0207, 0.0193, 0.0191, 0.0169, 0.0158, 0.0149],
        },
        'DNMT1-chr19\nDNase-seq': {
            'offsets': [-66, -66, -66, -66, -66, -66, -66, -66, -66, -66],
            'scores': [0.4359, 0.2212, 0.1712, 0.1685, 0.1600, 0.1594, 0.1566, 0.1528, 0.1332, 0.1313],
        },
    }
    cell_labels = {
        'ASPSCR1 (chr17)\nRNA-seq': ['Foreskin\nfibro', 'G401', 'HepG2', 'NCI-H460',
                                       'IMR-90', 'HeLa-S3', 'Caki2', 'MG63', 'HT1080', 'SK-N-SH'],
        'TFE3 (chrX)\nDNase-seq': ['Tfh cell', 'EM CD4+', 'Mem CD4+', 'Th22',
                                     'Th2', 'Imm NK', 'Mem CD8+', 'CMP', 'CM CD4+', 'CD4+ T'],
        'DNMT1-chr1\nDNase-seq': ['Tropho-\nblast', 'Chondro-\ncyte', 'Endo-\ndermal',
                                    'Glut.\nneuron', 'Keratino-\ncyte', 'Th1', 'NK cell',
                                    'Endothel.', 'T-cell', 'Th2'],
        'DNMT1-chr19\nDNase-seq': ['Imm NK', 'Th2', 'CD8+ T', 'CM CD4+', 'Mem CD4+',
                                     'EM CD8+', 'Mem CD8+', 'T-cell', 'Th22', 'CD4+ T'],
    }

    colors_map = ['#1a5c1a', '#8b1a1a', '#666666', '#2255aa']

    for idx, (bp_name, data) in enumerate(breakpoints.items()):
        ax = axes[idx // 2][idx % 2]
        ax.set_facecolor('#f5f5f5')
        ax.grid(True, alpha=0.3, axis='x', color='gray')
        ax.set_axisbelow(True)

        y = np.arange(len(data['scores']))
        color = colors_map[idx]
        bars = ax.barh(y, data['scores'], color=color, alpha=0.85,
                        edgecolor='white', linewidth=1.5, height=0.7)

        for bar, val in zip(bars, data['scores']):
            ax.text(bar.get_width() + max(data['scores'])*0.02,
                    bar.get_y() + bar.get_height()/2,
                    f'{val:.4f}', va='center', fontsize=8, fontweight='bold')

        labels = cell_labels[bp_name]
        ax.set_yticks(y)
        ax.set_yticklabels(labels, fontsize=8, fontweight='bold')
        ax.invert_yaxis()
        ax.set_title(bp_name, fontsize=12, fontweight='bold', color=color)
        ax.set_xlabel('Absolute ISM Score', fontsize=10)

    # Highlight the TFE3 panel
    axes[0][1].text(0.95, 0.05,
                     'MOST SIGNIFICANT\nFINDING\n7bp immune element\n(scores 4-8x all others)',
                     transform=axes[0][1].transAxes, fontsize=9, fontweight='bold',
                     color='#8b1a1a', ha='right', va='bottom',
                     bbox=dict(boxstyle='round,pad=0.4', facecolor='#ffeeee',
                               alpha=0.95, edgecolor='#8b1a1a', linewidth=2))

    plt.suptitle('In Silico Mutagenesis: Top Impact Scores Across All 4 Breakpoints',
                 fontsize=15, fontweight='bold', y=1.01)
    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, 'ism_heatmap.png'), dpi=200,
                bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print("Chart saved: ism_heatmap.png")


# ============================================================
# CHART 10: Escape Route Trap Diagram
# ============================================================
def chart_escape_routes():
    fig, ax = plt.subplots(figsize=(14, 8))
    fig.patch.set_facecolor('#f0f0f0')
    ax.set_facecolor('#f5f5f5')
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7, 9.5, 'Escape Route Analysis: All Exits Sealed',
            fontsize=16, fontweight='bold', ha='center', va='center')
    ax.text(7, 9.0, 'Three potential tumor escape routes — each blocked by a specific drug mechanism',
            fontsize=10, ha='center', va='center', color='#555')

    # Three escape routes as columns
    routes = [
        {
            'name': 'Angiogenic Switching',
            'desc': 'Bypass cimetidine via\nalternative VEGF signaling',
            'attempt': 'Upregulate VEGF to\nforce new blood vessels',
            'blocker': 'DOXYCYCLINE',
            'mechanism': 'MMP14 (1.289) paralyzed\n→ No chemical bulldozers\nto carve vessel tunnels\n→ VEGF signals useless',
            'x': 2.5,
        },
        {
            'name': 'Metabolic Reprogramming',
            'desc': 'Switch from Reverse Warburg\nto standard glycolysis',
            'attempt': 'Reactivate dormant\nglycolytic machinery',
            'blocker': 'DOXYCYCLINE + HCQ',
            'mechanism': 'TFEB 0.083, mTOR 0.070\n→ Glycolytic machinery\natrophied beyond recovery\n→ Mito already damaged',
            'x': 7.0,
        },
        {
            'name': 'Macrophage Subversion',
            'desc': 'Hijack M1 macrophages\ninto M2 "builders"',
            'attempt': 'Convert destroyers into\ncollagen bunker rebuilders',
            'blocker': 'IMMUNE RESPONSE',
            'mechanism': 'Massive M1 inflammatory\nstate (GI purge evidence)\n→ Environment too hostile\nfor M1→M2 conversion',
            'x': 11.5,
        },
    ]

    for r in routes:
        x = r['x']
        # Escape route box (red)
        escape_box = FancyBboxPatch((x-1.8, 6.5), 3.6, 1.8,
                                     boxstyle="round,pad=0.15",
                                     facecolor='#ffdddd', edgecolor='#cc4444', linewidth=2)
        ax.add_patch(escape_box)
        ax.text(x, 7.8, r['name'], fontsize=11, fontweight='bold', ha='center',
                va='center', color='#8b0000')
        ax.text(x, 7.0, r['attempt'], fontsize=8, ha='center', va='center', color='#555')

        # Arrow down
        ax.annotate('', xy=(x, 5.0), xytext=(x, 6.5),
                     arrowprops=dict(arrowstyle='->', color='#cc4444', lw=2.5))

        # BLOCKED stamp
        ax.text(x, 5.6, 'BLOCKED', fontsize=14, fontweight='bold',
                ha='center', va='center', color='#cc0000', rotation=15,
                bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                          edgecolor='#cc0000', linewidth=3, alpha=0.9))

        # Blocker box (green)
        blocker_box = FancyBboxPatch((x-1.8, 2.5), 3.6, 2.2,
                                      boxstyle="round,pad=0.15",
                                      facecolor='#ddffdd', edgecolor='#1a5c1a', linewidth=2)
        ax.add_patch(blocker_box)
        ax.text(x, 4.3, r['blocker'], fontsize=10, fontweight='bold', ha='center',
                va='center', color='#0a3d0a')
        ax.text(x, 3.2, r['mechanism'], fontsize=8, ha='center', va='center', color='#333')

        # Result
        ax.text(x, 1.8, 'EXIT SEALED', fontsize=10, fontweight='bold',
                ha='center', va='center', color='#1a5c1a',
                path_effects=[pe.withStroke(linewidth=2, foreground='white')])

    # Bottom summary
    ax.text(7, 0.6, 'The tumor\'s "quiet genome" (no chaotic mutations) means it lacks the mutational agility\n'
            'to invent novel escape proteins. All three mechanical workarounds are trapped.',
            fontsize=10, ha='center', va='center', color='#333',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#fff8dd', edgecolor='#ccaa44', alpha=0.9))

    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, 'escape_routes.png'), dpi=200,
                bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print("Chart saved: escape_routes.png")


# ============================================================
# CHART 11: Three-Matrix Bubble Chart
# ============================================================
def chart_three_matrices():
    fig, axes = plt.subplots(1, 3, figsize=(18, 7))
    fig.patch.set_facecolor('#f0f0f0')

    matrices = [
        {
            'title': 'Matrix 1: Dangerous Attributes\n(Growth & Angiogenesis)',
            'color': '#cc2200',
            'labels': ['Umbilical vein\nendothelial', 'Mammary micro-\nvascular endo.',
                       'Mesenchymal\nstem cell', 'Pulmonary artery\nendothelial',
                       'Neuronal\nstem cell', 'Common myeloid\nprogenitor',
                       'Coronary artery\nendothelial'],
            'scores': [11.53, 9.72, 8.69, 7.83, 6.91, 6.88, 6.66],
        },
        {
            'title': 'Matrix 2: Highest Vulnerabilities\n(Metabolic & Repair)',
            'color': '#1a5c1a',
            'labels': ['Skeletal muscle\nmyoblast', 'Fibroblast\nof lung',
                       'Foreskin\nfibroblast', 'Bronchus fibro-\nblast of lung',
                       'Fibroblast\ncell line', 'Smooth\nmuscle cell',
                       'Kidney\nepithelial'],
            'scores': [13.63, 13.34, 13.31, 10.66, 9.95, 9.88, 7.42],
        },
        {
            'title': 'Matrix 3: Probable Targets\n(Immune/Druggable)',
            'color': '#2255aa',
            'labels': ['Naive B cell', 'IgD-neg memory\nB cell',
                       'CD4+ CD25+\nreg T cell', 'CD4+ memory\nT cell',
                       'Naive CD8+\nT cell', 'CD8+ memory\nT cell',
                       'Immature\nNK cell'],
            'scores': [11.63, 9.75, 9.00, 8.88, 8.25, 8.13, 7.25],
        },
    ]

    for ax, m in zip(axes, matrices):
        ax.set_facecolor('#f5f5f5')
        ax.grid(True, alpha=0.3, axis='x', color='gray')
        ax.set_axisbelow(True)

        y = np.arange(len(m['scores']))
        sizes = [s * 5 for s in m['scores']]  # bubble size proportional to score

        # Horizontal bar + bubble overlay
        bars = ax.barh(y, m['scores'], color=m['color'], alpha=0.3,
                        edgecolor=m['color'], linewidth=1.5, height=0.6)
        ax.scatter(m['scores'], y, s=sizes, color=m['color'], alpha=0.8,
                    edgecolors='white', linewidth=2, zorder=5)

        for i, (score, label) in enumerate(zip(m['scores'], m['labels'])):
            ax.text(score + 0.3, i, f'{score:.2f}', va='center', fontsize=9, fontweight='bold')

        ax.set_yticks(y)
        ax.set_yticklabels(m['labels'], fontsize=8, fontweight='bold')
        ax.invert_yaxis()
        ax.set_title(m['title'], fontsize=11, fontweight='bold', color=m['color'])
        ax.set_xlabel('Score', fontsize=10)

    plt.suptitle('AlphaGenome Three-Matrix Analysis: Tumor Profile',
                 fontsize=15, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, 'alphagenome_matrices.png'), dpi=200,
                bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print("Chart saved: alphagenome_matrices.png")


# ============================================================
# CHART 12: HCQ Pharmacokinetic Loading Curve
# ============================================================
def chart_hcq_loading():
    fig, ax = plt.subplots(figsize=(14, 7))
    fig.patch.set_facecolor('#f0f0f0')
    ax.set_facecolor('#f5f5f5')
    ax.grid(True, alpha=0.3, linestyle='-', color='gray')
    ax.set_axisbelow(True)

    # HCQ pharmacokinetics: t1/2 = 40-50 days, starts at Day 31
    t_half = 45  # days
    k = np.log(2) / t_half

    # Days from start of treatment (Doxy starts Day 0, HCQ starts Day 31)
    days = np.linspace(0, 180, 500)

    # HCQ tissue accumulation: C(t) = Css * (1 - e^(-k*t)) where t is days since HCQ start
    hcq_days_on = np.maximum(days - 31, 0)
    hcq_level = 100 * (1 - np.exp(-k * hcq_days_on))
    hcq_level[days < 31] = 0

    # Doxycycline steady state (fast, t1/2 ~20 hrs)
    doxy_level = 100 * (1 - np.exp(-np.log(2) / 0.83 * days))  # 0.83 days = 20 hrs

    # Cimetidine (starts Day 20, based on actual timeline, fast PK)
    cim_days_on = np.maximum(days - 20, 0)
    cim_level = 100 * (1 - np.exp(-np.log(2) / 0.5 * cim_days_on))
    cim_level[days < 20] = 0

    ax.plot(days, doxy_level, color='#1a5c1a', linewidth=2.5, label='Doxycycline (t½ ~20h)')
    ax.plot(days, cim_level, color='#2255aa', linewidth=2.5, linestyle='-.',
            label='Cimetidine (t½ ~2h)')
    ax.plot(days, hcq_level, color='#cc4400', linewidth=3.5,
            label='HCQ (t½ ~40-50 days)', zorder=6)

    # Key thresholds
    ax.axhline(y=50, color='gray', linewidth=1, linestyle=':', alpha=0.5)
    ax.text(2, 52, '50% steady-state', fontsize=9, color='gray')

    ax.axhline(y=90, color='gray', linewidth=1, linestyle=':', alpha=0.5)
    ax.text(2, 92, '90% steady-state', fontsize=9, color='gray')

    # Annotate HCQ milestones
    # 50% at ~31 days after start = Day 62
    day_50 = 31 + t_half
    ax.annotate(f'HCQ 50% level\n(Day {int(day_50)})',
                xy=(day_50, 50), xytext=(day_50 + 15, 35),
                fontsize=9, fontweight='bold', color='#cc4400',
                arrowprops=dict(arrowstyle='->', color='#cc4400', lw=2),
                path_effects=[pe.withStroke(linewidth=2, foreground='white')])

    # HCQ still deepening at Day 90 (55-65% of Css)
    hcq_at_90 = 100 * (1 - np.exp(-k * (90 - 31)))
    ax.annotate(f'HCQ at Day 90: {hcq_at_90:.0f}%\n(still deepening)',
                xy=(90, hcq_at_90), xytext=(105, hcq_at_90 - 15),
                fontsize=9, fontweight='bold', color='#cc4400',
                arrowprops=dict(arrowstyle='->', color='#cc4400', lw=2),
                path_effects=[pe.withStroke(linewidth=2, foreground='white')])

    # Phase annotations
    ax.axvspan(0, 31, alpha=0.06, color='blue')
    ax.axvspan(31, 180, alpha=0.06, color='red')
    ax.text(15, 105, 'Phase 1: Doxy Only', fontsize=9, ha='center', fontweight='bold',
            color='#333', path_effects=[pe.withStroke(linewidth=2, foreground='white')])
    ax.text(105, 105, 'Phase 2: Triple Blockade', fontsize=9, ha='center', fontweight='bold',
            color='#333', path_effects=[pe.withStroke(linewidth=2, foreground='white')])

    # Key insight box
    ax.text(0.98, 0.45, 'Critical Insight:\nHCQ\'s extremely long half-life\n'
            'means the lysosomal blockade\ndeepens for MONTHS after starting.\n'
            'By Day 90, tissue levels are\nstill only ~65% of maximum.\n'
            'The blockade becomes self-\nsustaining — even brief drug\n'
            'holidays cannot reverse it.',
            transform=ax.transAxes, fontsize=9, va='center', ha='right',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#fff3dd', edgecolor='#cc6600',
                      alpha=0.95, linewidth=1.5))

    ax.set_xlim(0, 180)
    ax.set_ylim(0, 110)
    ax.set_xticks(np.arange(0, 195, 15))
    ax.set_xlabel('Days', fontsize=13, fontweight='bold')
    ax.set_ylabel('Tissue Concentration (% of Steady State)', fontsize=13, fontweight='bold')
    ax.set_title('Pharmacokinetic Loading: Triple Blockade Drug Accumulation',
                 fontsize=14, fontweight='bold', pad=15)
    ax.legend(loc='center left', fontsize=11, framealpha=0.95, edgecolor='gray')
    ax.tick_params(axis='both', which='major', labelsize=11)

    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, 'hcq_loading_curve.png'), dpi=200,
                bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print("Chart saved: hcq_loading_curve.png")


# ============================================================
# CHART 13: Fortress Architecture Diagram
# ============================================================
def chart_fortress_layers():
    fig, ax = plt.subplots(figsize=(14, 10))
    fig.patch.set_facecolor('#f0f0f0')
    ax.set_facecolor('#f5f5f5')
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 12)
    ax.axis('off')

    ax.text(7, 11.5, 'The Fortress: Five Defensive Layers & Drug Attacks',
            fontsize=16, fontweight='bold', ha='center')

    # Concentric-like layers from outside to inside (top to bottom)
    layers = [
        {
            'name': 'Layer 5: Epigenetic Fog',
            'desc': 'DNMT1 disruption → progressive methylation\ninstability, alters antigen presentation',
            'score': 'IDH1: 1.348 | IDH2: 1.747',
            'drug': 'Self-eroding\n(progressive demethylation)',
            'drug_color': '#888888',
            'y': 9.8, 'color': '#e8d0ff', 'edge': '#9955cc',
        },
        {
            'name': 'Layer 4: Immune Exclusion Zone',
            'desc': 'TFE3 7bp element (DNase 3.29) + DNMT1 T-cell switch\n+ LAG3 checkpoint + lactate moat + Treg enhancement',
            'score': 'LAG3: 0.111 | Treg score: 9.0',
            'drug': 'CIMETIDINE\n(immune modulation)',
            'drug_color': '#2255aa',
            'y': 7.8, 'color': '#d0e0ff', 'edge': '#4466cc',
        },
        {
            'name': 'Layer 3: Vascular Network',
            'desc': 'Dense neovascularization feeding tumor + fibroblasts\nEndothelial Danger Score: 11.53',
            'score': 'VEGFB: 2.004 | VEGFA: 1.484 | KDR: 0.327',
            'drug': 'CIMETIDINE\n(anti-VEGF) +\nDOXYCYCLINE\n(MMP → no vessel tunnels)',
            'drug_color': '#2255aa',
            'y': 5.8, 'color': '#ffe0d0', 'edge': '#cc6644',
        },
        {
            'name': 'Layer 2: Acidic Moat (Reverse Warburg Lactate)',
            'desc': 'Enslaved fibroblast glycolysis → lactate → acidic\nperimeter paralyzes T-cells and NK cells',
            'score': 'Fibroblast vuln: 13.63 | CTSD: 4.972',
            'drug': 'HCQ\n(lysosomal poison →\nfibroblast death →\nlactate pipeline cut)',
            'drug_color': '#cc4400',
            'y': 3.8, 'color': '#ffffcc', 'edge': '#ccaa00',
        },
        {
            'name': 'Layer 1: Collagen Bunker',
            'desc': 'Massive collagen barrier from enslaved fibroblasts\nFibrosis Score: 14.81',
            'score': 'MMP14: 1.289 | MMP7: 0.506',
            'drug': 'DOXYCYCLINE\n(MMP inhibition →\nbunker dissolves)',
            'drug_color': '#1a5c1a',
            'y': 1.8, 'color': '#d5e8d4', 'edge': '#448844',
        },
    ]

    for layer in layers:
        y = layer['y']
        # Layer box
        box = FancyBboxPatch((0.5, y - 0.7), 8.5, 1.5,
                              boxstyle="round,pad=0.15",
                              facecolor=layer['color'], edgecolor=layer['edge'],
                              linewidth=2.5)
        ax.add_patch(box)
        ax.text(0.8, y + 0.35, layer['name'], fontsize=11, fontweight='bold',
                va='center', color=layer['edge'])
        ax.text(0.8, y - 0.1, layer['desc'], fontsize=8, va='center', color='#333')
        ax.text(0.8, y - 0.45, layer['score'], fontsize=8, va='center', color='#666',
                fontstyle='italic')

        # Drug attack box
        drug_box = FancyBboxPatch((10.0, y - 0.55), 3.5, 1.2,
                                   boxstyle="round,pad=0.15",
                                   facecolor='white', edgecolor=layer['drug_color'],
                                   linewidth=2)
        ax.add_patch(drug_box)
        ax.text(11.75, y + 0.05, layer['drug'], fontsize=8, fontweight='bold',
                ha='center', va='center', color=layer['drug_color'])

        # Attack arrow
        ax.annotate('', xy=(10.0, y), xytext=(9.0, y),
                     arrowprops=dict(arrowstyle='->', color=layer['drug_color'],
                                    lw=2.5, connectionstyle='arc3,rad=0'))

    # Center label
    ax.text(4.75, 0.5, 'TUMOR CORE: ASPSCR1-TFE3 Fusion Engine + DNMT1 Shield',
            fontsize=10, fontweight='bold', ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#ff6666', edgecolor='#cc0000',
                      alpha=0.9, linewidth=2),
            color='white')

    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, 'fortress_layers.png'), dpi=200,
                bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print("Chart saved: fortress_layers.png")


# ============================================================
# RUN ALL
# ============================================================
if __name__ == '__main__':
    chart_drug_target_radar()
    chart_priming_comparison()
    chart_checkpoint_waterfall()
    chart_toxicity_comparison()
    chart_ism_heatmap()
    chart_escape_routes()
    chart_three_matrices()
    chart_hcq_loading()
    chart_fortress_layers()
    print("\n=== All 9 remaining charts generated successfully ===")
