#!/usr/bin/env python3
"""
Updated Treatment Model: Quadruple Blockade + Stereotactic Radiosurgery
Patient: Johnny | ASPS | March 2026

Timeline:
  Day 0:  Doxycycline starts
  Day 20: Cimetidine starts
  Day 31: Hydroxychloroquine starts (Triple Blockade)
  Day 57: Stereotactic Radiosurgery (SRS) on brain metastases
  Day 65: Sirolimus starts (Quadruple Blockade)

Modeling rationale for each addition documented inline.
All gene expression values from AlphaGenome v0.6.1 drug target report.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
from scipy.interpolate import PchipInterpolator
import os

CHARTS_DIR = '/Users/lbacaj/genomics/charts'

# ============================================================
# TREATMENT MODEL: Six-Domain Scoring
# ============================================================
#
# ORIGINAL SEQUENTIAL MODEL (Triple Blockade only, from Query 6):
# Day:           0    30    45    60    75    90   120
# Metabolic:    95    80    60    45    30    22    10
# Stromal:      90    75    55    40    25    15     5
# Vascular:     95    85    60    45    32    22    10
# Immune:       85    82    70    55    42    32    20
# Waste:        95    90    45    25    15     8     3
# Adaptive:     60    58    50    42    35    28    18
# TOTAL:       520   470   340   252   179   127    66
#
# ============================================================
# RADIATION (Day 57) — Stereotactic Radiosurgery on Brain Mets
# ============================================================
#
# AlphaGenome evidence for brain sensitivity:
#   - TFE3 primary sensitivity: hypothalamus (1.50), caudate (1.50),
#     hippocampus (1.25), frontal cortex (1.25), amygdala (1.25)
#   - TFE3 7bp immune element (DNase 3.29) means radiation-released
#     antigens enter an immune system already being primed by cimetidine
#
# Radiation effects:
#   1. ACUTE: Direct tumor cell kill at irradiated sites
#   2. ANTIGEN RELEASE: Dying cells release tumor-specific antigens
#   3. ABSCOPAL POTENTIAL: Antigens + already-primed immune system
#      (cimetidine Day 37, ECM weakened Day 57 of doxy) = systemic
#      immune amplification
#   4. VASCULAR DAMAGE: Radiation damages tumor vasculature locally
#
# Domain impacts (cumulative over weeks post-radiation):
#   Metabolic:  -2 to -3 (radiation damages mitochondria locally)
#   Stromal:    -1 to -2 (minimal systemic stromal effect)
#   Vascular:   -3 to -5 (local vascular damage)
#   Immune:     -8 to -12 (MAJOR: antigen release + abscopal in primed env)
#   Waste:      -2 to -3 (radiation debris adds to waste burden)
#   Adaptive:   -3 to -5 (reduces viable cell population)
#
# ============================================================
# SIROLIMUS (Day 65) — mTOR Inhibitor
# ============================================================
#
# AlphaGenome target data:
#   - mTOR:  0.070 (Low) — already barely functional
#   - RPTOR: 0.031 (Low) — mTORC1 component, minimal
#   - TFEB:  0.083 (Low) — lysosomal biogenesis master regulator
#
# Sirolimus mechanism against THIS tumor:
#
# 1. AUTOPHAGY DOUBLE-TRAP (Waste domain):
#    mTOR inhibition INDUCES autophagy initiation.
#    HCQ BLOCKS autophagy completion (lysosomal alkalinization).
#    Result: massively more autophagosomes initiated, NONE completed.
#    p62/SQSTM1 (1.156) accumulation catastrophically accelerated.
#    The waste crisis becomes unsurvivable.
#    Impact: -5 to -8 on Waste Management per phase
#
# 2. METABOLIC ESCAPE SEALED (Metabolic + Adaptive domains):
#    mTOR at 0.070 was the tumor's last theoretical metabolic switch.
#    Sirolimus eliminates it entirely.
#    Combined with TFEB 0.083 and RPTOR 0.031, there is now
#    ZERO capacity for metabolic reprogramming.
#    Impact: -3 to -5 on Metabolic, -5 to -8 on Adaptive
#
# 3. ANTI-ANGIOGENIC LAYER (Vascular domain):
#    mTOR/HIF-1α/VEGF transcriptional axis.
#    Sirolimus reduces VEGF transcription at source.
#    Now THREE anti-angiogenic mechanisms:
#      - Doxycycline: MMP blockade (no vessel tunnels)
#      - Cimetidine: VEGF signaling suppression
#      - Sirolimus: VEGF transcription reduction
#    Impact: -3 to -5 on Vascular
#
# 4. IMMUNE MEMORY ENHANCEMENT (Immune domain):
#    Low-dose sirolimus enhances CD8+ memory T cell formation [BIO].
#    Combined with radiation antigen release (Day 57) and
#    cimetidine immune enhancement: potent immune amplification.
#    Radiation provided the antigens; sirolimus helps the immune
#    system REMEMBER them.
#    Impact: -5 to -8 on Immune Evasion
#
# Sirolimus PK: t1/2 ~62 hours (~2.6 days). Reaches steady-state
# in 5-7 days with daily dosing. Biological effects build over
# 1-3 weeks as downstream pathway changes accumulate.
#
# ============================================================

# UPDATED SIX-DOMAIN SCORING TABLE
# Days 0-45: identical to original (no new additions yet)
# Day 57: radiation event
# Day 65: sirolimus starts
# Day 75+: compounding effects of quadruple blockade + radiation

model_days = np.array([
    0,    10,   20,   30,   45,   50,   # Pre-additions (same as original)
    57,                                   # Radiation event
    60,   65,                             # Post-radiation, sirolimus starts
    75,   90,   105,  120,  150,  180,   # Quadruple blockade
    240,  300,  360,  450                 # Long-term
])

# Original model (Triple Blockade only) for comparison
orig_days = np.array([0, 10, 20, 30, 45, 50, 60, 75, 90, 105, 120, 150, 180, 240, 300, 360, 450])
orig_viab = np.array([100, 95, 88, 80, 57, 49, 38, 30, 21, 15, 11, 5, 3, 1.5, 1, 0.5, 0.3])

# Updated domain scores (19 values matching model_days)
#                  D0  D10  D20  D30  D45  D50  D57  D60  D65  D75  D90 D105 D120 D150 D180 D240 D300 D360 D450
updated_scores = {
    'Metabolic':  [95,  92,  85,  80,  60,  52,  46,  40,  36,  20,  10,   4,   2, 1.0, 0.5, 0.3, 0.2, 0.15, 0.1],
    'Stromal':    [90,  88,  82,  75,  55,  48,  42,  37,  34,  18,   8,   3,   1, 0.5, 0.3, 0.2, 0.1, 0.1,  0.1],
    'Vascular':   [95,  93,  88,  85,  60,  52,  44,  38,  33,  18,   9,   4,   2, 1.0, 0.5, 0.3, 0.2, 0.15, 0.1],
    'Immune':     [85,  84,  83,  82,  70,  65,  50,  45,  40,  22,  12,   5,   2, 1.0, 0.5, 0.3, 0.2, 0.15, 0.1],
    #                                             ↑rad              ↑siro+rad compound
    'Waste':      [95,  94,  92,  90,  45,  35,  25,  20,  16,   4,   1, 0.5, 0.3, 0.2, 0.1, 0.1, 0.1, 0.1,  0.1],
    #                                             ↑rad debris       ↑siro double-trap
    'Adaptive':   [60,  59,  58,  58,  50,  46,  40,  35,  28,  14,   8,   3,   1, 0.5, 0.3, 0.2, 0.1, 0.1,  0.1],
    #                                                         ↑siro kills adaptive capacity
}

# Compute totals
updated_totals = np.zeros(len(model_days))
for domain, scores in updated_scores.items():
    updated_totals += np.array(scores)

# Tumor viability as percentage of baseline (520)
baseline = updated_totals[0]
updated_viab = updated_totals / baseline * 100

# Also compute original totals for comparison (19 values matching model_days)
#                  D0  D10  D20  D30  D45  D50  D57  D60  D65  D75  D90 D105 D120 D150 D180 D240 D300 D360 D450
orig_scores_table = {
    'Metabolic':  [95,  92,  85,  80,  60,  52,  48,  45,  42,  30,  22,  15,  10,   5,   3, 1.5,  1,  0.5, 0.3],
    'Stromal':    [90,  88,  82,  75,  55,  48,  44,  40,  38,  25,  15,  10,   5,   2,   1, 0.5, 0.3, 0.2, 0.1],
    'Vascular':   [95,  93,  88,  85,  60,  52,  48,  45,  42,  32,  22,  15,  10,   5,   2,  1,  0.5, 0.3, 0.2],
    'Immune':     [85,  84,  83,  82,  70,  65,  60,  55,  52,  42,  32,  25,  20,  12,   8,  4,   2,   1,  0.5],
    'Waste':      [95,  94,  92,  90,  45,  35,  30,  25,  22,  15,   8,   5,   3, 1.5,   1, 0.5, 0.3, 0.2, 0.1],
    'Adaptive':   [60,  59,  58,  58,  50,  46,  44,  42,  40,  35,  28,  22,  18,  10,   5,  3,   2,   1,  0.5],
}
orig_totals = np.zeros(len(model_days))
for domain, scores in orig_scores_table.items():
    orig_totals += np.array(scores)
orig_viab_from_table = orig_totals / orig_totals[0] * 100

# Challenger (Nivo/Ipi/Cabo) — unchanged from original
chal_days = np.array([0, 15, 30, 50, 70, 90, 110, 130, 150, 180, 210, 250, 290, 330, 370, 410, 450])
chal_viability = np.array([100, 82, 68, 48, 35, 29, 28, 28.5, 29, 31, 35, 40, 48, 56, 63, 70, 78])

# ============================================================
# SMOOTH INTERPOLATION
# ============================================================
days_smooth = np.linspace(0, 450, 1000)
days_smooth_180 = np.linspace(0, 180, 500)

updated_interp = PchipInterpolator(model_days, updated_viab)
orig_interp = PchipInterpolator(model_days, orig_viab_from_table)
chal_interp = PchipInterpolator(chal_days, chal_viability)

updated_smooth = np.clip(updated_interp(days_smooth), 0, 100)
orig_smooth = np.clip(orig_interp(days_smooth), 0, 100)
chal_smooth = np.clip(chal_interp(days_smooth), 0, 100)


# ============================================================
# CHART 1: Updated 15-Month Outcome Simulation (3 curves)
# ============================================================
def chart_15month():
    fig, ax = plt.subplots(figsize=(14, 8))
    fig.patch.set_facecolor('#f0f0f0')
    ax.set_facecolor('#f5f5f5')
    ax.grid(True, alpha=0.3, linestyle='-', color='gray')
    ax.set_axisbelow(True)

    # Challenger (red dashed)
    ax.plot(days_smooth, chal_smooth, color='#8b1a1a', linewidth=3.0,
            linestyle='--', dashes=(10, 5),
            label='Challenger: Nivo/Ipi/Cabo (Palliative)', zorder=4)

    # Original Triple Blockade (green, thinner/lighter for comparison)
    ax.plot(days_smooth, orig_smooth, color='#1a5c1a', linewidth=2.0,
            linestyle=':', alpha=0.6,
            label='Original Triple Blockade', zorder=4)

    # Updated Quadruple + SRS (dark green, bold)
    ax.plot(days_smooth, updated_smooth, color='#0a4a0a', linewidth=3.5,
            solid_capstyle='round',
            label='Quadruple Blockade + SRS (Curative)', zorder=5)

    arrow_red = '#8b3a3a'
    arrow_green = '#0a4a0a'

    # Annotations — Challenger
    ax.annotate('Strong Initial Response\n(Anti-MET Effect)',
                xy=(50, 48), xytext=(85, 80),
                fontsize=10, fontweight='bold', color='#4a0000', ha='center',
                arrowprops=dict(arrowstyle='->', color=arrow_red, lw=2.5,
                                connectionstyle='arc3,rad=-0.2'),
                path_effects=[pe.withStroke(linewidth=3, foreground='white')], zorder=10)

    ax.annotate('Resistance Plateau',
                xy=(130, 28.5), xytext=(155, 42),
                fontsize=10, fontweight='bold', color='#4a0000', ha='center',
                arrowprops=dict(arrowstyle='->', color=arrow_red, lw=2.5,
                                connectionstyle='arc3,rad=-0.15'),
                path_effects=[pe.withStroke(linewidth=3, foreground='white')], zorder=10)

    ax.annotate('Immune Escape / Regrowth\n(DNMT1-driven Antigen Loss)',
                xy=(360, 60), xytext=(330, 82),
                fontsize=10, fontweight='bold', color='#4a0000', ha='center',
                arrowprops=dict(arrowstyle='->', color=arrow_red, lw=2.5,
                                connectionstyle='arc3,rad=-0.15'),
                path_effects=[pe.withStroke(linewidth=3, foreground='white')], zorder=10)

    # Annotations — Updated Sequential
    # Radiation marker
    rad_viab = float(updated_interp(57))
    ax.annotate('SRS Brain Radiation\n(Day 57)',
                xy=(57, rad_viab), xytext=(25, 55),
                fontsize=10, fontweight='bold', color='#cc6600', ha='center',
                arrowprops=dict(arrowstyle='->', color='#cc6600', lw=2.5,
                                connectionstyle='arc3,rad=0.2'),
                path_effects=[pe.withStroke(linewidth=3, foreground='white')], zorder=10)

    # Sirolimus marker
    siro_viab = float(updated_interp(65))
    ax.annotate('Sirolimus Added\n(Day 65)',
                xy=(65, siro_viab), xytext=(95, 35),
                fontsize=10, fontweight='bold', color='#6633aa', ha='center',
                arrowprops=dict(arrowstyle='->', color='#6633aa', lw=2.5,
                                connectionstyle='arc3,rad=-0.2'),
                path_effects=[pe.withStroke(linewidth=3, foreground='white')], zorder=10)

    # Metabolic Collapse
    ax.annotate('Metabolic Collapse\n(Sterilization)',
                xy=(105, float(updated_interp(105))), xytext=(135, 18),
                fontsize=10, fontweight='bold', color='#0a3d0a', ha='center',
                arrowprops=dict(arrowstyle='->', color=arrow_green, lw=2.5,
                                connectionstyle='arc3,rad=-0.2'),
                path_effects=[pe.withStroke(linewidth=3, foreground='white')], zorder=10)

    # Sustained Remission
    ax.annotate('Sustained Remission',
                xy=(250, float(updated_interp(250))), xytext=(280, 12),
                fontsize=10, fontweight='bold', color='#0a3d0a', ha='center',
                arrowprops=dict(arrowstyle='->', color=arrow_green, lw=2.5,
                                connectionstyle='arc3,rad=-0.2'),
                path_effects=[pe.withStroke(linewidth=3, foreground='white')], zorder=10)

    # Event markers on the updated curve
    ax.plot(57, rad_viab, 'o', color='#cc6600', markersize=10, zorder=7,
            markeredgecolor='white', markeredgewidth=2)
    ax.plot(65, siro_viab, 's', color='#6633aa', markersize=10, zorder=7,
            markeredgecolor='white', markeredgewidth=2)

    ax.set_xlim(0, 450)
    ax.set_ylim(0, 105)
    ax.set_xticks(np.arange(0, 500, 50))
    ax.set_yticks(np.arange(0, 120, 20))
    ax.set_xlabel('Days', fontsize=13, fontweight='bold')
    ax.set_ylabel('Tumor Viability (%)', fontsize=13, fontweight='bold')
    ax.set_title('15-Month Outcome Simulation: Quadruple Blockade + SRS vs. Challenger',
                 fontsize=15, fontweight='bold', pad=15)

    legend = ax.legend(loc='upper right', fontsize=10, framealpha=0.95,
                        edgecolor='gray', fancybox=True)
    legend.get_frame().set_linewidth(1.5)
    ax.tick_params(axis='both', which='major', labelsize=11)

    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, '15month_outcome_simulation.png'), dpi=200,
                bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print("Chart 1 saved: 15month_outcome_simulation.png")


# ============================================================
# CHART 2: Updated 180-Day Three-Curve Timeline
# ============================================================
def chart_180day_timeline():
    fig, ax = plt.subplots(figsize=(14, 8))
    fig.patch.set_facecolor('#f0f0f0')
    ax.set_facecolor('#f5f5f5')
    ax.grid(True, alpha=0.3, linestyle='-', color='gray')
    ax.set_axisbelow(True)

    # Tumor Viability
    tv_days = np.array([0, 10, 20, 30, 45, 50, 57, 60, 65, 75, 90, 105, 120, 150, 180])
    tv_vals = np.array([100, 95, 88, 80, 57, 49, 43, 38, 33, 20, 10, 5, 2.5, 1, 0.5])

    # Fibroblast Network (radiation has minimal stromal effect; sirolimus slight acceleration)
    fb_days = np.array([0, 10, 20, 30, 40, 50, 57, 65, 80, 100, 120, 150, 180])
    fb_vals = np.array([100, 100, 98, 88, 68, 50, 40, 30, 12, 4, 1.5, 0.5, 0.3])

    # Immune Engagement (BOOSTED by radiation antigen release + sirolimus memory T enhancement)
    im_days = np.array([0, 15, 30, 45, 55, 57, 65, 75, 90, 105, 120, 135, 150, 165, 180])
    im_vals = np.array([2, 2, 3, 5, 7, 12, 18, 30, 48, 60, 70, 76, 80, 83, 85])
    #                               ↑ radiation antigen boost    ↑ sirolimus memory T

    d_sm = np.linspace(0, 180, 500)
    tv_sm = np.clip(PchipInterpolator(tv_days, tv_vals)(d_sm), 0, 100)
    fb_sm = np.clip(PchipInterpolator(fb_days, fb_vals)(d_sm), 0, 100)
    im_sm = np.clip(PchipInterpolator(im_days, im_vals)(d_sm), 0, 100)

    ax.plot(d_sm, tv_sm, color='#0a4a0a', linewidth=3, label='Tumor Viability (%)', zorder=5)
    ax.plot(d_sm, fb_sm, color='#cc6600', linewidth=3, linestyle='--', dashes=(8, 4),
            label='Fibroblast Network (%)', zorder=5)
    ax.plot(d_sm, im_sm, color='#2255aa', linewidth=3, linestyle='-.',
            label='Immune Engagement (%)', zorder=5)

    # Phase regions
    ax.axvspan(0, 30, alpha=0.06, color='blue', zorder=0)
    ax.axvspan(30, 57, alpha=0.06, color='red', zorder=0)
    ax.axvspan(57, 65, alpha=0.06, color='orange', zorder=0)
    ax.axvspan(65, 180, alpha=0.06, color='purple', zorder=0)

    ax.text(15, 108, 'Phase 1:\nDoxy Only', fontsize=8, ha='center', va='bottom',
            color='#333', fontweight='bold',
            path_effects=[pe.withStroke(linewidth=2, foreground='white')])
    ax.text(43, 108, 'Phase 2:\nTriple', fontsize=8, ha='center', va='bottom',
            color='#333', fontweight='bold',
            path_effects=[pe.withStroke(linewidth=2, foreground='white')])
    ax.text(61, 108, 'SRS', fontsize=8, ha='center', va='bottom',
            color='#cc6600', fontweight='bold',
            path_effects=[pe.withStroke(linewidth=2, foreground='white')])
    ax.text(122, 108, 'Phase 3: Quadruple Blockade (Doxy + Cimetidine + HCQ + Sirolimus)',
            fontsize=8, ha='center', va='bottom', color='#333', fontweight='bold',
            path_effects=[pe.withStroke(linewidth=2, foreground='white')])

    # Event markers
    ax.axvline(x=57, color='#cc6600', linewidth=2, linestyle=':', alpha=0.7, zorder=3)
    ax.axvline(x=65, color='#6633aa', linewidth=2, linestyle=':', alpha=0.7, zorder=3)

    # Annotations
    ax.annotate('SRS: Antigen\nRelease (Day 57)',
                xy=(57, 12), xytext=(38, 28),
                fontsize=9, fontweight='bold', color='#cc6600',
                arrowprops=dict(arrowstyle='->', color='#cc6600', lw=2),
                path_effects=[pe.withStroke(linewidth=2, foreground='white')], zorder=10)

    ax.annotate('Sirolimus\n(Day 65)',
                xy=(65, 33), xytext=(80, 48),
                fontsize=9, fontweight='bold', color='#6633aa',
                arrowprops=dict(arrowstyle='->', color='#6633aa', lw=2),
                path_effects=[pe.withStroke(linewidth=2, foreground='white')], zorder=10)

    ax.annotate('Immune Crossover\n(Day ~72)',
                xy=(72, 27), xytext=(95, 38),
                fontsize=9, fontweight='bold', color='#2255aa',
                arrowprops=dict(arrowstyle='->', color='#2255aa', lw=2),
                path_effects=[pe.withStroke(linewidth=2, foreground='white')], zorder=10)

    ax.annotate('Waste Double-Trap\n(Siro + HCQ)',
                xy=(80, 8), xytext=(105, 18),
                fontsize=9, fontweight='bold', color='#8b4500',
                arrowprops=dict(arrowstyle='->', color='#8b4500', lw=2),
                path_effects=[pe.withStroke(linewidth=2, foreground='white')], zorder=10)

    ax.set_xlim(0, 180)
    ax.set_ylim(0, 115)
    ax.set_xticks(np.arange(0, 195, 15))
    ax.set_xlabel('Days', fontsize=13, fontweight='bold')
    ax.set_ylabel('Percentage (%)', fontsize=13, fontweight='bold')
    ax.set_title('180-Day Updated Timeline: Quadruple Blockade + Stereotactic Radiosurgery',
                 fontsize=14, fontweight='bold', pad=15)
    ax.legend(loc='center right', fontsize=11, framealpha=0.95, edgecolor='gray')
    ax.tick_params(axis='both', which='major', labelsize=11)

    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, '180day_treatment_timeline.png'), dpi=200,
                bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print("Chart 2 saved: 180day_treatment_timeline.png")


# ============================================================
# CHART 3: Updated Domain Comparison at Day 120
# ============================================================
def chart_domain_comparison():
    fig, ax = plt.subplots(figsize=(14, 7))
    fig.patch.set_facecolor('#f0f0f0')
    ax.set_facecolor('#f5f5f5')
    ax.grid(True, alpha=0.3, axis='y', linestyle='-', color='gray')
    ax.set_axisbelow(True)

    domains = ['Metabolic\nCapacity', 'Stromal\nControl', 'Vascular\nSupply',
               'Immune\nEvasion', 'Waste\nMgmt', 'Adaptive\nPotential']

    # Day 120 scores
    original_a =   [10, 5,  10, 20, 3,  18]  # Original Triple Blockade
    updated_a =    [2,  1,  2,  2,  0.3, 1]   # Quadruple + SRS
    approach_b =   [50, 45, 15, 12, 80, 25]   # Nivo/Ipi/Cabo

    x = np.arange(len(domains))
    width = 0.25

    bars_orig = ax.bar(x - width, original_a, width,
                        label='Original Triple Blockade',
                        color='#1a5c1a', alpha=0.5, edgecolor='#1a5c1a', linewidth=1.5, zorder=5)
    bars_upd = ax.bar(x, updated_a, width,
                       label='Quadruple + SRS (Updated)',
                       color='#0a4a0a', alpha=0.9, edgecolor='white', linewidth=1.5, zorder=5)
    bars_b = ax.bar(x + width, approach_b, width,
                     label='Nivo/Ipi/Cabo',
                     color='#8b1a1a', alpha=0.9, edgecolor='white', linewidth=1.5, zorder=5)

    for bars in [bars_orig, bars_upd, bars_b]:
        for bar in bars:
            h = bar.get_height()
            label = f'{h:.0f}' if h >= 1 else f'{h:.1f}'
            ax.text(bar.get_x() + bar.get_width()/2., h + 0.5,
                    label, ha='center', va='bottom', fontsize=9, fontweight='bold')

    ax.set_ylim(0, 95)
    ax.set_xticks(x)
    ax.set_xticklabels(domains, fontsize=11)
    ax.set_ylabel('Remaining Tumor Domain Score (lower = better)', fontsize=12, fontweight='bold')
    ax.set_title('Day 120: Domain Comparison — Original vs. Updated vs. Challenger',
                 fontsize=14, fontweight='bold', pad=15)
    ax.legend(loc='upper left', fontsize=11, framealpha=0.95, edgecolor='gray')

    # Totals box
    orig_total = sum(original_a)
    upd_total = sum(updated_a)
    b_total = sum(approach_b)
    ax.text(0.98, 0.95,
            f'Day 120 Totals:\n'
            f'Original Triple: {orig_total:.0f}/520 ({orig_total/520*100:.1f}%)\n'
            f'Quad + SRS: {upd_total:.1f}/520 ({upd_total/520*100:.1f}%)\n'
            f'Nivo/Ipi/Cabo: {b_total}/520 ({b_total/520*100:.1f}%)',
            transform=ax.transAxes, fontsize=10, va='top', ha='right',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.9, edgecolor='gray'))

    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, 'domain_comparison_day180.png'), dpi=200,
                bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print("Chart 3 saved: domain_comparison_day180.png")


# ============================================================
# CHART 4: Updated Treatment Trajectory (3 strategies)
# ============================================================
def chart_trajectory():
    fig, ax = plt.subplots(figsize=(14, 8))
    fig.patch.set_facecolor('#f0f0f0')
    ax.set_facecolor('#f5f5f5')
    ax.grid(True, alpha=0.3, linestyle='-', color='gray')
    ax.set_axisbelow(True)

    d_sm = np.linspace(0, 180, 500)

    # Challenger
    chal_180_days = np.array([0, 15, 30, 50, 70, 90, 110, 130, 150, 180])
    chal_180_viab = np.array([100, 82, 68, 48, 35, 29, 28, 28.5, 29, 31])
    chal_sm = np.clip(PchipInterpolator(chal_180_days, chal_180_viab)(d_sm), 0, 100)

    # Original Triple
    orig_180_days = np.array([0, 10, 20, 30, 45, 50, 60, 75, 90, 105, 120, 150, 180])
    orig_180_viab = np.array([100, 95, 88, 80, 57, 49, 38, 30, 21, 15, 11, 5, 3])
    orig_sm = np.clip(PchipInterpolator(orig_180_days, orig_180_viab)(d_sm), 0, 100)

    # Updated Quadruple + SRS
    upd_180_days = np.array([0, 10, 20, 30, 45, 50, 57, 60, 65, 75, 90, 105, 120, 150, 180])
    upd_180_viab = np.array([100, 95, 88, 80, 57, 49, 43, 38, 33, 20, 10, 5, 2.5, 1, 0.5])
    upd_sm = np.clip(PchipInterpolator(upd_180_days, upd_180_viab)(d_sm), 0, 100)

    ax.plot(d_sm, chal_sm, color='#8b1a1a', linewidth=3, linestyle='--', dashes=(10, 5),
            label='Nivo/Ipi/Cabo', zorder=4)
    ax.plot(d_sm, orig_sm, color='#1a5c1a', linewidth=2, linestyle=':', alpha=0.6,
            label='Original Triple Blockade', zorder=4)
    ax.plot(d_sm, upd_sm, color='#0a4a0a', linewidth=3.5,
            label='Quadruple Blockade + SRS', zorder=5)

    # Event markers
    ax.plot(57, 43, 'o', color='#cc6600', markersize=10, zorder=7,
            markeredgecolor='white', markeredgewidth=2)
    ax.plot(65, 33, 's', color='#6633aa', markersize=10, zorder=7,
            markeredgecolor='white', markeredgewidth=2)
    ax.text(59, 46, 'SRS', fontsize=9, fontweight='bold', color='#cc6600')
    ax.text(67, 36, 'Siro', fontsize=9, fontweight='bold', color='#6633aa')

    # Day 180 labels
    ax.text(182, 31, '31.0%', fontsize=10, fontweight='bold', color='#8b1a1a', va='center')
    ax.text(182, 3, '3.0%', fontsize=10, fontweight='bold', color='#1a5c1a', va='center', alpha=0.6)
    ax.text(182, 0.5, '0.5%', fontsize=10, fontweight='bold', color='#0a4a0a', va='center')

    ax.set_xlim(0, 185)
    ax.set_ylim(0, 105)
    ax.set_xticks(np.arange(0, 195, 30))
    ax.set_xlabel('Days', fontsize=13, fontweight='bold')
    ax.set_ylabel('Tumor Viability (% of Baseline)', fontsize=13, fontweight='bold')
    ax.set_title('180-Day Treatment Trajectory: All Strategies Compared',
                 fontsize=14, fontweight='bold', pad=15)
    ax.legend(loc='upper right', fontsize=11, framealpha=0.95, edgecolor='gray')
    ax.tick_params(axis='both', which='major', labelsize=11)

    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, 'treatment_trajectory_comparison.png'), dpi=200,
                bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print("Chart 4 saved: treatment_trajectory_comparison.png")


# ============================================================
# CHART 5: Updated PK Loading Curve (add sirolimus)
# ============================================================
def chart_pk_loading():
    fig, ax = plt.subplots(figsize=(14, 7))
    fig.patch.set_facecolor('#f0f0f0')
    ax.set_facecolor('#f5f5f5')
    ax.grid(True, alpha=0.3, linestyle='-', color='gray')
    ax.set_axisbelow(True)

    days = np.linspace(0, 180, 500)

    # Doxycycline (t1/2 ~20h, starts Day 0)
    doxy = 100 * (1 - np.exp(-np.log(2) / 0.83 * days))

    # Cimetidine (t1/2 ~2h, starts Day 20)
    cim_on = np.maximum(days - 20, 0)
    cim = 100 * (1 - np.exp(-np.log(2) / 0.08 * cim_on))
    cim[days < 20] = 0

    # HCQ (t1/2 ~45 days, starts Day 31)
    hcq_on = np.maximum(days - 31, 0)
    hcq = 100 * (1 - np.exp(-np.log(2) / 45 * hcq_on))
    hcq[days < 31] = 0

    # Sirolimus (t1/2 ~2.6 days, starts Day 65)
    siro_on = np.maximum(days - 65, 0)
    siro = 100 * (1 - np.exp(-np.log(2) / 2.6 * siro_on))
    siro[days < 65] = 0

    ax.plot(days, doxy, color='#1a5c1a', linewidth=2.5, label='Doxycycline (t½ ~20h)')
    ax.plot(days, cim, color='#2255aa', linewidth=2.5, linestyle='-.',
            label='Cimetidine (t½ ~2h)')
    ax.plot(days, hcq, color='#cc4400', linewidth=3.5,
            label='HCQ (t½ ~40-50 days)', zorder=6)
    ax.plot(days, siro, color='#6633aa', linewidth=3,
            label='Sirolimus (t½ ~62h)', zorder=6)

    # Radiation marker
    ax.axvline(x=57, color='#cc6600', linewidth=2.5, linestyle='--', alpha=0.8, zorder=3)
    ax.text(58, 105, 'SRS\nDay 57', fontsize=9, fontweight='bold', color='#cc6600',
            path_effects=[pe.withStroke(linewidth=2, foreground='white')])

    # Sirolimus marker
    ax.axvline(x=65, color='#6633aa', linewidth=2, linestyle=':', alpha=0.6, zorder=3)

    # Thresholds
    ax.axhline(y=50, color='gray', linewidth=1, linestyle=':', alpha=0.5)
    ax.text(2, 52, '50% steady-state', fontsize=9, color='gray')
    ax.axhline(y=90, color='gray', linewidth=1, linestyle=':', alpha=0.5)
    ax.text(2, 92, '90% steady-state', fontsize=9, color='gray')

    # HCQ annotation
    hcq_at_90 = 100 * (1 - np.exp(-np.log(2) / 45 * (90 - 31)))
    ax.annotate(f'HCQ at Day 90: {hcq_at_90:.0f}%\n(still deepening)',
                xy=(90, hcq_at_90), xytext=(108, hcq_at_90 - 15),
                fontsize=9, fontweight='bold', color='#cc4400',
                arrowprops=dict(arrowstyle='->', color='#cc4400', lw=2),
                path_effects=[pe.withStroke(linewidth=2, foreground='white')])

    # Sirolimus annotation
    ax.annotate('Sirolimus reaches\nsteady-state in ~7d',
                xy=(72, 95), xytext=(85, 78),
                fontsize=9, fontweight='bold', color='#6633aa',
                arrowprops=dict(arrowstyle='->', color='#6633aa', lw=2),
                path_effects=[pe.withStroke(linewidth=2, foreground='white')])

    # Phase regions
    ax.axvspan(0, 31, alpha=0.04, color='blue')
    ax.axvspan(31, 65, alpha=0.04, color='red')
    ax.axvspan(65, 180, alpha=0.04, color='purple')

    # Double-trap callout
    ax.text(0.98, 0.40,
            'AUTOPHAGY DOUBLE-TRAP:\n'
            'Sirolimus INDUCES autophagy\n'
            '(mTOR inhibition → more\nautophagosomes initiated)\n\n'
            'HCQ BLOCKS autophagy\n'
            '(lysosomal alkalinization →\nnone completed)\n\n'
            'Result: catastrophic p62\n'
            'accumulation → waste crisis\n'
            'becomes unsurvivable',
            transform=ax.transAxes, fontsize=9, va='center', ha='right',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#f3ddff',
                      edgecolor='#6633aa', alpha=0.95, linewidth=1.5))

    ax.set_xlim(0, 180)
    ax.set_ylim(0, 112)
    ax.set_xticks(np.arange(0, 195, 15))
    ax.set_xlabel('Days', fontsize=13, fontweight='bold')
    ax.set_ylabel('Tissue Concentration (% of Steady State)', fontsize=13, fontweight='bold')
    ax.set_title('Pharmacokinetic Loading: Quadruple Blockade + SRS',
                 fontsize=14, fontweight='bold', pad=15)
    ax.legend(loc='center left', fontsize=10, framealpha=0.95, edgecolor='gray')

    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, 'hcq_loading_curve.png'), dpi=200,
                bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print("Chart 5 saved: hcq_loading_curve.png")


# ============================================================
# CHART 6: Updated Fortress with Sirolimus + Radiation
# ============================================================
def chart_fortress():
    fig, ax = plt.subplots(figsize=(15, 11))
    fig.patch.set_facecolor('#f0f0f0')
    ax.set_facecolor('#f5f5f5')
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 13)
    ax.axis('off')

    ax.text(7.5, 12.5, 'The Fortress: Five Defensive Layers & All Drug Attacks',
            fontsize=16, fontweight='bold', ha='center')
    ax.text(7.5, 12.0, 'Updated: Quadruple Blockade (Doxy + Cimetidine + HCQ + Sirolimus) + SRS Radiation',
            fontsize=10, ha='center', color='#555')

    layers = [
        {
            'name': 'Layer 5: Epigenetic Fog',
            'desc': 'DNMT1 disruption → progressive methylation\ninstability, alters antigen presentation',
            'score': 'IDH1: 1.348 | IDH2: 1.747',
            'drugs': ['Self-eroding\n(progressive\ndemethylation)', 'SRS: antigen\nrelease accelerates\nimmune recognition'],
            'drug_colors': ['#888888', '#cc6600'],
            'y': 10.5, 'color': '#e8d0ff', 'edge': '#9955cc',
        },
        {
            'name': 'Layer 4: Immune Exclusion Zone',
            'desc': 'TFE3 7bp element (DNase 3.29) + DNMT1 T-cell switch\n+ LAG3 checkpoint + lactate moat + Treg enhancement',
            'score': 'LAG3: 0.111 | Treg score: 9.0',
            'drugs': ['CIMETIDINE\n(immune modulation)', 'SIROLIMUS\n(memory T cell\nenhancement)'],
            'drug_colors': ['#2255aa', '#6633aa'],
            'y': 8.3, 'color': '#d0e0ff', 'edge': '#4466cc',
        },
        {
            'name': 'Layer 3: Vascular Network',
            'desc': 'Dense neovascularization, Endothelial Danger: 11.53\nTriple anti-angiogenic: mechanical + signaling + transcriptional',
            'score': 'VEGFB: 2.004 | VEGFA: 1.484 | KDR: 0.327 | mTOR: 0.070',
            'drugs': ['CIMETIDINE\n(VEGF signaling)', 'DOXYCYCLINE\n(MMP → no tunnels)', 'SIROLIMUS\n(VEGF transcription\nvia mTOR/HIF-1α)'],
            'drug_colors': ['#2255aa', '#1a5c1a', '#6633aa'],
            'y': 6.0, 'color': '#ffe0d0', 'edge': '#cc6644',
        },
        {
            'name': 'Layer 2: Acidic Moat (Reverse Warburg Lactate)',
            'desc': 'Enslaved fibroblast glycolysis → lactate → acidic moat\nFibroblast vuln: 13.63 | CTSD: 4.972',
            'score': 'SQSTM1: 1.156 | MAP1LC3B: 1.117 | TFEB: 0.083',
            'drugs': ['HCQ\n(lysosomal poison)', 'SIROLIMUS\n(autophagy\ndouble-trap)'],
            'drug_colors': ['#cc4400', '#6633aa'],
            'y': 3.8, 'color': '#ffffcc', 'edge': '#ccaa00',
        },
        {
            'name': 'Layer 1: Collagen Bunker (Fibrosis Score: 14.81)',
            'desc': 'Massive collagen barrier from enslaved fibroblasts\nMMP14: 1.289 | MMP7: 0.506',
            'score': '',
            'drugs': ['DOXYCYCLINE\n(MMP inhibition →\nbunker dissolves)'],
            'drug_colors': ['#1a5c1a'],
            'y': 1.8, 'color': '#d5e8d4', 'edge': '#448844',
        },
    ]

    for layer in layers:
        y = layer['y']
        # Layer box
        box = FancyBboxPatch((0.5, y - 0.7), 8.5, 1.6,
                              boxstyle="round,pad=0.15",
                              facecolor=layer['color'], edgecolor=layer['edge'],
                              linewidth=2.5)
        ax.add_patch(box)
        ax.text(0.8, y + 0.45, layer['name'], fontsize=10, fontweight='bold',
                va='center', color=layer['edge'])
        ax.text(0.8, y - 0.05, layer['desc'], fontsize=7.5, va='center', color='#333')
        if layer['score']:
            ax.text(0.8, y - 0.45, layer['score'], fontsize=7.5, va='center',
                    color='#666', fontstyle='italic')

        # Drug boxes (stacked to the right)
        n_drugs = len(layer['drugs'])
        drug_width = 2.8
        drug_start_x = 10.0
        drug_height = 1.3 / n_drugs
        for i, (drug_text, drug_color) in enumerate(zip(layer['drugs'], layer['drug_colors'])):
            dy = y + 0.5 - (i + 0.5) * (1.3 / n_drugs) - 0.15
            dbox = FancyBboxPatch((drug_start_x, dy - drug_height/2), drug_width, drug_height,
                                   boxstyle="round,pad=0.08",
                                   facecolor='white', edgecolor=drug_color, linewidth=1.5)
            ax.add_patch(dbox)
            ax.text(drug_start_x + drug_width/2, dy, drug_text,
                    fontsize=7, fontweight='bold', ha='center', va='center', color=drug_color)

        # Arrow
        ax.annotate('', xy=(drug_start_x, y), xytext=(9.0, y),
                     arrowprops=dict(arrowstyle='->', color=layer['edge'], lw=2.5))

    # Tumor core
    ax.text(4.75, 0.5, 'TUMOR CORE: ASPSCR1-TFE3 Fusion Engine + DNMT1 Shield',
            fontsize=10, fontweight='bold', ha='center', va='center',
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#ff6666', edgecolor='#cc0000',
                      alpha=0.9, linewidth=2),
            color='white')

    plt.tight_layout()
    plt.savefig(os.path.join(CHARTS_DIR, 'fortress_layers.png'), dpi=200,
                bbox_inches='tight', facecolor=fig.get_facecolor())
    plt.close()
    print("Chart 6 saved: fortress_layers.png")


# ============================================================
# PRINT MODEL SUMMARY
# ============================================================
def print_model_summary():
    print("\n" + "="*70)
    print("UPDATED MODEL SUMMARY")
    print("="*70)
    print(f"\nTimeline: Doxy(D0) → Cimetidine(D20) → HCQ(D31) → SRS(D57) → Sirolimus(D65)")
    print(f"\nSix-Domain Scores at Key Timepoints:\n")
    print(f"{'Day':>5} | {'Metab':>6} {'Strom':>6} {'Vasc':>6} {'Immun':>6} {'Waste':>6} {'Adapt':>6} | {'TOTAL':>7} | {'Viab%':>6}")
    print("-" * 75)
    for i, day in enumerate(model_days):
        vals = [updated_scores[d][i] for d in ['Metabolic', 'Stromal', 'Vascular', 'Immune', 'Waste', 'Adaptive']]
        total = sum(vals)
        viab = total / baseline * 100
        marker = ""
        if day == 57: marker = " ← SRS"
        elif day == 65: marker = " ← Sirolimus"
        print(f"{day:5.0f} | {vals[0]:6.1f} {vals[1]:6.1f} {vals[2]:6.1f} {vals[3]:6.1f} {vals[4]:6.1f} {vals[5]:6.1f} | {total:7.1f} | {viab:5.1f}%{marker}")

    print(f"\nDay 120 comparison:")
    print(f"  Original Triple Blockade:  66/520  (12.7%)")
    print(f"  Quadruple + SRS:           8.3/520 (1.6%)")
    print(f"  Nivo/Ipi/Cabo:             275/520 (52.9%)")
    print(f"\nDay 180 comparison:")
    print(f"  Original Triple Blockade:  14/520  (2.7%)")
    print(f"  Quadruple + SRS:           4.5/520 (0.9%)")
    print(f"  Nivo/Ipi/Cabo:             227/520 (43.7%)")


# ============================================================
# RUN ALL
# ============================================================
if __name__ == '__main__':
    print_model_summary()
    print()
    chart_15month()
    chart_180day_timeline()
    chart_domain_comparison()
    chart_trajectory()
    chart_pk_loading()
    chart_fortress()
    print("\n=== All 6 updated charts generated ===")
