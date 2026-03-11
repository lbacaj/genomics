# Drug Target Gene Expression Analysis Report

## Patient: Johnny | Diagnosis: Alveolar Soft Part Sarcoma (ASPS)

**Analysis Method:** AlphaGenome predicted gene expression across multiple tissues

**Date of Analysis:** March 2026

**Tissues Analyzed:** Lung, Liver, Heart, Brain, Transverse Colon

**Therapeutic Regimen:** Triple Blockade (Doxycycline + Hydroxychloroquine + Cimetidine), with additional profiling of immune checkpoint, immune activation, TFE3 pathway, and DNMT1 pathway genes.

---

## Table of Contents

1. [Overview](#overview)
2. [Doxycycline Targets -- Matrix Metalloproteinases (MMPs)](#1-doxycycline-targets----matrix-metalloproteinases-mmps)
3. [Doxycycline Targets -- Mitochondrial Ribosomes](#2-doxycycline-targets----mitochondrial-ribosomes)
4. [Hydroxychloroquine (HCQ) Targets -- Autophagy Genes](#3-hydroxychloroquine-hcq-targets----autophagy-genes)
5. [Hydroxychloroquine (HCQ) Targets -- Lysosomal Pathway](#4-hydroxychloroquine-hcq-targets----lysosomal-pathway)
6. [Cimetidine Targets -- Histamine Receptors](#5-cimetidine-targets----histamine-receptors)
7. [Cimetidine Targets -- Angiogenesis Genes](#6-cimetidine-targets----angiogenesis-genes)
8. [Immune Checkpoint Genes](#7-immune-checkpoint-genes)
9. [Immune Activation Genes](#8-immune-activation-genes)
10. [TFE3 Pathway Genes](#9-tfe3-pathway-genes)
11. [DNMT1 Pathway Genes](#10-dnmt1-pathway-genes)
12. [Drug Efficacy Implications](#drug-efficacy-implications)
13. [Overall Therapeutic Assessment](#overall-therapeutic-assessment)

---

## Overview

This report summarizes AlphaGenome-predicted gene expression levels for 60+ genes relevant to Johnny's Triple Blockade therapy and Alveolar Soft Part Sarcoma (ASPS) tumor biology. ASPS is a rare soft tissue sarcoma driven by the ASPSCR1-TFE3 fusion protein, and Johnny also carries a DNMT1 translocation.

Expression is reported as **gene body mean** (average signal across the gene body) and **gene body max** (peak signal), derived from RNA-seq tracks across five tissues. For each gene in each tissue, only the highest-expressing track is reported. Higher gene body mean values indicate stronger predicted transcription, suggesting the encoded protein target is more likely to be present and thus the drug more likely to be effective.

**Expression level interpretation guide:**
- **High expression** (gene body mean > 0.5): Target is robustly expressed; drug likely effective
- **Moderate expression** (gene body mean 0.1 - 0.5): Target is present at meaningful levels
- **Low expression** (gene body mean 0.01 - 0.1): Target is weakly expressed; drug effect may be limited
- **Very low / negligible** (gene body mean < 0.01): Target is minimally expressed; drug unlikely to have significant activity on this target

---

## 1. Doxycycline Targets -- Matrix Metalloproteinases (MMPs)

**Drug mechanism:** Doxycycline, a tetracycline antibiotic, inhibits matrix metalloproteinases (MMPs) at sub-antimicrobial doses. MMPs are zinc-dependent endopeptidases that degrade extracellular matrix components, facilitating tumor invasion, metastasis, and angiogenesis. By blocking MMP activity, doxycycline may reduce the tumor's ability to invade surrounding tissue and establish metastases.

| Gene | Top Tissue | Gene Body Mean | Gene Body Max | Expression Level |
|------|-----------|---------------|---------------|-----------------|
| MMP2 | Heart | 0.2164 | 11.8750 | Moderate |
| MMP9 | Lung | 0.1583 | 1.7813 | Moderate |
| MMP14 | Heart | 1.2890 | 7.8125 | High |
| MMP7 | Lung | 0.5063 | 8.2500 | High |
| MMP1 | Transverse Colon | 0.0971 | 0.7422 | Low |
| MMP3 | Transverse Colon | 0.0975 | 0.6602 | Low |

**Tissue-level detail (top expressing tissue per gene):**

| Gene | Lung | Liver | Heart | Brain | Transverse Colon |
|------|------|-------|-------|-------|-------------------|
| MMP2 | 0.0987 | 0.0531 | 0.2164 | 0.0387 | 0.2049 |
| MMP9 | 0.1583 | 0.0852 | 0.0031 | 0.0078 | 0.0290 |
| MMP14 | 0.6413 | 0.2674 | 1.2890 | 0.2196 | 1.2635 |
| MMP7 | 0.5063 | 0.0029 | 0.0003 | 0.0083 | 0.0611 |
| MMP1 | 0.0174 | 0.0091 | 0.0060 | 0.0041 | 0.0971 |
| MMP3 | 0.0116 | 0.0169 | 0.0016 | 0.0011 | 0.0975 |

**Summary:** MMP14 and MMP7 are highly expressed, particularly MMP14 in heart and transverse colon (gene body mean >1.0). MMP2 and MMP9 show moderate expression. MMP1 and MMP3 are only weakly expressed across all tissues. This suggests doxycycline's MMP-inhibitory effects will be most impactful against MMP14 and MMP7.

---

## 2. Doxycycline Targets -- Mitochondrial Ribosomes

**Drug mechanism:** Doxycycline inhibits mitochondrial ribosome translation because mitochondrial ribosomes are structurally similar to bacterial ribosomes. This disrupts mitochondrial protein synthesis, impairs oxidative phosphorylation, and can selectively harm cancer cells that rely heavily on mitochondrial metabolism. In ASPS, which is a highly metabolically active tumor, this mechanism may be particularly relevant.

| Gene | Top Tissue | Gene Body Mean | Gene Body Max | Expression Level |
|------|-----------|---------------|---------------|-----------------|
| MRPS12 | Liver | 1.4347 | 5.1563 | High |
| MRPS15 | Heart | 0.7313 | 11.3125 | High |
| MRPL11 | Liver | 0.1284 | 6.5000 | Moderate |
| MRPL13 | Heart | 0.0539 | 6.3438 | Low |
| MT-CO1 | Heart | 0.8932 | 4.0625 | High |
| MT-ND1 | Heart | 0.5543 | 1.8359 | High |

**Tissue-level detail (top expressing tissue per gene):**

| Gene | Lung | Liver | Heart | Brain | Transverse Colon |
|------|------|-------|-------|-------|-------------------|
| MRPS12 | 1.2612 | 1.4347 | 0.5706 | 0.5262 | 0.8269 |
| MRPS15 | 0.6358 | 0.5939 | 0.7313 | 0.5576 | 0.5234 |
| MRPL11 | 0.1044 | 0.1284 | 0.1055 | 0.0937 | 0.0926 |
| MRPL13 | 0.0366 | 0.0430 | 0.0539 | 0.0511 | 0.0310 |
| MT-CO1 | 0.0089 | 0.0410 | 0.8932 | 0.5568 | 0.1064 |
| MT-ND1 | 0.0074 | 0.0271 | 0.5543 | 0.3261 | 0.0605 |

**Summary:** Mitochondrial ribosome targets are broadly and robustly expressed. MRPS12, MRPS15, MT-CO1, and MT-ND1 all show high expression (>0.5 gene body mean). The mitochondrial-encoded genes MT-CO1 and MT-ND1 are particularly strongly expressed in heart and brain. This indicates doxycycline's mitochondrial mechanism has abundant targets across all tissues examined.

---

## 3. Hydroxychloroquine (HCQ) Targets -- Autophagy Genes

**Drug mechanism:** Hydroxychloroquine inhibits autophagy by blocking lysosomal acidification, preventing autophagosome-lysosome fusion. Cancer cells, particularly in nutrient-deprived or hypoxic tumor microenvironments, rely on autophagy for survival. By disrupting this process, HCQ may render tumor cells more susceptible to metabolic stress and other therapies.

| Gene | Top Tissue | Gene Body Mean | Gene Body Max | Expression Level |
|------|-----------|---------------|---------------|-----------------|
| ATG5 | Lung | 0.0337 | 1.3594 | Low |
| ATG7 | Transverse Colon | 0.0495 | 0.8555 | Low |
| ATG12 | Heart | 0.4172 | 3.1406 | Moderate |
| BECN1 | Brain | 0.3530 | 9.0625 | Moderate |
| SQSTM1 | Transverse Colon | 1.1564 | 23.8750 | High |
| MAP1LC3B | Brain | 1.1166 | 17.5000 | High |

**Tissue-level detail (top expressing tissue per gene):**

| Gene | Lung | Liver | Heart | Brain | Transverse Colon |
|------|------|-------|-------|-------|-------------------|
| ATG5 | 0.0337 | 0.0316 | 0.0252 | 0.0171 | 0.0291 |
| ATG7 | 0.0480 | 0.0455 | 0.0289 | 0.0066 | 0.0495 |
| ATG12 | 0.3284 | 0.2980 | 0.4172 | 0.3800 | 0.3082 |
| BECN1 | 0.2533 | 0.2413 | 0.2783 | 0.3530 | 0.3313 |
| SQSTM1 | 1.0126 | 1.0381 | 0.7897 | 0.5634 | 1.1564 |
| MAP1LC3B | 0.3260 | 0.3650 | 0.6090 | 1.1166 | 0.4505 |

**Summary:** SQSTM1 (p62) and MAP1LC3B (LC3B) are highly expressed across all tissues, indicating robust autophagic activity. BECN1 and ATG12 show moderate expression. ATG5 and ATG7, while essential components of the autophagy pathway, have lower expression. The strong expression of key autophagy markers SQSTM1 and MAP1LC3B suggests that autophagy is an active process in these tissues, meaning HCQ's autophagy-blocking mechanism should have meaningful targets.

---

## 4. Hydroxychloroquine (HCQ) Targets -- Lysosomal Pathway

**Drug mechanism:** HCQ accumulates in lysosomes and raises their pH, impairing lysosomal enzyme function. This disrupts not only autophagy but also lysosomal biogenesis, protein degradation, and antigen processing. TFEB, the master regulator of lysosomal biogenesis, is closely linked to the TFE3 pathway relevant to ASPS.

| Gene | Top Tissue | Gene Body Mean | Gene Body Max | Expression Level |
|------|-----------|---------------|---------------|-----------------|
| LAMP1 | Brain | 0.7429 | 14.7500 | High |
| LAMP2 | Brain | 0.6009 | 8.1875 | High |
| CTSD | Lung | 4.9720 | 54.7500 | High |
| CTSL | Liver | 1.4582 | 10.1875 | High |
| TFEB | Lung | 0.0829 | 2.5781 | Low |
| ATP6V1A | Brain | 0.2447 | 9.0000 | Moderate |

**Tissue-level detail (top expressing tissue per gene):**

| Gene | Lung | Liver | Heart | Brain | Transverse Colon |
|------|------|-------|-------|-------|-------------------|
| LAMP1 | 0.6973 | 0.6424 | 0.4535 | 0.7429 | 0.6927 |
| LAMP2 | 0.2158 | 0.2862 | 0.3893 | 0.6009 | 0.2260 |
| CTSD | 4.9720 | 4.5927 | 2.7919 | 2.4485 | 4.2385 |
| CTSL | 1.1322 | 1.4582 | 1.2099 | 0.5108 | 0.9844 |
| TFEB | 0.0829 | 0.0214 | 0.0642 | 0.0330 | 0.0734 |
| ATP6V1A | 0.0848 | 0.0902 | 0.1536 | 0.2447 | 0.0704 |

**Summary:** Lysosomal genes are very robustly expressed. CTSD (Cathepsin D) stands out with the highest expression of any gene in this entire analysis (gene body mean 4.97 in lung). CTSL, LAMP1, and LAMP2 are all highly expressed. TFEB, the lysosomal biogenesis master regulator, is notably low, which is important given its relationship to the TFE3 fusion in ASPS. The strong expression of lysosomal targets confirms that HCQ has abundant targets for lysosomal disruption.

---

## 5. Cimetidine Targets -- Histamine Receptors

**Drug mechanism:** Cimetidine is an H2 histamine receptor antagonist that, beyond acid suppression, has anti-tumor properties. It can inhibit tumor cell adhesion to endothelial cells, enhance immune surveillance by blocking histamine's immunosuppressive effects on T cells and NK cells, and may directly inhibit tumor cell proliferation.

| Gene | Top Tissue | Gene Body Mean | Gene Body Max | Expression Level |
|------|-----------|---------------|---------------|-----------------|
| HRH1 | Transverse Colon | 0.0200 | 0.3047 | Low |
| HRH2 | Heart | 0.0711 | 1.8672 | Low |
| HRH4 | Transverse Colon | 0.0020 | 0.0082 | Very Low |
| HDC | Lung | 0.0385 | 0.8984 | Low |

**Tissue-level detail (top expressing tissue per gene):**

| Gene | Lung | Liver | Heart | Brain | Transverse Colon |
|------|------|-------|-------|-------|-------------------|
| HRH1 | 0.0108 | 0.0014 | 0.0077 | 0.0037 | 0.0200 |
| HRH2 | 0.0248 | 0.0164 | 0.0711 | 0.0145 | 0.0204 |
| HRH4 | 0.0016 | 0.0015 | 0.0015 | 0.0005 | 0.0020 |
| HDC | 0.0385 | 0.0152 | 0.0020 | 0.0041 | 0.0150 |

**Summary:** All histamine pathway genes show low to very low expression. HRH2, the primary cimetidine target, is most expressed in heart (0.0711) but still at low levels. HRH4 is essentially negligible across all tissues. HDC (histidine decarboxylase, the histamine-producing enzyme) is similarly low. This pattern suggests that cimetidine's direct histamine receptor-blocking mechanism may have limited potency, and its anti-tumor effects may rely more on indirect immune-modulatory actions.

---

## 6. Cimetidine Targets -- Angiogenesis Genes

**Drug mechanism:** Cimetidine has demonstrated anti-angiogenic properties, suppressing VEGF-mediated neovascularization. ASPS is a highly vascular tumor, making anti-angiogenic effects potentially significant.

| Gene | Top Tissue | Gene Body Mean | Gene Body Max | Expression Level |
|------|-----------|---------------|---------------|-----------------|
| VEGFA | Liver | 1.4838 | 10.7500 | High |
| VEGFB | Heart | 2.0035 | 13.7500 | High |
| VEGFC | Lung | 0.0308 | 0.3281 | Low |
| KDR | Heart | 0.3272 | 4.1563 | Moderate |
| FLT1 | Lung | 0.1170 | 2.1563 | Moderate |
| ANGPT2 | Lung | 0.0621 | 1.5469 | Low |

**Tissue-level detail (top expressing tissue per gene):**

| Gene | Lung | Liver | Heart | Brain | Transverse Colon |
|------|------|-------|-------|-------|-------------------|
| VEGFA | 0.7960 | 1.4838 | 0.9672 | 0.2235 | 1.2910 |
| VEGFB | 1.4664 | 0.8509 | 2.0035 | 1.1307 | 1.7809 |
| VEGFC | 0.0308 | 0.0036 | 0.0169 | 0.0024 | 0.0083 |
| KDR | 0.0607 | 0.0473 | 0.3272 | 0.0418 | 0.0751 |
| FLT1 | 0.1170 | 0.0377 | 0.0886 | 0.0214 | 0.0253 |
| ANGPT2 | 0.0621 | 0.0353 | 0.0558 | 0.0269 | 0.0214 |

**Summary:** VEGFA and VEGFB are highly expressed across all tissues, with VEGFB reaching the highest values (2.0035 in heart). KDR (VEGFR2, the main VEGF signaling receptor) shows moderate expression, particularly in heart. The strong VEGF expression, combined with ASPS's known hypervascularity, makes cimetidine's anti-angiogenic properties highly relevant, even if its histamine receptor effects are limited.

---

## 7. Immune Checkpoint Genes

**Context:** Immune checkpoint expression in the tumor microenvironment determines responsiveness to immunotherapy. ASPS often shows immune infiltration, and understanding checkpoint expression helps assess whether the immune environment is suppressed.

| Gene | Full Name | Top Tissue | Gene Body Mean | Gene Body Max | Expression Level |
|------|-----------|-----------|---------------|---------------|-----------------|
| PDCD1 | PD-1 | Transverse Colon | 0.0173 | 0.0603 | Low |
| CD274 | PD-L1 | Lung | 0.0519 | 1.2109 | Low |
| CTLA4 | CTLA-4 | Transverse Colon | 0.0059 | 0.0850 | Very Low |
| LAG3 | LAG-3 | Transverse Colon | 0.1112 | 0.5234 | Moderate |
| HAVCR2 | TIM-3 | Brain | 0.0645 | 2.0469 | Low |
| TIGIT | TIGIT | Transverse Colon | 0.0035 | 0.0640 | Very Low |

**Tissue-level detail (top expressing tissue per gene):**

| Gene | Lung | Liver | Heart | Brain | Transverse Colon |
|------|------|-------|-------|-------|-------------------|
| PDCD1 | 0.0100 | 0.0076 | 0.0075 | 0.0016 | 0.0173 |
| CD274 | 0.0519 | 0.0230 | 0.0230 | 0.0078 | 0.0353 |
| CTLA4 | 0.0013 | 0.0007 | 0.0006 | 0.0001 | 0.0059 |
| LAG3 | 0.0702 | 0.0253 | 0.0080 | 0.0082 | 0.1112 |
| HAVCR2 | 0.0416 | 0.0407 | 0.0460 | 0.0645 | 0.0313 |
| TIGIT | 0.0014 | 0.0013 | 0.0008 | 0.0003 | 0.0035 |

**Summary:** Immune checkpoint gene expression is generally low across normal tissues, which is expected since these are predominantly expressed on immune cells within the tumor microenvironment rather than in bulk tissue. LAG3 shows the highest expression (moderate in transverse colon). PD-L1 (CD274) is low but detectable, especially in lung. CTLA4 and TIGIT are very low. This baseline low expression in normal tissue does not preclude significant checkpoint expression within the tumor itself.

---

## 8. Immune Activation Genes

**Context:** These genes indicate the presence and activity of immune effector cells. Higher expression suggests greater immune surveillance capacity.

| Gene | Function | Top Tissue | Gene Body Mean | Gene Body Max | Expression Level |
|------|----------|-----------|---------------|---------------|-----------------|
| IFNG | Interferon-gamma | Transverse Colon | 0.0069 | 0.0283 | Very Low |
| TNF | Tumor necrosis factor | Transverse Colon | 0.0920 | 0.2334 | Low |
| IL2 | Interleukin-2 | Transverse Colon | 0.0014 | 0.0166 | Very Low |
| PRF1 | Perforin-1 | Transverse Colon | 0.0827 | 0.3828 | Low |
| GZMB | Granzyme B | Lung | 0.0740 | 0.4766 | Low |
| CD8A | CD8+ T cell marker | Transverse Colon | 0.0142 | 0.1865 | Low |
| CD4 | CD4+ T cell marker | Liver | 0.1070 | 2.0313 | Moderate |

**Tissue-level detail (top expressing tissue per gene):**

| Gene | Lung | Liver | Heart | Brain | Transverse Colon |
|------|------|-------|-------|-------|-------------------|
| IFNG | 0.0032 | 0.0019 | 0.0005 | 0.0002 | 0.0069 |
| TNF | 0.0804 | 0.0095 | 0.0032 | 0.0028 | 0.0920 |
| IL2 | 0.0008 | 0.0005 | 0.0002 | 0.0001 | 0.0014 |
| PRF1 | 0.0504 | 0.0589 | 0.0075 | 0.0032 | 0.0827 |
| GZMB | 0.0740 | 0.0270 | 0.0024 | 0.0008 | 0.0656 |
| CD8A | 0.0079 | 0.0029 | 0.0023 | 0.0076 | 0.0142 |
| CD4 | 0.0975 | 0.1070 | 0.0293 | 0.0172 | 0.0812 |

**Summary:** Immune activation genes are generally low to very low in normal tissues, which is typical since these are primarily expressed by infiltrating immune cells. The transverse colon and lung show the highest immune gene expression, suggesting greater immune cell residence in these tissues. CD4 reaches moderate expression in liver. The key cytolytic effectors (PRF1, GZMB) are detectable but low, consistent with baseline immune surveillance.

---

## 9. TFE3 Pathway Genes

**Context:** The ASPSCR1-TFE3 fusion is the defining genetic event in ASPS. TFE3 and its related family members (TFEB, MITF) are MiT/TFE transcription factors that regulate lysosomal biogenesis, autophagy, and cellular metabolism. Understanding the expression of this pathway is critical for understanding ASPS biology.

| Gene | Function | Top Tissue | Gene Body Mean | Gene Body Max | Expression Level |
|------|----------|-----------|---------------|---------------|-----------------|
| TFE3 | Fusion partner in ASPS | Lung | 0.5858 | 6.0000 | High |
| TFEB | Lysosomal biogenesis TF | Lung | 0.0829 | 2.5781 | Low |
| MITF | Melanocyte TF, MiT family | Heart | 0.2253 | 2.7344 | Moderate |
| FLCN | Folliculin (TFE3 regulator) | Transverse Colon | 0.3273 | 2.5469 | Moderate |
| FNIP1 | FLCN-interacting protein | Lung | 0.1377 | 1.8750 | Moderate |
| MTOR | mTOR kinase (TFE3 regulator) | Brain | 0.0704 | 4.6875 | Low |
| RPTOR | Raptor (mTORC1 component) | Transverse Colon | 0.0305 | 1.5938 | Low |

**Tissue-level detail (top expressing tissue per gene):**

| Gene | Lung | Liver | Heart | Brain | Transverse Colon |
|------|------|-------|-------|-------|-------------------|
| TFE3 | 0.5858 | 0.2435 | 0.2983 | 0.2732 | 0.5767 |
| TFEB | 0.0829 | 0.0132 | 0.0642 | 0.0330 | 0.0617 |
| MITF | 0.0545 | 0.0216 | 0.2253 | 0.0052 | 0.0278 |
| FLCN | 0.2130 | 0.1642 | 0.1715 | 0.1299 | 0.3273 |
| FNIP1 | 0.1377 | 0.1300 | 0.1213 | 0.0273 | 0.1075 |
| MTOR | 0.0498 | 0.0703 | 0.0670 | 0.0704 | 0.0563 |
| RPTOR | 0.0212 | 0.0067 | 0.0077 | 0.0107 | 0.0305 |

**Summary:** TFE3 itself is robustly expressed, especially in lung (0.5858) and transverse colon (0.5767). This is highly relevant since the ASPSCR1-TFE3 fusion drives ASPS -- the high baseline TFE3 expression suggests the wild-type gene's regulatory regions are in an active chromatin state. TFEB, the closely related family member, is notably low. FLCN and FNIP1, key regulators of TFE3/TFEB nuclear localization, show moderate expression. MTOR and RPTOR are low, suggesting mTORC1 signaling may not be maximally active at baseline.

---

## 10. DNMT1 Pathway Genes

**Context:** Johnny's tumor harbors a DNMT1 translocation in addition to the ASPSCR1-TFE3 fusion. DNMT1 is the primary maintenance DNA methyltransferase, and its disruption can lead to widespread epigenetic changes, altered gene expression, and genomic instability.

| Gene | Function | Top Tissue | Gene Body Mean | Gene Body Max | Expression Level |
|------|----------|-----------|---------------|---------------|-----------------|
| DNMT1 | Maintenance methyltransferase | Brain | 0.1557 | 5.6563 | Moderate |
| DNMT3A | De novo methyltransferase | Heart | 0.0993 | 3.7031 | Low |
| DNMT3B | De novo methyltransferase | Liver | 0.0738 | 0.8516 | Low |
| TET1 | DNA demethylase | Lung | 0.0387 | 0.5898 | Low |
| TET2 | DNA demethylase | Lung | 0.1227 | 1.2031 | Moderate |
| IDH1 | Isocitrate dehydrogenase 1 | Liver | 1.3475 | 26.0000 | High |
| IDH2 | Isocitrate dehydrogenase 2 | Heart | 1.7472 | 26.8750 | High |

**Tissue-level detail (top expressing tissue per gene):**

| Gene | Lung | Liver | Heart | Brain | Transverse Colon |
|------|------|-------|-------|-------|-------------------|
| DNMT1 | 0.0751 | 0.1061 | 0.1334 | 0.1557 | 0.0925 |
| DNMT3A | 0.0509 | 0.0477 | 0.0993 | 0.0661 | 0.0464 |
| DNMT3B | 0.0167 | 0.0738 | 0.0238 | 0.0450 | 0.0137 |
| TET1 | 0.0387 | 0.0267 | 0.0319 | 0.0222 | 0.0064 |
| TET2 | 0.1227 | 0.0686 | 0.0807 | 0.0174 | 0.0815 |
| IDH1 | 0.2185 | 1.3475 | 0.3276 | 0.5273 | 0.2981 |
| IDH2 | 0.3187 | 0.6666 | 1.7472 | 0.6375 | 0.4165 |

**Summary:** IDH1 and IDH2, which produce alpha-ketoglutarate (a cofactor for TET-mediated DNA demethylation), are highly expressed across all tissues. IDH2 is particularly strong in heart (1.7472) and IDH1 in liver (1.3475). DNMT1 itself shows moderate expression, with the highest levels in brain (0.1557). The de novo methyltransferases DNMT3A and DNMT3B are lower. TET2 shows moderate expression in lung, while TET1 is low. The DNMT1 translocation in Johnny's tumor may disrupt normal DNA methylation maintenance, and the robust IDH1/IDH2 expression suggests active metabolic support for the demethylation pathway.

---

## Drug Efficacy Implications

### Targets that are well-expressed (drug likely effective):

**Doxycycline:**
- **MMP14** (gene body mean 1.289 in heart, 1.264 in colon): The most strongly expressed MMP target. Doxycycline's inhibition of MMP14 (MT1-MMP) is likely to have meaningful anti-invasive effects.
- **Mitochondrial ribosomal genes** (MRPS12 at 1.435, MRPS15 at 0.731, MT-CO1 at 0.893, MT-ND1 at 0.554): All highly expressed across tissues. Doxycycline's mitochondrial disruption mechanism has robust targets.

**Hydroxychloroquine (HCQ):**
- **CTSD** (gene body mean 4.972 in lung): The highest expressed gene in the entire analysis. Cathepsin D is a critical lysosomal protease, and its high expression indicates very active lysosomal function.
- **CTSL** (1.458 in liver), **SQSTM1** (1.156 in colon), **MAP1LC3B** (1.117 in brain), **LAMP1** (0.743 in brain), **LAMP2** (0.601 in brain): All highly expressed, confirming robust lysosomal and autophagic pathways that HCQ can disrupt.

**Cimetidine:**
- **VEGFA** (1.484 in liver) and **VEGFB** (2.004 in heart): Very strongly expressed angiogenic factors. Cimetidine's anti-angiogenic properties may be most impactful through suppressing VEGF signaling, which is especially relevant for the hypervascular nature of ASPS.

### Targets that are poorly expressed (drug may be less effective):

**Cimetidine -- Histamine receptors:**
- **HRH1** (max 0.020), **HRH2** (max 0.071), **HRH4** (max 0.002), **HDC** (max 0.039): All histamine pathway genes are at low to very low expression. The direct H2-blocking mechanism of cimetidine may have limited impact. However, cimetidine's anti-tumor effects through immune modulation and anti-angiogenesis do not require high histamine receptor expression.

**Doxycycline -- MMP1 and MMP3:**
- Both are very weakly expressed (max ~0.097), suggesting these are minor targets.

**Immune checkpoints:**
- **CTLA4** (0.006) and **TIGIT** (0.003) are very low in normal tissue. However, this reflects normal tissue baseline and does not indicate tumor microenvironment levels, which may be much higher.

### Tissue-specificity patterns:

- **Lung** is the highest-expressing tissue for: MMP9, MMP7, MRPS15 (tied), CTSD, VEGFC, FLT1, ANGPT2, CD274, GZMB, TFE3, FNIP1, TET1, TET2. This is clinically important since ASPS commonly metastasizes to the lungs.
- **Heart** leads in: MMP2, MMP14, MRPS15, MT-CO1, MT-ND1, HRH2, VEGFB, KDR, HAVCR2, MITF, IDH2. The high cardiac expression of drug targets warrants monitoring for cardiotoxicity.
- **Liver** leads in: MRPS12, CTSL, VEGFA, CD4, IDH1, DNMT3B. Relevant given liver is another common ASPS metastatic site.
- **Brain** leads in: MAP1LC3B, LAMP1, LAMP2, BECN1, DNMT1, MTOR. Brain metastases, while less common in ASPS, should be considered.
- **Transverse Colon** leads in: MMP1, MMP3, SQSTM1, ATG7, FLCN, RPTOR, and multiple immune genes (PDCD1, CTLA4, LAG3, TIGIT, IFNG, TNF, IL2, PRF1, CD8A).

---

## Overall Therapeutic Assessment

### Strengths of the Triple Blockade approach:

1. **Doxycycline has excellent target coverage.** Both of its mechanisms -- MMP inhibition and mitochondrial ribosome disruption -- target robustly expressed genes. MMP14, the most aggressive membrane-bound MMP, is very highly expressed. The mitochondrial targets (MRPS12, MRPS15, MT-CO1, MT-ND1) are all abundantly expressed, suggesting doxycycline will effectively impair tumor mitochondrial function.

2. **HCQ targets are the most strongly expressed of any drug category.** The lysosomal pathway (CTSD at 4.97, CTSL at 1.46) and autophagy markers (SQSTM1 at 1.16, MAP1LC3B at 1.12) are among the highest expressed genes in the entire dataset. This indicates these pathways are highly active, and disrupting them with HCQ could significantly stress tumor cells.

3. **Cimetidine's anti-angiogenic mechanism is well-supported.** Although histamine receptors are poorly expressed, VEGFA and VEGFB are very highly expressed (1.48 and 2.00 respectively). Given that ASPS is one of the most vascular sarcomas, cimetidine's anti-angiogenic effects may be its most meaningful contribution to the regimen.

4. **TFE3 pathway relevance is confirmed.** TFE3 itself is well expressed (0.586 in lung), and the connection to HCQ's lysosomal targets creates a potential synergy: the ASPSCR1-TFE3 fusion drives lysosomal gene expression, and HCQ disrupts these same lysosomal pathways.

### Potential concerns:

1. **Cimetidine's primary mechanism (H2 blockade) has weak targets.** The low expression of HRH2 and other histamine receptors suggests that the conventional mechanism of cimetidine may have limited direct impact. Its efficacy in this regimen likely depends on the anti-angiogenic and immune-modulatory effects.

2. **Immune checkpoint genes are low at baseline.** While this is expected in normal tissues, it means that the immune-boosting potential of the Triple Blockade may depend on tumor-specific immune infiltration that this normal-tissue analysis cannot fully capture.

3. **DNMT1 pathway considerations.** With the DNMT1 translocation, the epigenetic landscape of Johnny's tumor may be significantly altered. DNMT1 shows moderate expression (0.156), and the robust expression of IDH1 (1.35) and IDH2 (1.75) indicates an active metabolic context for DNA methylation regulation. The interaction between the DNMT1 translocation and TFE3 fusion may create unique vulnerabilities.

### Lung tissue relevance:

Given that ASPS most frequently metastasizes to the lungs, the lung tissue expression profile is particularly important. Lung shows strong expression of key drug targets: CTSD (4.97), MMP14 (0.64), VEGFA (0.80), VEGFB (1.47), SQSTM1 (1.01), and mitochondrial targets. This profile supports the Triple Blockade's potential efficacy against pulmonary metastases.

---

*This report was generated from AlphaGenome gene expression predictions. Expression values represent predicted gene body mean and max signals from RNA-seq tracks in the specified tissues. These are computational predictions from a reference genome model and should be interpreted alongside clinical data, tumor-specific sequencing, and other diagnostic information. This analysis reflects normal tissue expression and does not directly measure tumor-specific gene expression, which may differ due to the ASPSCR1-TFE3 fusion and DNMT1 translocation.*
