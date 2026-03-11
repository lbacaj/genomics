#!/usr/bin/env python3
"""
15-Month Outcome Simulation: Sequential Strategy vs. Challenger Strategy
Based on AlphaGenome analysis data from Queries 5-9
Patient: Johnny | ASPS | March 2026
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch
import matplotlib.patheffects as pe

# ============================================================
# DATA: Derived from Query 5 (War Game), Query 7 (Timeline),
#        and Query 9 (Treatment Comparison)
# ============================================================

# --- Sequential Strategy (Curative): Triple Blockade ---
# Phase 1: Doxy alone (Days 0-30), Phase 2: Triple Blockade (31+)
# Data points from Query 7 tumor viability curve + Query 9 Approach A
seq_days = np.array([0, 10, 20, 30, 45, 50, 60, 75, 90, 105, 120, 150, 180, 240, 300, 360, 450])
seq_viability = np.array([100, 95, 88, 80, 57, 49, 38, 30, 21, 15, 11, 5, 3, 1.5, 1, 0.5, 0.3])

# --- Challenger: Nivo/Ipi/Cabo (Palliative) ---
# Strong initial response (anti-MET/anti-VEGFR2 effect from cabozantinib)
# then resistance plateau, then immune escape / regrowth (DNMT1-driven antigen loss)
# Data from Query 9 Approach B + biological escape modeling
chal_days = np.array([0, 15, 30, 50, 70, 90, 110, 130, 150, 180, 210, 250, 290, 330, 370, 410, 450])
chal_viability = np.array([100, 82, 68, 48, 35, 29, 28, 28.5, 29, 31, 35, 40, 48, 56, 63, 70, 78])

# ============================================================
# SMOOTH INTERPOLATION
# ============================================================
from scipy.interpolate import PchipInterpolator

days_smooth = np.linspace(0, 450, 1000)
seq_interp = PchipInterpolator(seq_days, seq_viability)
chal_interp = PchipInterpolator(chal_days, chal_viability)

seq_smooth = np.clip(seq_interp(days_smooth), 0, 100)
chal_smooth = np.clip(chal_interp(days_smooth), 0, 100)

# ============================================================
# CHART CREATION
# ============================================================
fig, ax = plt.subplots(figsize=(14, 8))

# Background styling
fig.patch.set_facecolor('#f0f0f0')
ax.set_facecolor('#f5f5f5')

# Grid
ax.grid(True, alpha=0.3, linestyle='-', color='gray')
ax.set_axisbelow(True)

# Plot curves
line_seq, = ax.plot(days_smooth, seq_smooth, color='#1a5c1a', linewidth=3.0,
                     solid_capstyle='round', label='Sequential Strategy (Curative)',
                     zorder=5)
line_chal, = ax.plot(days_smooth, chal_smooth, color='#8b1a1a', linewidth=3.0,
                      linestyle='--', dashes=(10, 5),
                      label='Challenger: Nivo/Ipi/Cabo (Palliative)',
                      zorder=5)

# ============================================================
# ANNOTATIONS with arrows
# ============================================================
arrow_color_red = '#8b3a3a'
arrow_color_green = '#1a5c1a'

# Annotation style
ann_kwargs = dict(fontsize=10, fontweight='bold', ha='center',
                  path_effects=[pe.withStroke(linewidth=3, foreground='white')])

# 1. "Strong Initial Response (Anti-MET Effect)" - on red curve ~day 50
ax.annotate('Strong Initial Response\n(Anti-MET Effect)',
            xy=(50, 48), xytext=(85, 78),
            fontsize=10, fontweight='bold', color='#4a0000',
            ha='center',
            arrowprops=dict(arrowstyle='->', color=arrow_color_red, lw=2.5,
                            connectionstyle='arc3,rad=-0.2'),
            path_effects=[pe.withStroke(linewidth=3, foreground='white')],
            zorder=10)

# 2. "Resistance Plateau" - on red curve ~day 120
ax.annotate('Resistance Plateau',
            xy=(130, 28.5), xytext=(155, 42),
            fontsize=10, fontweight='bold', color='#4a0000',
            ha='center',
            arrowprops=dict(arrowstyle='->', color=arrow_color_red, lw=2.5,
                            connectionstyle='arc3,rad=-0.15'),
            path_effects=[pe.withStroke(linewidth=3, foreground='white')],
            zorder=10)

# 3. "Immune Escape / Regrowth (DNMT1-driven Antigen Loss)" - on red curve ~day 350
ax.annotate('Immune Escape / Regrowth\n(DNMT1-driven Antigen Loss)',
            xy=(360, 60), xytext=(330, 82),
            fontsize=10, fontweight='bold', color='#4a0000',
            ha='center',
            arrowprops=dict(arrowstyle='->', color=arrow_color_red, lw=2.5,
                            connectionstyle='arc3,rad=-0.15'),
            path_effects=[pe.withStroke(linewidth=3, foreground='white')],
            zorder=10)

# 4. "Metabolic Collapse (Sterilization)" - on green curve ~day 120
ax.annotate('Metabolic Collapse\n(Sterilization)',
            xy=(120, 11), xytext=(135, 22),
            fontsize=10, fontweight='bold', color='#0a3d0a',
            ha='center',
            arrowprops=dict(arrowstyle='->', color=arrow_color_green, lw=2.5,
                            connectionstyle='arc3,rad=-0.2'),
            path_effects=[pe.withStroke(linewidth=3, foreground='white')],
            zorder=10)

# 5. "Sustained Remission" - on green curve ~day 300
ax.annotate('Sustained Remission',
            xy=(300, 1), xytext=(330, 12),
            fontsize=10, fontweight='bold', color='#0a3d0a',
            ha='center',
            arrowprops=dict(arrowstyle='->', color=arrow_color_green, lw=2.5,
                            connectionstyle='arc3,rad=-0.2'),
            path_effects=[pe.withStroke(linewidth=3, foreground='white')],
            zorder=10)

# ============================================================
# AXES AND LABELS
# ============================================================
ax.set_xlim(0, 450)
ax.set_ylim(0, 105)
ax.set_xticks(np.arange(0, 500, 50))
ax.set_yticks(np.arange(0, 120, 20))

ax.set_xlabel('Days', fontsize=13, fontweight='bold')
ax.set_ylabel('Tumor Viability (%)', fontsize=13, fontweight='bold')
ax.set_title('15-Month Outcome Simulation: Sequential vs. Challenger Strategy',
             fontsize=15, fontweight='bold', pad=15)

# Legend
legend = ax.legend(loc='upper right', fontsize=11, framealpha=0.95,
                    edgecolor='gray', fancybox=True)
legend.get_frame().set_linewidth(1.5)

# Minor ticks
ax.minorticks_on()
ax.tick_params(axis='both', which='major', labelsize=11)

plt.tight_layout()
plt.savefig('/Users/lbacaj/genomics/15month_outcome_simulation.png', dpi=200,
            bbox_inches='tight', facecolor=fig.get_facecolor())
plt.close()
print("Chart saved: 15month_outcome_simulation.png")


# ============================================================
# CHART 2: Three-Curve Timeline (Tumor + Fibroblast + Immune)
# From Query 7 data
# ============================================================
fig2, ax2 = plt.subplots(figsize=(14, 8))
fig2.patch.set_facecolor('#f0f0f0')
ax2.set_facecolor('#f5f5f5')
ax2.grid(True, alpha=0.3, linestyle='-', color='gray')
ax2.set_axisbelow(True)

# Tumor Viability (same as sequential above, 180 days)
tv_days = np.array([0, 10, 20, 30, 45, 50, 60, 75, 90, 105, 120, 150, 180])
tv_vals = np.array([100, 95, 88, 80, 57, 49, 38, 30, 21, 15, 11, 5, 3])

# Fibroblast Network (from Query 7 fibroblast melting curve)
fb_days = np.array([0, 10, 20, 30, 40, 50, 65, 80, 100, 120, 150, 180])
fb_vals = np.array([100, 100, 98, 88, 68, 50, 28, 15, 5, 2, 1, 0.5])

# Immune Engagement (from Query 7 immune curve)
im_days = np.array([0, 15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180])
im_vals = np.array([2, 2, 3, 5, 8, 12, 20, 30, 40, 50, 58, 65, 70])

days_sm2 = np.linspace(0, 180, 500)

tv_interp = PchipInterpolator(tv_days, tv_vals)
fb_interp = PchipInterpolator(fb_days, fb_vals)
im_interp = PchipInterpolator(im_days, im_vals)

tv_sm = np.clip(tv_interp(days_sm2), 0, 100)
fb_sm = np.clip(fb_interp(days_sm2), 0, 100)
im_sm = np.clip(im_interp(days_sm2), 0, 100)

ax2.plot(days_sm2, tv_sm, color='#1a5c1a', linewidth=3, label='Tumor Viability (%)', zorder=5)
ax2.plot(days_sm2, fb_sm, color='#cc6600', linewidth=3, linestyle='--', dashes=(8, 4),
         label='Fibroblast Network (%)', zorder=5)
ax2.plot(days_sm2, im_sm, color='#2255aa', linewidth=3, linestyle='-.',
         label='Immune Engagement (%)', zorder=5)

# Phase regions
ax2.axvspan(0, 30, alpha=0.06, color='blue', zorder=0)
ax2.axvspan(30, 180, alpha=0.06, color='red', zorder=0)
ax2.text(15, 103, 'Phase 1:\nDoxy Only', fontsize=9, ha='center', va='bottom',
         color='#333333', fontweight='bold',
         path_effects=[pe.withStroke(linewidth=2, foreground='white')])
ax2.text(105, 103, 'Phase 2: Triple Blockade (Doxy + Cimetidine + HCQ)',
         fontsize=9, ha='center', va='bottom', color='#333333', fontweight='bold',
         path_effects=[pe.withStroke(linewidth=2, foreground='white')])

# Key inflection annotations
ax2.annotate('HCQ Entry\n(Day 31)',
             xy=(31, 78), xytext=(55, 95),
             fontsize=9, fontweight='bold', color='#8b0000',
             arrowprops=dict(arrowstyle='->', color='#8b0000', lw=2),
             path_effects=[pe.withStroke(linewidth=2, foreground='white')], zorder=10)

ax2.annotate('Waste Tipping\nPoint (Day 50)',
             xy=(50, 49), xytext=(75, 62),
             fontsize=9, fontweight='bold', color='#8b4500',
             arrowprops=dict(arrowstyle='->', color='#8b4500', lw=2),
             path_effects=[pe.withStroke(linewidth=2, foreground='white')], zorder=10)

ax2.annotate('Reverse Warburg\nCollapse (Day 70)',
             xy=(70, 33), xytext=(95, 45),
             fontsize=9, fontweight='bold', color='#cc6600',
             arrowprops=dict(arrowstyle='->', color='#cc6600', lw=2),
             path_effects=[pe.withStroke(linewidth=2, foreground='white')], zorder=10)

ax2.annotate('Immune\nCrossover',
             xy=(115, 37), xytext=(135, 52),
             fontsize=9, fontweight='bold', color='#2255aa',
             arrowprops=dict(arrowstyle='->', color='#2255aa', lw=2),
             path_effects=[pe.withStroke(linewidth=2, foreground='white')], zorder=10)

ax2.set_xlim(0, 180)
ax2.set_ylim(0, 110)
ax2.set_xticks(np.arange(0, 195, 15))
ax2.set_yticks(np.arange(0, 120, 20))
ax2.set_xlabel('Days', fontsize=13, fontweight='bold')
ax2.set_ylabel('Percentage (%)', fontsize=13, fontweight='bold')
ax2.set_title('180-Day Treatment Timeline: Tumor Viability, Fibroblast Network & Immune Engagement',
              fontsize=14, fontweight='bold', pad=15)
legend2 = ax2.legend(loc='upper right', fontsize=11, framealpha=0.95,
                      edgecolor='gray', fancybox=True)
legend2.get_frame().set_linewidth(1.5)
ax2.tick_params(axis='both', which='major', labelsize=11)

plt.tight_layout()
plt.savefig('/Users/lbacaj/genomics/180day_treatment_timeline.png', dpi=200,
            bbox_inches='tight', facecolor=fig2.get_facecolor())
plt.close()
print("Chart saved: 180day_treatment_timeline.png")


# ============================================================
# CHART 3: Six-Domain Stacked/Grouped Bar Chart
# Approach A vs B vs Hybrid at Day 180
# From Query 9 data
# ============================================================
fig3, ax3 = plt.subplots(figsize=(14, 7))
fig3.patch.set_facecolor('#f0f0f0')
ax3.set_facecolor('#f5f5f5')
ax3.grid(True, alpha=0.3, axis='y', linestyle='-', color='gray')
ax3.set_axisbelow(True)

domains = ['Metabolic\nCapacity', 'Stromal\nControl', 'Vascular\nSupply',
           'Immune\nEvasion', 'Waste\nMgmt', 'Adaptive\nPotential']

# Day 180 scores from Query 9
approach_a = [2, 1, 2, 3, 1, 5]      # Triple Blockade
approach_b = [50, 45, 15, 12, 80, 25] # Nivo/Ipi/Cabo
hybrid     = [2, 1, 2, 1, 1, 3]      # Hybrid (A + anti-LAG3)

x = np.arange(len(domains))
width = 0.25

bars_a = ax3.bar(x - width, approach_a, width, label='Approach A: Triple Blockade',
                  color='#1a5c1a', alpha=0.9, edgecolor='white', linewidth=1.5, zorder=5)
bars_b = ax3.bar(x, approach_b, width, label='Approach B: Nivo/Ipi/Cabo',
                  color='#8b1a1a', alpha=0.9, edgecolor='white', linewidth=1.5, zorder=5)
bars_h = ax3.bar(x + width, hybrid, width, label='Hybrid: A + Anti-LAG3',
                  color='#2255aa', alpha=0.9, edgecolor='white', linewidth=1.5, zorder=5)

# Value labels on bars
for bars in [bars_a, bars_b, bars_h]:
    for bar in bars:
        height = bar.get_height()
        ax3.text(bar.get_x() + bar.get_width()/2., height + 1,
                 f'{int(height)}', ha='center', va='bottom', fontsize=9,
                 fontweight='bold')

ax3.set_ylim(0, 95)
ax3.set_xticks(x)
ax3.set_xticklabels(domains, fontsize=11)
ax3.set_ylabel('Remaining Tumor Domain Score (lower = better)', fontsize=12, fontweight='bold')
ax3.set_title('Day 180: Six-Domain Comparison — Triple Blockade vs. Nivo/Ipi/Cabo vs. Hybrid',
              fontsize=14, fontweight='bold', pad=15)
legend3 = ax3.legend(loc='upper left', fontsize=11, framealpha=0.95,
                      edgecolor='gray', fancybox=True)
legend3.get_frame().set_linewidth(1.5)

# Add total scores as text
ax3.text(0.98, 0.95, f'Day 180 Totals:\nTriple Blockade: 14/600 (2.3%)\n'
         f'Nivo/Ipi/Cabo: 227/600 (37.8%)\nHybrid: 10/600 (1.7%)',
         transform=ax3.transAxes, fontsize=10, va='top', ha='right',
         bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.9,
                   edgecolor='gray'))

plt.tight_layout()
plt.savefig('/Users/lbacaj/genomics/domain_comparison_day180.png', dpi=200,
            bbox_inches='tight', facecolor=fig3.get_facecolor())
plt.close()
print("Chart saved: domain_comparison_day180.png")


# ============================================================
# CHART 4: Treatment Trajectory Over Time (Both Approaches)
# Multi-timepoint domain totals from Query 9
# ============================================================
fig4, ax4 = plt.subplots(figsize=(14, 8))
fig4.patch.set_facecolor('#f0f0f0')
ax4.set_facecolor('#f5f5f5')
ax4.grid(True, alpha=0.3, linestyle='-', color='gray')
ax4.set_axisbelow(True)

# Domain totals over time from Query 9
traj_days = [0, 30, 90, 120, 180]
traj_a = [515, 466, 117, 56, 14]
traj_b = [515, 421, 321, 275, 227]
traj_h = [515, 466, 117, 48, 10]

# Normalize to percentage
traj_a_pct = [v/515*100 for v in traj_a]
traj_b_pct = [v/515*100 for v in traj_b]
traj_h_pct = [v/515*100 for v in traj_h]

traj_smooth = np.linspace(0, 180, 500)
ta_interp = PchipInterpolator(traj_days, traj_a_pct)
tb_interp = PchipInterpolator(traj_days, traj_b_pct)
th_interp = PchipInterpolator(traj_days, traj_h_pct)

ax4.plot(traj_smooth, np.clip(ta_interp(traj_smooth), 0, 100),
         color='#1a5c1a', linewidth=3, label='Triple Blockade (Approach A)', zorder=5)
ax4.plot(traj_smooth, np.clip(tb_interp(traj_smooth), 0, 100),
         color='#8b1a1a', linewidth=3, linestyle='--', dashes=(10, 5),
         label='Nivo/Ipi/Cabo (Approach B)', zorder=5)
ax4.plot(traj_smooth, np.clip(th_interp(traj_smooth), 0, 100),
         color='#2255aa', linewidth=3, linestyle='-.',
         label='Hybrid: A + Anti-LAG3', zorder=5)

# Data point markers
for days, vals, color in [(traj_days, traj_a_pct, '#1a5c1a'),
                           (traj_days, traj_b_pct, '#8b1a1a'),
                           (traj_days, traj_h_pct, '#2255aa')]:
    ax4.scatter(days, vals, color=color, s=60, zorder=6, edgecolors='white', linewidth=1.5)

ax4.set_xlim(0, 185)
ax4.set_ylim(0, 105)
ax4.set_xticks(np.arange(0, 195, 30))
ax4.set_yticks(np.arange(0, 120, 10))
ax4.set_xlabel('Days', fontsize=13, fontweight='bold')
ax4.set_ylabel('Total Tumor Score (% of Baseline)', fontsize=13, fontweight='bold')
ax4.set_title('180-Day Treatment Trajectory: All Three Strategies Compared',
              fontsize=14, fontweight='bold', pad=15)
legend4 = ax4.legend(loc='upper right', fontsize=11, framealpha=0.95,
                      edgecolor='gray', fancybox=True)
legend4.get_frame().set_linewidth(1.5)
ax4.tick_params(axis='both', which='major', labelsize=11)

# Score annotations at Day 180
ax4.text(183, traj_a_pct[-1] + 3, f'{traj_a_pct[-1]:.1f}%', fontsize=10,
         fontweight='bold', color='#1a5c1a', va='bottom')
ax4.text(183, traj_b_pct[-1] + 2, f'{traj_b_pct[-1]:.1f}%', fontsize=10,
         fontweight='bold', color='#8b1a1a', va='bottom')
ax4.text(183, traj_h_pct[-1] - 5, f'{traj_h_pct[-1]:.1f}%', fontsize=10,
         fontweight='bold', color='#2255aa', va='top')

plt.tight_layout()
plt.savefig('/Users/lbacaj/genomics/treatment_trajectory_comparison.png', dpi=200,
            bbox_inches='tight', facecolor=fig4.get_facecolor())
plt.close()
print("Chart saved: treatment_trajectory_comparison.png")

print("\n=== All 4 charts generated successfully ===")
