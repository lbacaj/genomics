# ASPS Genomic Analysis — AlphaGenome Pipeline

Comprehensive genomic analysis of Alveolar Soft Part Sarcoma (ASPS) driven by the **ASPSCR1-TFE3** translocation, using Google DeepMind's [AlphaGenome](https://deepmind.google/discover/blog/alphagenome-predicts-how-dna-sequence-drives-gene-regulation/) model to predict regulatory variant effects at single base-pair resolution.

## Somatic Alterations Analyzed

| Gene | Alteration | Breakpoint (hg38) |
|------|-----------|-------------------|
| **ASPSCR1** | t(17;X) translocation, exons 1-7 | chr17:82,010,811 |
| **TFE3** | t(17;X) translocation, exons 4-10 | chrX:49,043,986 |
| **DNMT1** (partner) | t(1;19) translocation | chr1:31,048,832 |
| **DNMT1** (primary) | t(1;19) translocation, exon 14 | chr19:10,160,241 |

## Query Reports

Nine sequential analyses building from raw genomic data to treatment strategy:

| # | Report | Description |
|---|--------|-------------|
| 1 | `query1_somatic_alteration_analysis.md` | Comprehensive translocation mapping across all breakpoints |
| 2 | `query2_blockade_evaluation.md` | Triple Blockade strength assessment and escape route analysis |
| 3 | `query3_top50_analysis.md` | Top 50x3 matrix — Strengths, Vulnerabilities, and Druggable Targets |
| 4 | `query4_top5_impact_tracks.md` | Top 5 highest-impact tracks per chromosome translocation variant |
| 5 | `query5_war_game.md` | War Game simulation — battle for terrain modeling |
| 6 | `query6_sequential_priming.md` | Sequential Priming Model — 30-day Doxycycline then 90-day Triple Blockade |
| 7 | `query7_tumor_death_timeline.md` | Tumor cell death timeline — 90-day chart with sequential Doxycycline priming |
| 8 | `query8_immune_deep_dive.md` | Immune system deep dive + DNMT1 mutation probability |
| 9 | `query9_treatment_comparison.md` | Treatment comparison — Triple Blockade vs. Immunotherapy combination |

## Specialized Analysis Reports

| Report | Description |
|--------|-------------|
| `contact_map_report.md` | 3D chromatin structure / Hi-C contact maps at each breakpoint |
| `deep_ism_report.md` | Deep In Silico Mutagenesis — base-pair resolution functional mapping |
| `drug_target_report.md` | Drug target gene expression analysis for the Triple Blockade |
| `fusion_junction_report.md` | Chimeric ASPSCR1-TFE3 fusion sequence modeling |
| `metabolic_panel_report.md` | OXPHOS / metabolic gene panel — Reverse Warburg hypothesis validation |
| `multimodal_report.md` | Multi-modal chromatin landscape (DNase, ATAC, CAGE, histone ChIP, TF ChIP, splice sites) |
| `neighborhood_gene_report.md` | Wider neighborhood gene effects within 500kb of each breakpoint |
| `population_variant_report.md` | gnomAD / ClinVar overlap at functionally critical ISM positions |
| `procap_report.md` | PROCAP transcription initiation analysis at single-nucleotide resolution |
| `splice_junction_report.md` | Splice site usage and splice junction predictions at breakpoints |
| `splicing_accessibility_report.md` | Splicing and chromatin accessibility analysis |
| `reproduction_report.md` | Independent reproduction and validation of initial findings |
| `extended_analysis_report.md` | Extended AlphaGenome multi-modal analysis |
| `dietary_metabolic_strategy_report.md` | Genomics-informed dietary and metabolic strategy |

## Charts

13 publication-quality visualizations in `charts/`:

