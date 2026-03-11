# Wider Neighborhood Gene Effects Report
### Date: March 11, 2026
### Patient: Johnny | ASPS Genomic Profile
### Genomic Drivers: ASPSCR1-TFE3 Fusion (chr17/chrX) + DNMT1 Translocation (chr19/chr1)

---

## What We Ran

For each of the 4 translocation breakpoints, we mapped all protein-coding genes within a 500kb radius and profiled their expression using AlphaGenome's RNA_SEQ predictions. This identifies the "collateral damage" — genes near each breakpoint whose regulation could be disrupted by the translocation through TAD boundary disruption, enhancer hijacking, or direct gene breakage.

**Method:**
- Gene identification from GENCODE v46 GTF (hg38)
- Expression profiling via `predict_interval` (1MB context, RNA_SEQ, 6 tissues)
- Distance calculation from breakpoint to nearest gene boundary
- Cross-reference with TAD boundary findings from contact map analysis

---

## Key Findings

### 1. ASPSCR1 neighborhood (chr17:82,010,811) — Gene-rich, metabolic hub

**47 protein-coding genes within 500kb.** This is a gene-dense region of chromosome 17.

| Gene | Distance | Strand | Expression (mean) | Top Tissue | Significance |
|------|----------|--------|-------------------|------------|--------------|
| **ASPSCR1** | 0 (inside) | + | 0.093 | spleen | Breakpoint gene; fusion partner |
| CENPX | 7.9kb | - | 0.572 | spleen | Centromere protein; chromosome segregation |
| LRRC45 | 12.5kb | + | 0.248 | spleen | Leucine-rich repeat; centriole assembly |
| RAC3 | 20.9kb | + | 0.329 | brain | Rho GTPase; cell migration, invasion |
| **DCXR** | 24.3kb | - | **3.202** | liver (7.61) | Dicarbonyl reductase; highest expressed neighbor |
| RFNG | 37.1kb | - | 1.228 | spleen | Radical fringe; Notch signaling modifier |
| GPS1 | 39.9kb | + | 1.251 | spleen | COP9 signalosome; protein degradation |
| DUS1L | 46.7kb | - | 0.871 | spleen | tRNA dihydrouridine synthase |
| NOTUM | 49.0kb | - | 0.047 | liver | Wnt signaling inhibitor |
| **FASN** | 67.5kb | - | **1.693** | liver (3.68) | Fatty acid synthase; de novo lipogenesis |
| SIRT7 | 89.5kb | - | 0.673 | spleen | Sirtuin 7; chromatin regulation; DNA repair |

**Critical neighbors:**
- **DCXR** (24kb away, expression 3.20): The highest-expressed gene near the ASPSCR1 breakpoint. Dicarbonyl/L-xylulose reductase is involved in carbonyl detoxification — relevant to oxidative stress in the tumor microenvironment.
- **FASN** (67kb away, expression 1.69): Fatty acid synthase controls de novo lipogenesis. Many cancers upregulate FASN for membrane biosynthesis. Its proximity to the breakpoint means the translocation could alter its regulation.
- **RAC3** (21kb away): A Rho GTPase that promotes cell migration and invasion — directly relevant to metastasis.
- **RFNG** (37kb): A Notch signaling modifier. Notch dysregulation is implicated in multiple cancers.
- **SIRT7** (89kb): A sirtuin involved in chromatin regulation and DNA repair. Disruption could affect the tumor's "quiet genome" stability.

**Note:** SLC16A3/MCT4 (the lactate exporter identified in the metabolic panel analysis) is 207kb from the breakpoint — within the same neighborhood but beyond the nearest 15 genes profiled here. Its expression was profiled separately (mean 0.195, top in spleen).

### 2. TFE3 neighborhood (chrX:49,043,986) — Immune-relevant cluster

**40 protein-coding genes within 500kb.**

