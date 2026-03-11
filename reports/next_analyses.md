# Additional AlphaGenome Analyses — Prioritized List
### Patient: Johnny | ASPS Genomic Profile
### Created: March 11, 2026

---

## 1. Contact Maps / 3D Chromatin Structure — COMPLETED

AlphaGenome supports `CONTACT_MAPS` output. This shows TAD boundaries and enhancer-promoter loops at each breakpoint. Translocations disrupt 3D chromatin topology, and mapping which TAD boundaries are broken reveals genes affected at a distance — not just at the breakpoint itself.

**Status:** Run on March 11, 2026. Results in:
- Report: [`contact_map_report.md`](contact_map_report.md)
- Images (40 PNGs): [`contact_maps/`](contact_maps/)
- Structured data: [`contact_map_results.json`](contact_map_results.json)
- Script: [`contact_maps_analysis.py`](contact_maps_analysis.py)

**Key result:** 3 of 4 breakpoints sit directly at TAD boundaries. The ASPSCR1 breakpoint is ~12kb from a boundary near SLC16A3/MCT4 (the lactate transporter central to Reverse Warburg metabolism). The DNMT1-chr1 breakpoint is at a boundary adjacent to LAPTM5 (essential for T-cell cytotoxicity). See full report for details.

---

## 2. Fusion Junction Sequence Modeling — COMPLETED

Instead of analyzing each breakpoint independently, construct the actual chimeric DNA sequence that results from the translocation (ASPSCR1 exons 1-7 joined to TFE3 exons 4-10) and feed it to `predict_sequence`. This would predict what the fusion transcript actually looks like — its expression pattern, splicing, and chromatin state — rather than inferring it from the breakpoints separately.

**Status:** Run on March 11, 2026. Results in:
- Report: [`fusion_junction_report.md`](fusion_junction_report.md)
- Images (7 PNGs): [`fusion_analysis/`](fusion_analysis/)
- Structured data: [`fusion_analysis/fusion_results.json`](fusion_analysis/fusion_results.json)
- Script: [`fusion_junction_analysis.py`](fusion_junction_analysis.py)

**Key results:** The fusion creates a precision transcriptional machine with 4-7x amplified transcription initiation (CAGE) compared to normal ASPSCR1, focused exclusively on the + strand. No aberrant splice sites form at the junction — the fusion produces a single clean transcript. Chromatin at the junction adopts an intermediate accessibility state between normal ASPSCR1 and normal TFE3. See full report for details.

---

## 3. Splice Site Usage / Splice Junction Analysis — COMPLETED

The existing analysis used `SPLICE_SITES` but AlphaGenome also has `SPLICE_SITE_USAGE` and `SPLICE_JUNCTIONS` output types. Running these at the breakpoints would directly predict whether aberrant splice products form at the fusion junction — clinically relevant for neoantigen prediction.

**Status:** Run on March 11, 2026. Results in:
- Report: [`splice_junction_report.md`](splice_junction_report.md)
- Images (7 PNGs): [`splice_junctions/`](splice_junctions/)
- Structured data: [`splice_junctions/splice_junction_results.json`](splice_junctions/splice_junction_results.json)
- Script: [`splice_junction_analysis.py`](splice_junction_analysis.py)

**Key results:** ASPSCR1 has 4 active + strand splice sites within 1kb (usage 0.95-0.98). TFE3 has only 1 active - strand splice site within 1kb, located 876bp from the breakpoint — confirming the intron-like gap at the fusion junction. DNMT1-chr1 is a splice desert (0 sites within 10kb). DNMT1-chr19 has 8 active - strand splice sites within 1kb, with one just 179bp from the breakpoint. Variant effects on splicing are negligible at all breakpoints (max 0.000047). No cryptic splice sites or neoantigen-generating splice aberrations detected.

---

## 4. Broader OXPHOS / Metabolic Gene Panel — COMPLETED

The drug target script covers MMPs and mitochondrial ribosomal proteins, but the "mitochondrial addiction" finding (vulnerability score 13.6) could be deepened by profiling the full metabolic machinery.

**Status:** Run on March 11, 2026. Results in:
- Report: [`metabolic_panel_report.md`](metabolic_panel_report.md)
- Images (12 PNGs): [`metabolic_analysis/`](metabolic_analysis/)
- Structured data: [`metabolic_analysis/metabolic_results.json`](metabolic_analysis/metabolic_results.json)
- Summary CSV: [`metabolic_analysis/metabolic_summary.csv`](metabolic_analysis/metabolic_summary.csv)
- Script: [`oxphos_metabolic_analysis.py`](oxphos_metabolic_analysis.py)

