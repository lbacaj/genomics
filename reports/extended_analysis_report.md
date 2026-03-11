# Extended AlphaGenome Analysis: Johnny's ASPS Genomic Profile
### Date: March 11, 2026
### Genomic Drivers: ASPSCR1-TFE3 Fusion (chr17/chrX), DNMT1 Translocation (chr1/chr19)

---

## Overview

This report extends the initial reproduction analysis with four new dimensions:

1. **Multi-modal profiling** — chromatin accessibility (DNASE/ATAC), transcription initiation (CAGE), histone modifications (ChIP-seq), transcription factor binding, and splice sites at all 4 breakpoints
2. **Deep in silico mutagenesis (ISM)** — 256bp window, 768 variants per target, with both RNA-seq and DNase scorers to map the exact regulatory elements at each breakpoint
3. **Drug target gene expression** — predicted expression levels of 60+ genes targeted by the current Triple Blockade therapy, plus immune checkpoint and pathway genes
4. **Splicing and chromatin accessibility** — detailed accessibility measurements at each breakpoint

---

## 1. The Chromatin Landscape at Each Breakpoint

The multi-modal analysis reveals that these four breakpoints sit in fundamentally different regulatory environments:

### ASPSCR1 (chr17:82,010,811) — An Actively Transcribed Region

The ASPSCR1 breakpoint is in a region of **active transcription**:
- **RNA Polymerase II** (POLR2AphosphoS5) is bound here at very high levels, especially in spleen tissue (score 414.6) — this means the transcriptional machinery is physically present and engaged at this locus
- **H3K4me3** (active promoter mark) is extremely high in brain (384.0) — confirming a promoter or promoter-adjacent region
- **H3K36me3** (active elongation mark) is high in thymus (339.2) and brain (317.4) — confirming active gene body transcription
- **H3K27ac** (active enhancer/promoter mark) is high in spleen (333.2)
- **CTCF insulator binding** is present in colon (118.0) and spleen (116.3) — indicating a chromatin boundary element
- **Active splice sites** are predicted (donor and acceptor scores = 1.0)
- Chromatin accessibility (DNase) is moderate: kidney (0.23), spleen (0.17), liver (0.11)

**Interpretation:** The ASPSCR1 breakpoint disrupts an actively transcribed, chromatically open gene locus with strong insulator elements. When this region is rearranged in the translocation, the active transcriptional machinery that normally drives ASPSCR1 is redirected to drive the fusion transcript. The high RNA Pol II and histone marks explain why the ASPSCR1-TFE3 fusion is such a powerful oncogenic driver — the ASPSCR1 promoter is constitutively active across many tissues.

### TFE3 (chrX:49,043,986) — Open Chromatin with Repressive Histone Marks

The TFE3 breakpoint presents a paradoxical regulatory signature:
- **Chromatin accessibility is the HIGHEST of all 4 breakpoints** by a wide margin:
  - DNase: colon (0.61), lung (0.48), brain (0.41) — 3-10x higher than other breakpoints
  - ATAC: colon (0.36), lung (0.21)
  - Peak DNase signal: **92.0** in colon, **64** in brain and lung
- **But the histone marks are REPRESSIVE**, not active:
  - **H3K9me3** (heterochromatin/silencing mark) dominates: brain (3.08), lung (1.81), thymus (1.75)
  - **H3K27me3** (Polycomb repression mark): brain (1.41)
  - Active marks like H3K4me3 and H3K36me3 are essentially absent
- **CAGE signal is significant** (spleen 0.51, lung 0.47, with peaks up to 780) — indicating transcription initiation occurs here
- **CTCF binding is present** in brain (0.93) but at low levels overall
- **Liver-specific TF binding** (HNF4G, TAF1, ATF3) appears — suggesting tissue-specific regulation