| Gene | Distance | Strand | Expression (mean) | Top Tissue | Significance |
|------|----------|--------|-------------------|------------|--------------|
| **TFE3** | 576bp | - | 0.486 | spleen | Breakpoint gene; fusion partner |
| CCDC120 | 9.6kb | + | 0.111 | colon | Coiled-coil domain |
| PRAF2 | 27.2kb | - | 0.861 | brain | Prenylated Rab acceptor; vesicle trafficking |
| WDR45 | 30.4kb | - | 0.220 | spleen | WD repeat; autophagy (BPAN when mutated) |
| GRIPAP1 | 41.7kb | - | 0.256 | spleen | GRIP-associated protein; receptor trafficking |
| GPKOW | 69.4kb | - | 0.197 | spleen | G-patch domain; RNA splicing |
| **PIM2** | 125.0kb | - | 0.554 | spleen (1.56) | Proto-oncogene kinase; anti-apoptotic |
| **PLP2** | 127.9kb | + | **2.081** | colon (3.93) | Proteolipid protein 2; highest expressed |
| PRICKLE3 | 130.8kb | - | 0.211 | colon | Planar cell polarity pathway |
| **FOXP3** | 206.5kb | - | — | — | Master regulator of regulatory T cells |

**Critical neighbors:**
- **WDR45** (30kb away): Encodes a protein essential for autophagy. Mutations cause BPAN (beta-propeller protein-associated neurodegeneration). Its proximity to TFE3 — the master regulator of lysosomal biogenesis — creates a concentrated autophagy regulatory zone. The translocation could disrupt WDR45 regulation.
- **PIM2** (125kb, expression 0.55 in spleen): A proto-oncogene that inhibits apoptosis and promotes cell survival. PIM kinases are drug targets in hematologic malignancies. Its high spleen expression and proximity to TFE3 are notable.
- **FOXP3** (207kb): The master regulator of regulatory T cells (Tregs). Disruption of the TAD containing FOXP3 could affect Treg differentiation in the tumor microenvironment — relevant to immune evasion.
- **PLP2** (128kb, expression 2.08): The highest-expressed gene in the TFE3 neighborhood. Proteolipid protein involved in membrane organization.

### 3. DNMT1-chr1 breakpoint (chr1:31,048,832) — PUM1 is directly broken

**10 protein-coding genes within 500kb.** This is a gene-sparse region.

**Major new finding: The breakpoint is INSIDE PUM1, not in intergenic space.**

| Gene | Distance | Strand | Expression (mean) | Top Tissue | Significance |
|------|----------|--------|-------------------|------------|--------------|
| **PUM1** | 0 (inside) | - | 0.174 | lung | **Pumilio RNA-binding protein 1; mRNA stability regulator** |
| NKAIN1 | 131kb | - | 0.024 | brain | Na+/K+ ATPase interacting |
| SDC3 | 140kb | - | 0.250 | brain | Syndecan-3; neural development |
| SNRNP40 | 211kb | - | 0.111 | spleen | Spliceosome component |
| ZCCHC17 | 248kb | + | 0.053 | brain | Zinc finger; RNA binding |
| **LAPTM5** | 291kb | - | **0.704** | spleen (2.23) | Lysosomal protein; T-cell/NK-cell cytotoxicity |
| FABP3 | 316kb | - | 0.131 | brain | Fatty acid binding protein; heart type |
| MATN1 | 325kb | - | 0.015 | spleen | Matrilin-1; cartilage matrix |
| SERINC2 | 361kb | + | 0.243 | liver | Serine incorporator; membrane lipid synthesis |

**PUM1 disruption is biologically significant:**

PUM1 (Pumilio RNA-binding protein 1) is a post-transcriptional regulator that controls the stability and translation of hundreds of mRNAs. It is a key component of the PUF (Pumilio and FBF) family of RNA-binding proteins. PUM1:

- **Regulates cell proliferation** by controlling mRNA decay of cell cycle genes
- **Modulates the immune response** by regulating cytokine mRNA stability
- **Controls stem cell self-renewal** through post-transcriptional gene regulation
- PUM1 haploinsufficiency causes **PADDAS** (PUM1-associated developmental disability, ataxia, and seizures)

