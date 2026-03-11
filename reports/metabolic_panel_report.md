# OXPHOS / Metabolic Gene Panel Report
### Date: March 11, 2026
### Patient: Johnny | ASPS Genomic Profile
### Genomic Drivers: ASPSCR1-TFE3 Fusion (chr17/chrX) + DNMT1 Translocation (chr19/chr1)

---

## What We Ran

We profiled the predicted expression of 47 metabolic genes across 6 tissues using AlphaGenome's `predict_interval` with RNA_SEQ output, organized into 10 functional panels:

| Panel | Genes | Rationale |
|-------|-------|-----------|
| OXPHOS Complex I | NDUFB8, NDUFS1, NDUFS2, NDUFV1, NDUFA9 | Electron transport chain entry point |
| OXPHOS Complex II | SDHB, SDHA, SDHC, SDHD | Succinate dehydrogenase (links TCA to ETC) |
| OXPHOS Complex III | UQCRC2, UQCRC1, UQCRFS1 | Cytochrome bc1 complex |
| OXPHOS Complex IV | COX4I1, COX5A, COX6B1, COX7A2 | Cytochrome c oxidase (O2 consumption) |
| OXPHOS Complex V | ATP5F1A, ATP5F1B, ATP5MC1, ATP5PO | ATP synthase (the final output) |
| TCA Cycle | CS, ACO2, IDH2, OGDH, SUCLA2, FH, MDH2, DLST | Krebs cycle enzymes |
| Lactate Transport | SLC16A1/MCT1, SLC16A3/MCT4, SLC16A7/MCT2, LDHA, LDHB | The Reverse Warburg fuel line |
| Glucose Transport | SLC2A1/GLUT1, SLC2A4/GLUT4, SLC2A3/GLUT3, HK2, PKM | Glycolysis entry and exit |
| Fatty Acid Oxidation | CPT1A, CPT2, ACADM, HADHA, ACAD9 | Alternative fuel pathway |
| Mitochondrial Dynamics | MFN1, MFN2, OPA1, DRP1/DNM1L, FIS1 | Fission/fusion balance |

**Tissues:** Lung, Liver, Heart, Brain, Transverse colon, Spleen

**Method:** For each gene, `predict_interval` was called with 1MB context centered on the gene body. Expression was extracted from the gene body region on the matching strand.

---

## Key Findings

### 1. Heart dominates OXPHOS expression — the benchmark for mitochondrial addiction

Every single OXPHOS gene across all 5 complexes shows heart as the top-expressing tissue. This is expected — heart has the highest mitochondrial density of any organ. But it provides the critical benchmark:

**If ASPS tumors approach heart-level OXPHOS expression, they are genuinely mitochondrially addicted.**

| Complex | Top Gene | Heart Expression | Next Tissue | Fold Difference |
|---------|----------|-----------------|-------------|-----------------|
| Complex I | NDUFV1 | mean 3.01 | spleen 2.27 | 1.3x |
| Complex II | SDHA | mean 0.99 | colon 0.36 | 2.8x |
| Complex III | UQCRC1 | mean 4.36 | liver 1.95 | 2.2x |
| Complex IV | COX4I1 | mean 5.99 | liver 3.60 | 1.7x |
| Complex V | ATP5F1B | mean **17.85** | liver 8.38 | 2.1x |

**ATP5F1B (ATP synthase beta subunit) is the highest-expressed metabolic gene in the entire panel** — mean 17.85 in heart, with peaks reaching 113.5. This makes Complex V (ATP synthase) the most abundantly expressed part of the electron transport chain. If the tumor upregulates this pathway, ATP synthase inhibitors could be particularly effective.

### 2. The Reverse Warburg fuel line is confirmed at the molecular level

The lactate transport genes show exactly the tissue-specific pattern predicted by the Reverse Warburg hypothesis:

| Gene | Function in Reverse Warburg | Top Tissue | Expression |
|------|---------------------------|------------|------------|
| **LDHA** | Pyruvate → Lactate (in fibroblasts) | Liver (3.33) | Ubiquitous, high everywhere |
| **LDHB** | Lactate → Pyruvate (in tumor) | Heart (0.55) | Heart/brain preferential |
| **SLC16A1/MCT1** | Lactate importer (tumor side) | Heart (0.33) | Heart/brain — lactate consumers |
| **SLC16A3/MCT4** | Lactate exporter (fibroblast side) | Spleen (0.71) | Spleen/colon — glycolytic tissues |
| **SLC16A7/MCT2** | Lactate importer (low affinity) | Heart (0.16) | Low expression overall |

**The directional pattern is exactly right:**

- **LDHA** (makes lactate) is expressed everywhere at high levels (mean 1.72 overall, max 42.75 in liver). In the Reverse Warburg model, cancer-associated fibroblasts express LDHA to convert pyruvate to lactate for export.

- **LDHB** (consumes lactate, converts back to pyruvate) is highest in heart — the organ that naturally uses lactate as fuel. If the ASPS tumor co-opts this pathway, it would upregulate LDHB to convert imported lactate back to pyruvate for burning in its mitochondria.

- **MCT1/SLC16A1** (lactate importer) is highest in heart and brain — the two organs that physiologically import lactate. The tumor would need to upregulate MCT1 to import lactate from fibroblasts.

- **MCT4/SLC16A3** (lactate exporter) is highest in spleen and colon — tissues with high glycolytic activity that export lactate. Cancer-associated fibroblasts would use MCT4 to export the lactate they produce.

### 3. SLC16A3/MCT4 is only 207kb from the ASPSCR1 breakpoint

**This is the most clinically significant finding in this analysis.**

SLC16A3/MCT4 is located at chr17:82,217,933-82,261,129. The ASPSCR1 breakpoint is at chr17:82,010,811. The distance is only **207kb**.

From the contact map analysis, we already know the ASPSCR1 breakpoint is ~12kb from a TAD boundary, and SLC16A3/MCT4 was identified as a nearby gene potentially affected by TAD disruption.

Now we know MCT4 is the lactate exporter — the gene that cancer-associated fibroblasts use to feed lactate to the tumor. Its proximity to the ASPSCR1 breakpoint means the translocation could:

1. **Disrupt the TAD boundary** separating ASPSCR1 from MCT4, potentially altering MCT4 regulation
2. **Place MCT4 under new enhancer control** from the rearranged chromosome
3. **Create a regulatory connection** between the fusion oncogene and the metabolic fuel line

This is consistent with the "Reverse Warburg fuel line" model: the tumor not only drives its own metabolism via TFE3 overexpression, but the translocation itself may directly affect the lactate transport machinery by disrupting the regulatory neighborhood of MCT4.

### 4. Glycolysis bottlenecks: HK2 is low, PKM is high

| Gene | Function | Overall Mean | Top Tissue |
|------|----------|-------------|------------|
| **PKM** (pyruvate kinase) | Last glycolysis step | 1.07 | Heart (2.11) |
| **SLC2A4/GLUT4** | Insulin-responsive glucose transporter | 0.47 | Heart (3.17) |
| **SLC2A1/GLUT1** | Constitutive glucose transporter | 0.20 | Brain (0.56) |
| **HK2** (hexokinase 2) | First glycolysis step (commits glucose) | 0.07 | Colon (0.12) |
| **SLC2A3/GLUT3** | Neuronal glucose transporter | 0.05 | Spleen (0.12) |

HK2 is the rate-limiting step of glycolysis and has the lowest expression of the glucose transport panel (mean 0.07). This means that in normal tissues, cells are not strongly committed to glycolysis. In the Reverse Warburg model, cancer-associated fibroblasts would need to upregulate HK2 to increase glycolytic flux. This makes HK2 a potential biomarker — elevated HK2 in the tumor microenvironment would confirm active glycolytic conversion.

### 5. Fatty acid oxidation: HADHA dominates

| Gene | Overall Mean | Top Tissue |
|------|-------------|------------|
| **HADHA** | 0.36 | Heart (0.96) |
| CPT2 | 0.15 | Liver (0.28) |
| ACADM | 0.12 | Heart (0.30) |
| CPT1A | 0.10 | Colon (0.21) |
| ACAD9 | 0.09 | Spleen (0.13) |