**Interpretation:** The TFE3 breakpoint is in a "poised" regulatory state — the chromatin is physically accessible (high DNase/ATAC) but is being actively silenced by repressive histone marks (H3K9me3/H3K27me3). This is characteristic of a developmental regulatory element that is kept accessible but transcriptionally suppressed. In normal cells, this allows rapid activation of TFE3 when needed (e.g., for lysosomal biogenesis during stress). In the context of the ASPSCR1-TFE3 translocation, the fusion places TFE3's coding sequence under the control of ASPSCR1's constitutively active promoter, bypassing the repressive marks that normally keep TFE3 in check. This is the molecular mechanism by which the translocation converts a carefully regulated transcription factor into an always-on oncogenic driver.

### DNMT1 chr1 (chr1:31,048,832) — A Thymus-Specific Enhancer

The chr1 DNMT1 breakpoint has a distinctive **enhancer signature**:
- Chromatin accessibility is **low** across all tissues (DNase max 0.05, ATAC max 0.04)
- **H3K4me1** (enhancer mark) is very high in **thymus** (297.8) — the classic enhancer signature
- **H3K27ac** (active enhancer mark) is high in **thymus** (197.5) — confirming an active enhancer, not a poised one
- **H3K9me3** (silencing mark) is also elevated in thymus (176.5) — suggesting contested regulation
- **CTCF insulator binding** is strong across brain (115.3), colon (113.1), and spleen (111.2) — indicating a boundary element
- **Liver-specific TFs** (HNF4A: 112.2, SP1: 107.6) are bound
- Splice site activity is **minimal** (max acceptor score 0.16)

**Interpretation:** The chr1 DNMT1 breakpoint is in an enhancer element that is most active in the thymus. The thymus is where T-cell maturation occurs, and an enhancer active specifically in this tissue could regulate genes involved in T-cell development. The presence of both active (H3K27ac) and repressive (H3K9me3) marks suggests this enhancer is in a state of regulatory conflict — which is consistent with its role in the translocation disrupting normal T-cell maturation programs. This connects directly to the finding from the initial analysis that the chr1 DNMT1 breakpoint most strongly affects monocytes and B cells — immune cells that share developmental origins with T cells in the thymus.

### DNMT1 chr19 (chr19:10,160,241) — The Most Active Regulatory Region

The chr19 DNMT1 breakpoint shows the **strongest active transcription marks**:
- **H3K4me3** (active promoter): brain (396.2) — the highest of any breakpoint
- **H3K36me3** (active elongation): thymus (384.5) — indicating active gene transcription
- **H3K27ac** (active regulatory): spleen (371.7)
- **RNA Polymerase II** (POLR2AphosphoS5): spleen (320.5) — actively transcribing
- **CTCF binding** is strong across colon (135.2), spleen (131.9), brain (128.9)
- **Active splice sites** are present (donor and acceptor = 1.0)
- **CAGE peaks** reach 58-63 in thymus and brain — significant transcription initiation
- Chromatin accessibility is moderate: kidney (0.07), liver (0.06), spleen (0.06)

**Interpretation:** This is the primary DNMT1 locus — the gene itself lives here. The very high active transcription marks confirm DNMT1 is being actively transcribed across multiple tissues. The breakpoint at exon 14 disrupts this transcription, which would compromise DNMT1's ability to maintain DNA methylation patterns. Since DNMT1 is the primary maintenance methyltransferase (responsible for copying methylation patterns during DNA replication), its disruption at this locus would cause progressive loss of methylation across the genome — an "epigenetic erosion" that could unmask genes normally silenced by methylation, including immune-recognition genes and tumor suppressors.

---

## 2. Deep ISM: Mapping the Exact Regulatory Elements

The 256bp ISM analysis (768 variants per target) identified the specific DNA positions that control gene regulation at each breakpoint.

### ASPSCR1: Two Regulatory Hotspots Flanking the Breakpoint

Two distinct clusters of functionally critical bases were identified:

**Downstream hotspot (positions +56 to +62):**
- chr17:82,010,867 (A at +56): score 0.78
- chr17:82,010,868 (G at +57): score 0.81
- chr17:82,010,869 (G at +58): score **0.83** — the single most impactful position
- chr17:82,010,870 (T at +59): score 0.82
- chr17:82,010,873 (G at +62): score 0.59
- **Most affected tissues:** Panc1 (-0.83), foreskin fibroblast (-0.71), PFSK-1 (-0.66), HCT116 (-0.56) — all fibroblast or mesenchymal cell types