The translocation breaking PUM1 means one allele is non-functional. While the remaining allele provides some PUM1 function, haploinsufficiency effects could contribute to:
- Altered mRNA stability profiles in tumor and immune cells
- Dysregulated cell cycle control
- Impaired post-transcriptional fine-tuning of gene expression

**This reframes the DNMT1-chr1 breakpoint:** Previously characterized as hitting a "splice desert" near LAPTM5, the breakpoint actually disrupts PUM1 directly. The damage at this breakpoint is double — PUM1 breakage (post-transcriptional regulation) plus TAD boundary disruption affecting LAPTM5 (immune function at 291kb distance).

### 4. DNMT1-chr19 breakpoint (chr19:10,160,241) — ICAM cluster and immune signaling

**37 protein-coding genes within 500kb.** Gene-dense region.

| Gene | Distance | Strand | Expression (mean) | Top Tissue | Significance |
|------|----------|--------|-------------------|------------|--------------|
| **DNMT1** | 0 (inside) | - | 0.126 | spleen | Breakpoint gene; DNA methyltransferase |
| **EIF3G** | 40kb | - | **2.410** | spleen (3.45) | Translation initiation factor; protein synthesis |
| P2RY11 | 45kb | + | 0.553 | spleen | Purinergic receptor; ATP signaling; immune activation |
| PPAN | 48kb | + | 0.527 | spleen | Peter Pan homolog; ribosome biogenesis |
| ANGPTL6 | 58kb | - | 0.284 | spleen | Angiopoietin-like 6; angiogenesis |
| S1PR2 | 61kb | - | 0.141 | spleen | Sphingosine-1-phosphate receptor 2; immune trafficking |
| SHFL | 67kb | + | 0.984 | liver (1.65) | Shiftless; antiviral innate immunity |
| MRPL4 | 92kb | + | 0.487 | spleen | Mitochondrial ribosomal protein L4 |
| **ICAM1** | 111kb | + | 0.402 | spleen (0.80) | Intercellular adhesion molecule 1; immune cell binding |
| ICAM4 | 127kb | + | 0.196 | spleen | ICAM4; red blood cell adhesion |
| ICAM5 | 130kb | + | 0.047 | spleen | ICAM5; telencephalin; neuronal |

**Critical neighbors:**
- **EIF3G** (40kb, expression 2.41): The highest-expressed gene near the DNMT1 breakpoint. Translation initiation factor subunit G — disruption could impair global protein synthesis.
- **P2RY11** (45kb): Purinergic receptor that senses extracellular ATP — a "danger signal" released by damaged cells. P2RY11 activates immune responses. Its proximity to the DNMT1 breakpoint means the translocation could alter ATP-sensing in the tumor microenvironment.
- **S1PR2** (61kb): Sphingosine-1-phosphate receptor 2 controls immune cell trafficking. Disruption could affect T-cell and B-cell migration to the tumor.
- **ICAM1** (111kb): The intercellular adhesion molecule that T-cells use to bind and kill target cells. The ICAM cluster (ICAM1/4/5) at 111-130kb from the breakpoint is within the TAD disruption zone. If the translocation alters ICAM1 expression, it could impair immune cell adhesion to tumor cells.
- **MRPL4** (92kb): A mitochondrial ribosomal protein — one of the Doxycycline targets identified in the drug target analysis. Its proximity to the DNMT1 breakpoint means Doxycycline's effects could be amplified if the translocation alters MRPL4 regulation.
- **SHFL** (67kb): An antiviral innate immunity gene. Its presence near the DNMT1 breakpoint adds to the immune signaling disruption pattern.

---

## Synthesis: The Translocation Network Map

### Each breakpoint disrupts a distinct functional neighborhood