**Key results:** 47 genes profiled across 10 metabolic panels. Heart dominates OXPHOS expression across all 5 complexes, with ATP5F1B (Complex V) being the highest-expressed gene (mean 17.85). The Reverse Warburg fuel line is confirmed: LDHA (makes lactate) is ubiquitous, MCT1 (imports lactate) is highest in oxidative tissues (heart/brain), MCT4 (exports lactate) is highest in glycolytic tissues (spleen/colon). Critically, SLC16A3/MCT4 is only 207kb from the ASPSCR1 breakpoint — the translocation directly disrupts the regulatory neighborhood of the lactate export gene.

---

## 5. Wider Neighborhood Gene Effects — COMPLETED

Mapped all protein-coding genes within 500kb of each breakpoint and profiled their expression across tissues to identify collateral damage from the translocations.

**Status:** Run on March 11, 2026. Results in:
- Report: [`neighborhood_gene_report.md`](neighborhood_gene_report.md)
- Images (4 PNGs): [`neighborhood_analysis/`](neighborhood_analysis/)
- Structured data: [`neighborhood_analysis/neighborhood_results.json`](neighborhood_analysis/neighborhood_results.json)
- Script: [`neighborhood_gene_analysis.py`](neighborhood_gene_analysis.py)

**Key results:** 134 protein-coding genes identified across the 4 neighborhoods. Major discovery: the DNMT1-chr1 breakpoint is INSIDE PUM1 (Pumilio RNA-binding protein 1), not in intergenic space — adding a post-transcriptional regulatory disruption. TFE3 neighborhood contains WDR45 (autophagy, 30kb) and FOXP3 (Treg regulator, 207kb). DNMT1-chr19 neighborhood contains an ICAM cluster (ICAM1/4/5 at 111-130kb) and immune signaling genes (P2RY11, S1PR2, SHFL). ASPSCR1 neighborhood contains FASN (lipogenesis, 67kb) and RAC3 (cell migration, 21kb).

---

## 6. Population Variant Overlap — COMPLETED

Cross-referenced the critical ISM positions against ClinVar and gnomAD to validate ISM findings with population genetics and clinical data.

**Status:** Run on March 11, 2026. Results in:
- Report: [`population_variant_report.md`](population_variant_report.md)
- Images (2 PNGs): [`population_variants/`](population_variants/)
- Structured data: [`population_variants/population_variant_results.json`](population_variants/population_variant_results.json)
- Script: [`population_variant_analysis.py`](population_variant_analysis.py)

**Key results:** The ASPSCR1 ISM hotspot (chr17:82,010,869) has a ClinVar entry — it's a splice donor variant (c.1237+1G>T) independently confirming the ISM prediction. All ISM regulatory positions have only singleton variants in gnomAD (AF ~0.000001), confirming strong evolutionary constraint. Unexpected: the TFE3 breakpoint (chrX:49,043,986) harbors a common polymorphism rs59403483 with AF=83%.

---

## 7. PROCAP Deep Dive — COMPLETED

PROCAP (Precision Run-On CAP sequencing) measures transcription initiation at single-nucleotide resolution. Data was collected fresh from AlphaGenome (not from multimodal_results.json, which did not include PROCAP).

**Status:** Run on March 11, 2026. Results in:
- Report: [`procap_report.md`](procap_report.md)
- Images (8 PNGs): [`procap_analysis/`](procap_analysis/)
- Structured data: [`procap_analysis/procap_results.json`](procap_analysis/procap_results.json)
- Script: [`procap_analysis.py`](procap_analysis.py)

**Key results:** TFE3 has massive PROCAP signal (score 416.0 at bp-632 on - strand) — 670x stronger than ASPSCR1 (0.61). This explains why the fusion CAGE is so amplified: TFE3's promoter is enormously powerful. Unexpected bidirectional transcription at TFE3 breakpoint (+ strand scores 21-31) suggests enhancer activity. The DNMT1-chr1 breakpoint (inside PUM1) has active transcription initiation at bp+373 (PROCAP 2.41), confirming the translocation breaks through an active initiation zone. PROCAP data only available for K562 cell line.

---

## Summary Table

| # | Analysis | Status | Priority | Estimated API Calls |
|---|----------|--------|----------|-------------------|
| 1 | Contact Maps / 3D Structure | **DONE** | Highest | 16 |
| 2 | Fusion Junction Sequence | **DONE** | High | 12 |
| 3 | Splice Site Usage / Junctions | **DONE** | High | 8-16 |
| 4 | OXPHOS / Metabolic Gene Panel | **DONE** | High | ~25 |
| 5 | Neighborhood Gene Effects | **DONE** | Medium | ~50 (gene expression) |
| 6 | Population Variant Overlap | **DONE** | Medium | 0 (external DBs) |
| 7 | PROCAP Deep Dive | **DONE** | Medium | 8 (K562 PROCAP + CAGE) |