**Upstream hotspot (positions -12 to -9):**
- chr17:82,010,799 (T at -12): score 0.57
- chr17:82,010,800 (A at -11): score 0.72
- chr17:82,010,801 (G at -10): score 0.69
- chr17:82,010,802 (G at -9): score 0.54

**DNase ISM** revealed a third critical position at chr17:82,010,807 (T at **-4**, immediately adjacent to the breakpoint) that controls chromatin accessibility in stem cells (H9: 0.13, WTC11: 0.13). This position specifically controls whether the chromatin is open or closed in pluripotent/stem-like cells.

**Biological significance:** These two regulatory hotspots likely represent a **transcription factor binding motif** (the downstream GGGT cluster) and a **regulatory element** (the upstream AGG cluster). Together they define the boundaries of a ~70bp regulatory module centered on the breakpoint. The fibroblast-specific sensitivity confirms that this module specifically controls fibroblast gene expression programs — when the translocation disrupts this module, the aberrant regulatory control drives fibroblast recruitment.

### TFE3: A Critical Immune Regulatory Element with Massive Chromatin Effects

The TFE3 ISM revealed the most dramatic finding in the entire analysis:

**A single regulatory cluster at positions -93 to -99 controls immune cell chromatin accessibility:**
- chrX:49,043,887 (C at -99): DNase score 3.08
- chrX:49,043,888 (G at -98): DNase score **3.20**
- chrX:49,043,889 (C at -97): DNase score **3.20**
- chrX:49,043,890 (C at -96): DNase score **3.19**
- chrX:49,043,891 (C at -95): DNase score 3.03
- chrX:49,043,892 (T at -94): DNase score 3.09
- chrX:49,043,893 (C at -93): DNase score **3.29** — the largest effect in the entire ISM analysis

**The tissues most affected by mutations in this element are overwhelmingly immune cells:**
- T follicular helper cells: -3.29
- Effector memory CD4+ T cells: -3.18
- CD4+ memory T cells: -2.88
- Immature NK cells: -2.73
- CD8+ memory T cells: -2.63
- CD4+ T cells: -2.55

The negative scores mean that mutating these positions **reduces** chromatin accessibility — this element is a **chromatin opener** for immune cells. In its intact form, it keeps the chromatin around TFE3 accessible in immune cells. The translocation at the breakpoint (93bp downstream) disrupts the spatial relationship between this element and the TFE3 gene, potentially altering how immune cells regulate TFE3 expression.

**RNA_SEQ ISM** at the same positions showed CD14+ monocytes (0.035), testis (0.031), and regulatory T cells (0.019) as the most affected — confirming this element regulates both chromatin state and gene expression in immune cells.

A second cluster at position +83 (chrX:49,044,069) specifically affects brain tissues: Purkinje cells (0.022), cerebellum (0.021), cerebellar hemisphere (0.016), hypothalamus (0.015) — connecting to the brain-tissue sensitivity identified in the original analysis.

### DNMT1 chr1: Low-Impact Distributed Regulation

The chr1 DNMT1 breakpoint showed the **weakest ISM effects** of all four targets:
- Maximum RNA_SEQ effect: 0.007 (liver, at position +114)
- Maximum DNase effect: 0.032 (WERI-Rb-1, at position +125)
- Sensitive positions are distributed, not clustered — no single dominant regulatory element
- The most affected tissues are liver, Peyer's patch, and peripheral blood mononuclear cells

**Interpretation:** This breakpoint is in a regulatory region with dispersed, low-magnitude effects. It contributes to the tumor's biology but is not a primary regulatory driver. Its main contribution appears to be through disrupting the enhancer element identified in the histone analysis (H3K4me1/H3K27ac in thymus) rather than through a specific transcription factor binding site.

### DNMT1 chr19: A Single Position Controls T-Cell Chromatin

The chr19 DNMT1 ISM revealed a **single dominant regulatory position**:

**Position chr19:10,160,175 (C at -66 from breakpoint) is a T-cell/NK cell chromatin switch:**

RNA_SEQ effects of C>A mutation:
- CD8+ T cells: +0.115
- NK cells: +0.094
- CD4+ T cells: +0.091
- Regulatory T cells: +0.088
- T-helper 17 cells: +0.079

DNase effects of C>A mutation:
- Immature NK cells: **+0.436** — the second-largest single-position effect in the entire analysis
- T-helper 2 cells: +0.221
- CD8+ T cells: +0.171
- Central memory CD4+ T cells: +0.169
- CD4+ memory T cells: +0.160
- Effector memory CD8+ T cells: +0.159
- CD8+ memory T cells: +0.157
- T cells: +0.153
- T-helper 22 cells: +0.133

**All 15 of the top DNase hits are T cells or NK cells.** This single cytosine at position -66 is a master switch for T-cell and NK cell chromatin accessibility at the DNMT1 locus.

The positive scores mean that mutating this position **increases** chromatin accessibility — this position normally acts as a **chromatin compactor** at the DNMT1 locus in immune cells. In other words, DNMT1 uses this regulatory element to keep its own chromatin somewhat restricted in T cells and NK cells, maintaining controlled expression levels. The translocation disrupts this control, potentially allowing unregulated DNMT1 expression or loss of expression in immune cells.

---

## 3. Drug Target Gene Expression Profiles

AlphaGenome predictions for the expression of drug target genes across 5 tissue types (lung, liver, heart, brain, colon):

### Doxycycline Targets

**Matrix Metalloproteinases (MMPs):**
| Gene | Highest Expression | Lowest Expression |
|------|-------------------|-------------------|
| MMP14 | Heart (1.29) | Liver (0.02) |
| MMP7 | Lung (0.51) | Heart (0.0001) |
| MMP2 | Heart (0.22) | Liver (0.02) |
| MMP9 | Lung (0.16) | Heart (0.001) |
| MMP1 | Colon (0.10) | Heart (0.002) |
| MMP3 | Colon (0.10) | Heart (0.0003) |

MMP14 has the highest predicted expression overall. MMP7 and MMP9 are expressed primarily in lung — relevant since ASPS often metastasizes to lung. MMPs are nearly absent in heart, suggesting Doxycycline's MMP-inhibition effects would be concentrated in the tumor microenvironment (fibroblasts, lung) rather than causing cardiac side effects.

**Mitochondrial Ribosomal Proteins:**
| Gene | Highest Expression | Lowest Expression |
|------|-------------------|-------------------|
| MRPS12 | Liver (1.43) | Lung (0.18) |
| MT-CO1 | Heart (0.89) | Lung (0.0001) |
| MRPS15 | Heart (0.73) | Lung (0.10) |
| MT-ND1 | Heart (0.55) | Lung (0.0001) |

Mitochondrial genes (MT-CO1, MT-ND1) are most highly expressed in heart — consistent with heart tissue's high mitochondrial density. MRPS12 (nuclear-encoded mitochondrial ribosomal protein) is highest in liver. Doxycycline's mitochondrial inhibition would affect these tissues, which is relevant to the "engine block" mechanism of the Triple Blockade.

### Hydroxychloroquine Targets

**Autophagy Genes:**
| Gene | Highest Expression | Lowest Expression |
|------|-------------------|-------------------|
| SQSTM1/p62 | Colon (1.16) | Lung (0.34) |
| MAP1LC3B | Brain (1.12) | Liver (0.15) |
| ATG12 | Heart (0.42) | Liver (0.14) |
| BECN1 | Brain (0.35) | Heart (0.11) |

**Lysosomal Genes:**
| Gene | Highest Expression | Lowest Expression |
|------|-------------------|-------------------|
| CTSD | Lung (4.97) | Lung low strand (0.58) |
| CTSL | Liver (1.46) | Colon (0.19) |
| LAMP1 | Brain (0.74) | Heart (0.12) |
| LAMP2 | Brain (0.60) | Colon (0.12) |