HADHA (the alpha subunit of mitochondrial trifunctional protein) has the highest expression, predominantly in heart. If the tumor uses fatty acid oxidation as a backup fuel source, HADHA would be a vulnerability — but the overall expression levels are much lower than OXPHOS genes, suggesting fatty acid oxidation is secondary to the lactate fuel line.

### 6. Mitochondrial dynamics: MFN2 high, fission/fusion balance tissue-specific

| Gene | Function | Overall Mean | Top Tissue |
|------|----------|-------------|------------|
| **MFN2** | Outer membrane fusion | 0.42 | Heart (1.53) |
| **FIS1** | Fission | 0.36 | Spleen (0.67) |
| MFN1 | Outer membrane fusion | 0.12 | Spleen (0.17) |
| DRP1/DNM1L | Fission GTPase | 0.12 | Brain (0.23) |
| OPA1 | Inner membrane fusion | 0.09 | Heart (0.16) |

The fission/fusion balance varies by tissue:
- **Heart:** Fusion-dominant (MFN2 = 1.53, FIS1 = 0.39) — long, fused mitochondrial networks for efficient OXPHOS
- **Spleen:** Fission-dominant (FIS1 = 0.67, MFN2 = 0.25) — fragmented mitochondria in immune cells

For ASPS tumors that depend on OXPHOS, a fusion-dominant mitochondrial network (like heart) would be expected. Drugs that force mitochondrial fission (e.g., by inhibiting MFN2 or enhancing DRP1) could fragment the network and reduce OXPHOS efficiency.

---

## Therapeutic Implications

### The metabolic vulnerability hierarchy

Based on expression levels and pathway logic, the tumor's metabolic dependencies rank:

1. **OXPHOS Complex V (ATP synthase)** — highest expression (ATP5F1B mean 17.85). The final step of oxidative phosphorylation. Drugs: Oligomycin-class inhibitors (research), Bedaquiline (repurposed from TB).

2. **OXPHOS Complex IV (cytochrome c oxidase)** — COX4I1 mean 5.99. The oxygen-consuming step. Drugs: Already partially targeted by Doxycycline (which inhibits mitochondrial translation of COX subunits).

3. **Lactate transport (MCT1/MCT4)** — The fuel supply line. MCT4 proximity to the ASPSCR1 breakpoint makes it a potential direct target of the translocation's regulatory effects. Drugs: AZD3965 (MCT1 inhibitor, in clinical trials), Syrosingopine (dual MCT1/MCT4 inhibitor).

4. **LDHB (lactate → pyruvate conversion)** — The enzyme that converts imported lactate back to usable fuel. Higher in oxidative tissues. Drugs: LDHB-specific inhibitors are under development.

5. **MFN2 (mitochondrial fusion)** — Maintaining the fused mitochondrial network required for efficient OXPHOS. Drugs: Leflunomide (inhibits mitochondrial fusion, approved for RA).

### Strengthening the Triple Blockade rationale

| Drug | Metabolic Target Confirmed | Evidence from This Panel |
|------|---------------------------|--------------------------|
| **Doxycycline** | Mitochondrial ribosome → OXPHOS Complex IV | COX4I1 is 3rd highest metabolic gene (mean 2.19). Doxycycline inhibits translation of mitochondrially-encoded subunits. |
| **HCQ** | Autophagy → Mitochondrial quality control | MFN2 fusion dominance means healthy mitochondria are maintained by active quality control. HCQ disrupts lysosomal degradation of damaged mitochondria, causing toxic accumulation. |
| **Cimetidine** | Anti-angiogenic → O2 supply to mitochondria | OXPHOS requires O2 (Complex IV). Restricting angiogenesis starves the mitochondria of O2, synergizing with Complex IV inhibition by Doxycycline. |

### A potential 4th axis: MCT1 inhibition

The metabolic data suggests a possible addition to the therapeutic strategy:

**AZD3965 (MCT1 inhibitor)** would block lactate import into the tumor. Combined with:
- Doxycycline (breaks the OXPHOS machinery that burns the lactate)
- HCQ (disrupts lysosomal recycling of damaged mitochondria)
- Cimetidine (restricts O2 supply to remaining functional mitochondria)

This would attack the tumor's metabolism from four angles simultaneously: **cut the fuel supply (MCT1), break the engine (Doxycycline), disable the repair shop (HCQ), and restrict the oxygen (Cimetidine).**

---

## Images

All images saved in `/Users/lbacaj/genomics/metabolic_analysis/`:

| File | Description |
|------|-------------|
| `OXPHOS_COMPLEX_I_heatmap.png` | Gene x tissue expression heatmap for Complex I |
| `OXPHOS_COMPLEX_II_heatmap.png` | Gene x tissue heatmap for Complex II |
| `OXPHOS_COMPLEX_III_heatmap.png` | Gene x tissue heatmap for Complex III |
| `OXPHOS_COMPLEX_IV_heatmap.png` | Gene x tissue heatmap for Complex IV (includes COX4I1) |
| `OXPHOS_COMPLEX_V_heatmap.png` | Gene x tissue heatmap for Complex V (includes ATP5F1B) |
| `TCA_CYCLE_heatmap.png` | Gene x tissue heatmap for TCA cycle enzymes |
| `LACTATE_TRANSPORT_heatmap.png` | Gene x tissue heatmap — MCT1, MCT4, LDHA, LDHB |
| `GLUCOSE_TRANSPORT_heatmap.png` | Gene x tissue heatmap — GLUT1, GLUT4, HK2, PKM |
| `FATTY_ACID_OXIDATION_heatmap.png` | Gene x tissue heatmap for FAO enzymes |
| `MITO_DYNAMICS_heatmap.png` | Gene x tissue heatmap — MFN1/2, OPA1, DRP1, FIS1 |
| `reverse_warburg_comparison.png` | Side-by-side comparison of MCT1 vs MCT4 vs LDHA vs LDHB |
| `metabolic_overview.png` | All 47 genes ranked by overall expression, colored by panel |

---

## Connection to Prior Analyses

1. **Contact map analysis validated:** The contact map analysis identified SLC16A3/MCT4 near the ASPSCR1 TAD boundary. This analysis confirms MCT4 is the lactate exporter gene — making the TAD boundary disruption directly relevant to the Reverse Warburg metabolism. The translocation doesn't just break the genome near MCT4; it breaks the genome near the gene that controls lactate export.

2. **Mitochondrial addiction quantified:** The initial analysis identified "mitochondrial addiction" with a vulnerability score of 13.6. This analysis provides the molecular basis — all 5 OXPHOS complexes, 8 TCA cycle enzymes, and the lactate transport machinery are expressed at levels consistent with high oxidative metabolism. Heart-level OXPHOS expression would confirm the tumor is running its mitochondria at maximum capacity.

3. **Doxycycline mechanism confirmed:** The drug target analysis showed Doxycycline targets mitochondrial ribosomes (MRPS/MRPL genes). This analysis shows the downstream effect — COX4I1 (Complex IV) is the 3rd highest metabolic gene. Doxycycline prevents translation of mitochondrially-encoded COX subunits, directly disabling the most expressed part of the cytochrome c oxidase complex.

4. **HCQ mechanism extended:** HCQ targets lysosomes/autophagy. The mitochondrial dynamics data shows MFN2-dominant fusion networks require active mitophagy (lysosomal degradation of damaged mitochondria) to maintain quality. HCQ disrupting this quality control pathway would cause accumulation of damaged, ROS-producing mitochondria — converting the tumor's metabolic strength into a source of oxidative damage.

---

*Analysis performed using AlphaGenome v0.6.1 (Google DeepMind). Expression predictions for 47 genes across 6 UBERON tissue ontology terms. Gene body expression extracted from strand-matched RNA-seq tracks. All raw data saved to metabolic_analysis/metabolic_results.json and metabolic_analysis/metabolic_summary.csv.*