- **15-Month Outcome Simulation** — Sequential Strategy vs. Nivo/Ipi/Cabo, 450-day tumor viability curves
- **180-Day Treatment Timeline** — Tumor viability, fibroblast network, and immune engagement overlay
- **Six-Domain Comparison at Day 180** — Triple Blockade vs. Nivo/Ipi/Cabo vs. Hybrid
- **Treatment Trajectory Comparison** — Total tumor score over 180 days for all strategies
- **Drug Target Expression Radar** — Spider plot of 16 key targets color-coded by drug
- **Sequential vs. Simultaneous Priming** — Trajectory curves + Day 120 domain comparison
- **Checkpoint Expression Waterfall** — LAG3 >> TIM-3 >> PD-L1 >> PD-1 >> CTLA-4 >> TIGIT
- **Toxicity Head-to-Head** — Grade 3-4 events, discontinuation rates, risk factors
- **ISM Heatmap Across Breakpoints** — Top impact scores for all 4 breakpoints
- **Escape Route Trap Diagram** — Three escape routes each blocked by specific drug mechanism
- **Three-Matrix Bubble Chart** — Dangerous Attributes, Vulnerabilities, Probable Targets
- **HCQ Pharmacokinetic Loading** — Drug tissue accumulation curves over 90 days
- **Fortress Architecture Diagram** — Five defensive layers with drug attack vectors

## Analysis Subdirectories

| Directory | Contents |
|-----------|----------|
| `contact_maps/` | Hi-C contact map visualizations across 4 cell types (HCT116, HFFc6, HepG2, IMR90) for each breakpoint |
| `fusion_analysis/` | ASPSCR1-TFE3 chimeric fusion sequence predictions — RNA-seq, CAGE, DNase, splice comparisons |
| `metabolic_analysis/` | OXPHOS complex I-V heatmaps, TCA cycle, fatty acid oxidation, glucose/lactate transport, Reverse Warburg comparison |
| `neighborhood_analysis/` | Gene neighborhood maps within 500kb of each breakpoint |
| `population_variants/` | Variant density comparisons and summary tables against gnomAD/ClinVar |
| `procap_analysis/` | Transcription initiation zoom and PROCAP vs. CAGE comparisons per breakpoint |
| `splice_junctions/` | Splice junction and splice site usage visualizations per breakpoint |

## Python Scripts

| Script | Purpose |
|--------|---------|
| `reproduce_analysis.py` | Reproduce the core AlphaGenome analysis |
| `reproduce_comprehensive.py` | Comprehensive reproduction with 3 scoring approaches |
| `extend_multimodal.py` | Multi-modal analysis across all output types |
| `extend_ism_deep.py` | Deep 256bp ISM window at critical ASPSCR1 position |
| `extend_drug_targets.py` | Drug target accessibility scoring for Triple Blockade |
| `extend_splicing.py` | Splicing and 3D contact analysis at breakpoints |
| `contact_maps_analysis.py` | Hi-C contact map prediction and TAD boundary analysis |
| `fusion_junction_analysis.py` | Chimeric fusion sequence construction and modeling |
| `oxphos_metabolic_analysis.py` | Full OXPHOS/metabolic gene panel profiling |
| `splice_junction_analysis.py` | Splice site usage and junction analysis |
| `neighborhood_gene_analysis.py` | 500kb neighborhood gene characterization |
| `population_variant_analysis.py` | gnomAD/ClinVar cross-reference at ISM positions |
| `procap_analysis.py` | PROCAP transcription initiation deep dive |
| `generate_all_charts.py` | Generate charts 5-13 |
| `outcome_simulation_chart.py` | Generate charts 1-4 (outcome simulations) |
| `updated_model.py` | Updated Quadruple Blockade + Stereotactic Radiosurgery model |

## Setup

1. Install AlphaGenome: `pip install -U alphagenome`
2. Set your API key in `.env`: `ALPHA_GENOME_API_KEY=your_key_here`
3. Run any analysis script: `python reproduce_comprehensive.py`

## Key Findings

- **ASPSCR1 (chr17)** — Highest transcriptional volatility (score 14.0 in BJ fibroblasts)
- **Extreme fibrosis** (score 14.81) and **angiogenic demand** (score 11.53) as primary tumor strengths
- **Mitochondrial addiction** (score 13.625) as the core vulnerability — confirmed Reverse Warburg metabolism
- **Naive B cells** (11.625) and **Regulatory T cells** (9.0) as top immune/druggable targets
- Triple Blockade rationale validated: Doxycycline (engine block) + HCQ (disposal block) + metabolic starvation (fuel block)