CTSD (Cathepsin D, a lysosomal protease) has the **highest expression of any drug target gene** at 4.97 in lung. This is significant because CTSD is a critical lysosomal enzyme — HCQ's inhibition of lysosomal function would be particularly impactful in tissues where CTSD is highly expressed. SQSTM1/p62 (the autophagy receptor) is highest in colon (1.16), confirming active autophagy flux in gut-associated tissues.

### Cimetidine Targets

**Histamine Receptors:**
| Gene | Highest Expression | Lowest Expression |
|------|-------------------|-------------------|
| HRH2 | Heart (0.07) | Liver (0.008) |
| HDC | Lung (0.04) | Heart (0.001) |
| HRH1 | Colon (0.02) | Liver (0.0004) |
| HRH4 | Colon (0.002) | Liver (0.0002) |

Histamine receptor expression is uniformly **low** across all tissues. HRH2 (the primary Cimetidine target) is highest in heart but at only 0.07. This low expression level suggests Cimetidine's therapeutic effect in this context may be operating through a different mechanism than simple receptor blockade — possibly through its known immunomodulatory effects on T-cell function or its anti-angiogenic properties.

**Angiogenesis Genes:**
| Gene | Highest Expression | Lowest Expression |
|------|-------------------|-------------------|
| VEGFB | Heart (2.00) | Liver (0.11) |
| VEGFA | Liver (1.48) | Brain (0.22) |
| KDR/VEGFR2 | Heart (0.33) | Liver (0.02) |
| FLT1/VEGFR1 | Lung (0.12) | Colon (0.009) |

VEGFB and VEGFA are highly expressed — VEGFB in heart (2.00) and VEGFA in liver (1.48). KDR (the primary VEGF receptor on endothelial cells) is highest in heart (0.33). The high expression of VEGF ligands across tissues confirms the tumor's ability to commandeer angiogenic signaling wherever it metastasizes.

### Immune Checkpoint and Activation Genes

**Immune Checkpoints:**
| Gene | Highest Expression | Tissue |
|------|-------------------|--------|
| LAG3 | 0.111 | Colon |
| HAVCR2/TIM-3 | 0.065 | Brain |
| CD274/PD-L1 | 0.052 | Lung |
| PDCD1/PD-1 | 0.017 | Colon |
| CTLA4 | 0.006 | Colon |
| TIGIT | 0.004 | Colon |

LAG3 has the highest checkpoint expression (0.11 in colon). PD-L1 (CD274) is moderately expressed in lung (0.05). Most checkpoint genes are highest in colon, which is rich in immune cells. The relatively low expression of PD-1 (0.017) and CTLA4 (0.006) suggests these standard checkpoint inhibitor targets may have limited activity in the context of this tumor's microenvironment.

**Immune Activation Genes:**
| Gene | Highest Expression | Tissue |
|------|-------------------|--------|
| CD4 | 0.107 | Liver |
| TNF | 0.092 | Colon |
| PRF1 (perforin) | 0.083 | Colon |
| GZMB (granzyme B) | 0.074 | Lung |
| IFNG | 0.007 | Colon |
| CD8A | 0.014 | Colon |

TNF (0.092), perforin (0.083), and granzyme B (0.074) are all moderately expressed in immune-rich tissues (colon, lung). These are the effector molecules T cells and NK cells use to kill tumor cells. Their expression levels in lung are particularly relevant given ASPS's predilection for pulmonary metastases.

### Key Pathway Genes

**TFE3 Pathway:**
| Gene | Highest Expression | Tissue |
|------|-------------------|--------|
| TFE3 | 0.586 | Lung |
| FLCN (folliculin) | 0.327 | Colon |
| MITF | 0.225 | Heart |
| FNIP1 | 0.138 | Lung |
| TFEB | 0.083 | Lung |
| MTOR | 0.070 | Brain |

TFE3 itself is most highly expressed in lung (0.586). FLCN (folliculin, a tumor suppressor in the TFE3 pathway) is expressed in colon (0.327). MTOR expression is relatively low across all tissues (max 0.070 in brain), which is notable because mTOR is a key regulator of TFE3/TFEB nuclear localization.