| Breakpoint | Direct Gene Hit | Neighborhood Theme | Key Collateral Targets |
|-----------|----------------|-------------------|----------------------|
| ASPSCR1 | ASPSCR1 (fusion) | Metabolic / biosynthesis | DCXR, FASN, RAC3, SIRT7, SLC16A3 (207kb) |
| TFE3 | TFE3 (fusion) | Autophagy / immune regulation | WDR45, PIM2, FOXP3 |
| DNMT1-chr1 | **PUM1** (RNA regulation) | Sparse; post-transcriptional | LAPTM5 (291kb, immune) |
| DNMT1-chr19 | DNMT1 (methylation) | Immune signaling / adhesion | EIF3G, P2RY11, S1PR2, ICAM1, SHFL |

### The immune evasion picture deepens

Combining the neighborhood analysis across all 4 breakpoints reveals a pattern of immune disruption:

1. **TFE3 neighborhood:** FOXP3 (Treg master regulator) at 207kb — potential Treg dysregulation
2. **DNMT1-chr19 neighborhood:** ICAM1 (immune adhesion) at 111kb, P2RY11 (danger sensing) at 45kb, S1PR2 (immune trafficking) at 61kb
3. **DNMT1-chr1 neighborhood:** LAPTM5 (T-cell cytotoxicity) at 291kb, PUM1 (mRNA regulation of immune genes) directly broken
4. **ASPSCR1 neighborhood:** RAC3 (cell migration) at 21kb — promotes invasion and metastasis

The tumor's two translocations don't just create the ASPSCR1-TFE3 fusion and break DNMT1 — they disrupt regulatory neighborhoods containing multiple immune signaling genes (FOXP3, ICAM1, P2RY11, S1PR2, LAPTM5) and a key RNA regulator (PUM1).

### The metabolic picture extends

The ASPSCR1 neighborhood contains FASN (fatty acid synthase, 67kb) and SLC16A3/MCT4 (lactate exporter, 207kb). The DNMT1-chr19 neighborhood contains MRPL4 (mitochondrial ribosomal protein, 92kb). These metabolic genes in the collateral damage zone provide additional nodes where the translocations could amplify or disrupt metabolic programs.

---

## Images

All images saved in `/Users/lbacaj/genomics/neighborhood_analysis/`:

| File | Description |
|------|-------------|
| `ASPSCR1_neighborhood.png` | Gene neighborhood map — 15 nearest genes with expression bars, colored by distance |
| `TFE3_neighborhood.png` | Gene neighborhood map for TFE3 breakpoint |
| `DNMT1_chr1_neighborhood.png` | Gene neighborhood map — note sparse gene density and PUM1 at center |
| `DNMT1_chr19_neighborhood.png` | Gene neighborhood map — note ICAM cluster and immune genes |

---

## Connection to Prior Analyses

1. **Contact map validation:** The contact maps showed TAD boundaries at 3 of 4 breakpoints. This analysis identifies the genes within those TADs that could be affected by boundary disruption — particularly ICAM1 (111kb from DNMT1-chr19 breakpoint) and FOXP3 (207kb from TFE3 breakpoint).

2. **Metabolic panel extension:** The metabolic analysis profiled SLC16A3/MCT4 and MRPL4 individually. The neighborhood analysis confirms both are within the collateral damage zones of their respective breakpoints, not just randomly located nearby.

3. **PUM1 discovery reframes the DNMT1-chr1 breakpoint:** Previous analyses characterized this breakpoint as hitting intergenic space near LAPTM5. The neighborhood mapping reveals the breakpoint is actually inside PUM1, a major RNA-binding protein. This adds a post-transcriptional regulatory dimension to the translocation's effects that was previously unrecognized.

4. **Splice junction connection:** The splice analysis showed the DNMT1-chr1 breakpoint is in a "splice desert" (0 splice sites within 10kb). This is consistent with the breakpoint being in a large intron of PUM1 (which spans 134kb). Large introns have sparse splice sites.

---

*Analysis performed using AlphaGenome v0.6.1 (Google DeepMind). Gene annotations from GENCODE v46 (hg38). Expression predictions for 50 genes across 6 UBERON tissue ontology terms. All raw data saved to neighborhood_analysis/neighborhood_results.json.*
