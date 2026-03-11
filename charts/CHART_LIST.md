# Chart List — Johnny ASPS Genomic Analysis

## Completed (13/13)

- [x] **15-Month Outcome Simulation** (`15month_outcome_simulation.png`) — Sequential Strategy (Curative) vs. Challenger Nivo/Ipi/Cabo (Palliative), 450-day tumor viability curves with annotated inflection points
- [x] **180-Day Treatment Timeline** (`180day_treatment_timeline.png`) — Three-curve overlay: Tumor Viability, Fibroblast Network melting, Immune Engagement rising, with phase regions and inflection annotations
- [x] **Six-Domain Comparison at Day 180** (`domain_comparison_day180.png`) — Bar chart comparing Triple Blockade vs. Nivo/Ipi/Cabo vs. Hybrid across all six tumor domains
- [x] **Treatment Trajectory Comparison** (`treatment_trajectory_comparison.png`) — Total tumor score (% baseline) over 180 days for all three strategies
- [x] **Drug Target Expression Radar Chart** (`drug_target_radar.png`) — Spider plot of 16 key targets (CTSD 4.97, VEGFB 2.0, MRPS12 1.4, etc.) color-coded by drug, showing tumor expression landscape
- [x] **Sequential vs. Simultaneous Priming** (`priming_comparison.png`) — Side-by-side: trajectory curves + Day 120 domain bar chart, showing sequential wins by ~10%
- [x] **Checkpoint Expression Waterfall** (`checkpoint_waterfall.png`) — LAG3 (0.111) >> TIM-3 >> PD-L1 >> PD-1 >> CTLA-4 >> TIGIT, making the case for anti-LAG3
- [x] **Toxicity Head-to-Head** (`toxicity_comparison.png`) — Three-panel: Grade 3-4 events (5% vs 50%), discontinuation rates, risk factor comparison
- [x] **ISM Heatmap Across Breakpoints** (`ism_heatmap.png`) — Top impact scores for all 4 breakpoints, highlighting TFE3 7bp immune element (3.29 — 4-8x all others)
- [x] **Escape Route Trap Diagram** (`escape_routes.png`) — Three escape routes (angiogenic, metabolic, macrophage) each shown BLOCKED by specific drug mechanism
- [x] **Three-Matrix Bubble Chart** (`alphagenome_matrices.png`) — Dangerous Attributes, Vulnerabilities, Probable Targets side-by-side with scores
- [x] **HCQ Pharmacokinetic Loading** (`hcq_loading_curve.png`) — All 3 drugs' tissue accumulation curves, showing HCQ still deepening at Day 90 (only ~60% of steady state)
- [x] **Fortress Architecture Diagram** (`fortress_layers.png`) — Five defensive layers (collagen bunker → epigenetic fog) with drug attack arrows

## Generation Scripts

- `outcome_simulation_chart.py` — Charts 1-4
- `generate_all_charts.py` — Charts 5-13