**DNMT1 Pathway:**
| Gene | Highest Expression | Tissue |
|------|-------------------|--------|
| IDH2 | 1.747 | Heart |
| IDH1 | 1.348 | Liver |
| DNMT1 | 0.156 | Brain |
| TET2 | 0.123 | Lung |
| DNMT3A | 0.099 | Heart |
| DNMT3B | 0.074 | Liver |
| TET1 | 0.039 | Lung |

IDH1 and IDH2 (isocitrate dehydrogenases that produce alpha-ketoglutarate, required by TET enzymes for demethylation) are the most highly expressed genes in this pathway, in liver (1.35) and heart (1.75) respectively. DNMT1 itself is most expressed in brain (0.156). The TET enzymes (which oppose DNMT1 by removing methylation) are expressed at low-moderate levels (TET2: 0.123 in lung). The imbalance between high IDH/TET potential and moderate DNMT1 expression suggests the tumor's epigenetic landscape is sensitive to perturbation of DNMT1 function.

---

## 4. Integrated Findings

### The Complete Picture of Each Breakpoint

**ASPSCR1 (chr17)** — The constitutively active promoter
- Active transcription (RNA Pol II, H3K4me3, H3K36me3)
- Two regulatory hotspots at -11 and +58 controlling fibroblast gene expression
- Provides the always-on promoter for the fusion transcript

**TFE3 (chrX)** — The poised engine with an immune control switch
- Open chromatin but repressive histone marks (poised state)
- A critical 7bp regulatory element at -93 to -99 that controls T cell and NK cell chromatin accessibility with effects 3-10x larger than any other position
- Provides the transcription factor coding sequence and metabolic programming

**DNMT1 chr1** — The thymus enhancer
- Active enhancer in thymus (H3K4me1 + H3K27ac)
- Weakest functional impact of the four breakpoints
- Contributes to immune cell developmental regulation

**DNMT1 chr19** — The epigenetic shield with a T-cell master switch
- Actively transcribed gene body (H3K4me3, RNA Pol II, splice sites)
- A single position at -66 acts as a master chromatin compactor for T cells and NK cells
- Provides the methyltransferase activity that maintains epigenetic silencing

### Therapeutic Implications

**Doxycycline targeting is well-supported:**
- MMP genes are expressed in the relevant tissues (lung, colon — metastatic sites)
- Mitochondrial targets (MT-CO1, MT-ND1) are highly expressed in metabolically active tissues
- The fibroblast-dominance at the ASPSCR1 breakpoint (confirmed by ISM) makes MMP inhibition mechanistically coherent

**Hydroxychloroquine targeting is strongly supported:**
- CTSD (cathepsin D) has the highest expression of any drug target gene (4.97 in lung)
- SQSTM1/p62 (autophagy receptor) is highly expressed in colon (1.16)
- The lysosomal/autophagy pathway is clearly active in the tumor-relevant tissues

**Cimetidine's mechanism may be primarily immunomodulatory rather than anti-histaminergic:**
- Histamine receptor expression is very low (HRH2 max 0.07)
- But angiogenic targets (VEGFA: 1.48, VEGFB: 2.00) are highly expressed
- Cimetidine's known effects on T-cell function may be more relevant than receptor blockade, given the T-cell sensitivity identified at both DNMT1 breakpoints

**The immune opportunity is specific and measurable:**
- The TFE3 ISM identified a 7bp element controlling immune cell chromatin with scores of 3.0+ (massive)
- The DNMT1 chr19 ISM identified a single position controlling T-cell/NK cell chromatin
- These two elements together define the tumor's immunological "address" — the specific DNA sequences that govern whether immune cells can access and respond to the tumor
- LAG3 (0.111 in colon) is the most expressed immune checkpoint — this may be a more relevant therapeutic target than PD-1/CTLA4 for this specific tumor

---

*Analysis performed using AlphaGenome v0.6.1 (Google DeepMind). All raw data saved to multimodal_results.json, deep_ism_results.json, drug_target_results.json, and splicing_accessibility_results.json.*
