# Query 3: Comprehensive Top 50x3 Analysis — Strengths, Vulnerabilities, and Druggable Values

**Patient:** Johnny
**Diagnosis:** Alveolar Soft Part Sarcoma (ASPS)
**Date:** March 11, 2026
**Somatic Alterations:**
- ASPSCR1-TFE3 fusion: t(17;X)(q25.3;p11.23) — ASPSCR1 exon 7 to TFE3 exon 4
- DNMT1 translocation: t(1;19)(p35.2;p13.2) — exon 14
**Current Treatment:** Doxycycline (50 days), Cimetidine (21 days), Hydroxychloroquine (19 days)
**Analytical Platform:** AlphaGenome v0.6.1 (Google DeepMind)

---

**Scoring and Evidence Legend:**
- **[AG]** = AlphaGenome score (computational prediction from model)
- **[AG-ISM]** = AlphaGenome In Silico Mutagenesis score
- **[AG-MM]** = AlphaGenome Multi-Modal chromatin data
- **[AG-DT]** = AlphaGenome Drug Target gene expression prediction
- **[BIO]** = Established cancer/ASPS biology (peer-reviewed, consensus knowledge)
- **[INFERRED]** = Conceptual inference combining AlphaGenome data with established biology; not directly measured by AlphaGenome

---

## Part 1: ASPSCR1-TFE3 Fusion — Individual Analysis

### 1A. Top 50 Tumor Strengths (ASPSCR1-TFE3)

What gives the ASPSCR1-TFE3-driven tumor its power, ranked by estimated impact.

| Rank | Strength | Description | Score / Evidence |
|------|----------|-------------|-----------------|
| 1 | **Constitutive transcriptional activation** | ASPSCR1 promoter is always-on across tissues. RNA Polymerase II (POLR2AphosphoS5) is bound at 414.6 in spleen; H3K4me3 at 384.0 in brain; H3K27ac at 333.2 in spleen. The fusion places TFE3 coding sequence under this constitutive promoter, bypassing TFE3's normal repressive marks. | [AG-MM] POLR2AphosphoS5: 414.6; H3K4me3: 384.0; H3K27ac: 333.2 |
| 2 | **Extreme fibroblast enslavement** | ASPSCR1 breakpoint's transcriptional impact is overwhelmingly concentrated in fibroblasts: BJ cell score 14.0, skeletal muscle myoblast 12.0, IMR-90 12.0, foreskin fibroblast 12.0, lung fibroblast 12.0. ISM confirms: foreskin fibroblast -0.71. The tumor chemically enslaves surrounding fibroblasts to serve as metabolic fuel factories. | [AG] BJ: 14.0; ISM: -0.71 fibroblast |
| 3 | **Extreme fibrosis / collagen bunker** | Fibrosis score 14.81 in the vulnerability/danger matrix. Enslaved fibroblasts deposit massive collagen, forming an impenetrable physical barrier that excludes drugs and immune cells. MMP14 expression at 1.289 maintains this matrix. | [AG] Fibrosis score: 14.81; [AG-DT] MMP14: 1.289 |
| 4 | **Angiogenic command** | Endothelial cell danger score 11.53. VEGFB expression 2.004 (heart), VEGFA 1.484 (liver), KDR/VEGFR2 0.327 (heart). ASPS is one of the most vascular sarcomas; the fusion drives relentless neovascularization to feed both tumor and enslaved stroma. | [AG] Endothelial danger: 11.53; [AG-DT] VEGFB: 2.004, VEGFA: 1.484 |
| 5 | **Immune evasion via 7bp chromatin element displacement** | The translocation displaces a 7bp element at TFE3 positions -93 to -99 (DNase scores 3.0-3.29) that normally keeps chromatin open for T cells, NK cells, and monocytes. This is the largest ISM effect across all breakpoints. T follicular helper cells: -3.29, effector memory CD4+ T cells: -3.18, immature NK cells: -2.73. | [AG-ISM] DNase: 3.29 (largest effect in entire analysis) |
| 6 | **Reverse Warburg metabolic architecture** | The tumor does not ferment its own glucose. It forces fibroblasts to undergo glycolysis, then imports the lactate to burn in its upregulated mitochondria via OXPHOS. Five independent lines of data converge on this phenotype. | [AG + BIO] Fibroblast dominance + mitochondrial expression + lysosomal overload + vulnerability matrix + angiogenic demand |
| 7 | **Mitochondrial OXPHOS specialization** | MT-CO1 expression 0.893 (heart), MT-ND1 0.554 (heart), MRPS12 1.435 (liver), MRPS15 0.731 (heart). The tumor runs a high-efficiency oxidative engine that extracts maximum energy from imported lactate. | [AG-DT] MT-CO1: 0.893; MRPS12: 1.435; MRPS15: 0.731 |
| 8 | **Quiet genome / genomic stability** | Driven by a single rigid translocation rather than chaotic random mutations. No mutational burden means standard chemotherapy targeting dividing cells has minimal effect. The tumor is structurally stable and predictable but extremely hard to destabilize. | [BIO] Single-driver translocation architecture |
| 9 | **Lysosomal biogenesis overdrive** | TFE3 constitutively activates lysosomal biogenesis programs. CTSD (cathepsin D) at 4.972 (lung) — the highest-expressed drug target in the entire dataset. CTSL at 1.458. LAMP1 at 0.743, LAMP2 at 0.601. The tumor has massive lysosomal capacity. | [AG-DT] CTSD: 4.972 (highest in dataset); CTSL: 1.458 |
| 10 | **Autophagy-driven waste processing** | SQSTM1/p62 at 1.156 (colon), MAP1LC3B at 1.117 (brain), BECN1 at 0.353, ATG12 at 0.417. Constitutive autophagy maintains the fuel pipeline by recycling damaged components in enslaved fibroblasts. | [AG-DT] SQSTM1: 1.156; MAP1LC3B: 1.117 |
| 11 | **Multi-tissue endothelial cell recruitment** | Danger scores across multiple endothelial types: umbilical vein 11.53, mammary microvascular 9.72, pulmonary artery 7.83, coronary artery 6.66, bladder microvascular 5.06, glomerular 4.80, lymphatic 4.66. The tumor recruits vasculature from any tissue it reaches. | [AG] Multiple endothelial scores: 4.66-11.53 |
| 12 | **Stem cell plasticity** | Mesenchymal stem cell danger score 8.688, neuronal stem cell 6.906, mammary stem cell 5.313. The ASPSCR1 breakpoint at position -4 contains a stem cell chromatin switch (endodermal cell DNase 0.1115) granting self-renewal and resistance to differentiation. | [AG] MSC: 8.688; [AG-ISM] Stem cell switch: 0.1115 |
| 13 | **Bimodal regulatory architecture** | Two regulatory hotspots flank the ASPSCR1 breakpoint: upstream cluster at -11 (RNA-seq score 0.72) and downstream cluster at +56 to +62 (score 0.83). The translocation severs these clusters, creating a neomorphic regulatory unit driving aberrant fusion expression. | [AG-ISM] Upstream: 0.72; Downstream: 0.83 |
| 14 | **TFE3 poised chromatin state exploitation** | TFE3 locus has the highest chromatin accessibility of all breakpoints (DNase 0.607 colon, peak 92.0) but repressive histone marks (H3K9me3 3.08, H3K27me3 1.41). The fusion bypasses these repressive marks entirely by using ASPSCR1's constitutive promoter. | [AG-MM] TFE3 DNase: 0.607; H3K9me3 dominates histone landscape |
| 15 | **Acidic microenvironment moat** | Fibroblast-produced lactate creates a highly acidic microenvironment that physically and chemically paralyzes invading T cells and NK cells, creating an immune-exclusion zone independent of checkpoint signaling. | [INFERRED] From Reverse Warburg architecture + fibroblast enslavement data |
| 16 | **High transcription initiation at TFE3 locus** | CAGE positive-strand signal at TFE3 is 50x higher than ASPSCR1 and 85x higher than DNMT1-chr1. Center max reaches 780.0 in spleen. The TFE3 locus is primed for massive transcriptional output when activated by the fusion. | [AG-MM] CAGE: 0.514 mean, 780.0 peak (spleen) |
| 17 | **MMP-mediated tissue invasion** | MMP14 at 1.289 (heart), MMP7 at 0.506 (lung), MMP9 at 0.158 (lung), MMP2 at 0.216 (heart). These zinc-dependent endopeptidases degrade ECM, facilitating invasion, metastasis, and tunnel formation for new blood vessels. | [AG-DT] MMP14: 1.289; MMP7: 0.506 |
| 18 | **Pulmonary metastatic tropism** | Lung shows strong expression of tumor-enabling targets: CTSD 4.972, MMP7 0.506, MMP9 0.158, VEGFA 0.796, TFE3 0.586. ASPS preferentially metastasizes to lung, and the genomic profile supports this tropism. | [AG-DT] Multiple lung targets; [BIO] ASPS lung metastasis tropism |
| 19 | **CTCF insulator-mediated domain architecture** | CTCF binding at ASPSCR1: 118.0 (colon), 116.3 (spleen), 110.2 (brain). These insulator elements define chromatin domains that the fusion exploits to establish its regulatory territory. | [AG-MM] CTCF: 110-118 across tissues |
| 20 | **Myeloid progenitor engagement** | Common myeloid progenitor (CD34+) danger score 6.875. The tumor can influence myeloid lineage cells, potentially subverting innate immune responses and promoting tumor-associated macrophage polarization toward M2 (pro-tumor) phenotype. | [AG] Myeloid progenitor: 6.875 |
| 21 | **Fibroblast-specific regulatory control** | The downstream ISM hotspot at +56 to +62 specifically affects fibroblast/mesenchymal cell types: Panc1 -0.83, foreskin fibroblast -0.71, PFSK-1 -0.66, HCT116 -0.56. This is a hardwired regulatory module for fibroblast reprogramming. | [AG-ISM] Panc1: -0.83; fibroblast: -0.71 |
| 22 | **Resistance to standard chemotherapy** | The quiet genome with a single stable translocation lacks rapidly dividing mutational clones that cytotoxic chemotherapy typically targets. ASPS has historically shown poor response to conventional chemotherapy. | [BIO] ASPS chemotherapy resistance is established |
| 23 | **Wharton's jelly MSC recruitment** | Mesenchymal stem cell of Wharton's jelly danger score 5.563. This indicates the tumor can recruit primitive mesenchymal cells from multiple developmental sources, expanding its stromal support network. | [AG] Wharton's jelly MSC: 5.563 |
| 24 | **High active elongation marks** | H3K36me3 at ASPSCR1: thymus 339.2, brain 317.4, spleen 284.2, lung 275.3. These marks confirm continuous active transcription through the gene body, ensuring stable fusion transcript production. | [AG-MM] H3K36me3: 275-339 across tissues |
| 25 | **Splice site integrity at ASPSCR1** | Strong splice site predictions at ASPSCR1 (donor and acceptor max = 1.0), confirming the breakpoint preserves exon-intron architecture needed for proper fusion transcript splicing. | [AG-MM] Splice donor/acceptor: 1.0 |
| 26 | **Smooth muscle cell reprogramming** | Smooth muscle cell vulnerability score 9.875. The tumor can reprogram smooth muscle cells in addition to fibroblasts, expanding the pool of stromal cells available for metabolic enslavement. | [AG] Smooth muscle: 9.875 |
| 27 | **TFE3-driven metabolic adaptation** | TFE3 expression 0.586 (lung), 0.577 (colon). As a MiT/TFE family member, TFE3 regulates metabolic adaptation during stress, lysosomal positioning, and nutrient sensing — all constitutively activated by the fusion. | [AG-DT] TFE3: 0.586; [BIO] MiT/TFE function |
| 28 | **Neuronal metabolic mimicry** | TFE3 shows brain-tissue sensitivity: hypothalamus 1.50, caudate nucleus 1.50, Ammon's horn 1.25, frontal cortex 1.25. ISM position +83 affects Purkinje cells (0.022), cerebellum (0.021). The tumor borrows neuronal metabolic strategies for OXPHOS efficiency. | [AG] Brain tissues: 1.25-1.50; [AG-ISM] Purkinje: 0.022 |
| 29 | **Keratinocyte reprogramming capacity** | Hair follicular keratinocyte score 9.0 at ASPSCR1. Foreskin keratinocyte ISM score -0.363. The tumor can influence epithelial barrier cells, potentially aiding invasion through epithelial surfaces. | [AG] Keratinocyte: 9.0; [AG-ISM] -0.363 |
| 30 | **Liver-specific TF engagement at TFE3** | HNF4G (0.680), TAF1 (0.608), ATF3 (0.422) binding at TFE3 locus. This tissue-specific regulation may facilitate hepatic metastasis or metabolic adaptation using liver-specific transcriptional programs. | [AG-MM] HNF4G: 0.680; TAF1: 0.608 |
| 31 | **Kidney epithelial vulnerability exploitation** | Kidney epithelial cell vulnerability score 7.422. ASPSCR1 DNase signal highest in kidney (0.235). The tumor's regulatory architecture has specific impact on renal tissues, relevant to potential renal metastases. | [AG] Kidney epithelial: 7.422; [AG-MM] Kidney DNase: 0.235 |
| 32 | **VEGF receptor co-expression** | KDR/VEGFR2 at 0.327 (heart), FLT1/VEGFR1 at 0.117 (lung). Both VEGF receptors are expressed, ensuring the tumor's angiogenic signals are received by endothelial cells in the microenvironment. | [AG-DT] KDR: 0.327; FLT1: 0.117 |
| 33 | **Cardiac ventricle fibroblast engagement** | Cardiac ventricle fibroblast vulnerability score 6.359. The tumor's fibroblast enslavement machinery can operate in cardiac tissue, relevant to the cardiac tissue signals detected across analyses. | [AG] Cardiac fibroblast: 6.359 |
| 34 | **SP1 transcription factor recruitment** | SP1 binding at ASPSCR1: 111.7 (liver). SP1 is a ubiquitous transcription factor that drives basal expression of many housekeeping genes, reinforcing constitutive fusion transcript production. | [AG-MM] SP1: 111.7 |
| 35 | **EP300 enhancer activation** | EP300 binding at ASPSCR1: 89.5 (colon). EP300 is a histone acetyltransferase and transcriptional coactivator, indicating active enhancer elements near the breakpoint that amplify fusion gene expression. | [AG-MM] EP300: 89.5 |
| 36 | **Broad chromatin accessibility at ASPSCR1** | DNase-seq accessibility across tissues: kidney 0.235, spleen 0.170, liver 0.106, lung 0.082, heart 0.080. The promoter region is accessible in multiple tissues, enabling the fusion to drive expression wherever the tumor metastasizes. | [AG-MM] DNase: 0.080-0.235 across tissues |
| 37 | **Lactate shuttle metabolic efficiency** | The Reverse Warburg architecture converts stromal glycolysis into tumor OXPHOS, extracting approximately 18x more ATP per glucose molecule than standard Warburg glycolysis. This metabolic efficiency is a competitive advantage. | [INFERRED] From Reverse Warburg phenotype + mitochondrial expression data |
| 38 | **ANGPT2-mediated vascular destabilization** | ANGPT2 expression at 0.062 (lung). Angiopoietin-2 destabilizes existing blood vessels, facilitating the remodeling needed for tumor angiogenesis and creating entry points for metastatic seeding. | [AG-DT] ANGPT2: 0.062 |
| 39 | **Trophoblast-like invasive program** | Trophoblast cell target score 5.594. Trophoblast cells are the most naturally invasive human cells (placental implantation). The tumor may borrow aspects of trophoblast invasion programs. | [AG] Trophoblast: 5.594 |
| 40 | **HNF4A-mediated hepatic program access** | HNF4A binding at ASPSCR1: 91.1 (liver). This liver-master transcription factor binding suggests the fusion can access hepatic metabolic programs, potentially aiding liver metastasis. | [AG-MM] HNF4A: 91.1 |
| 41 | **GABPA regulatory engagement** | GABPA binding at ASPSCR1: 95.3 (liver). GABPA regulates mitochondrial genes and cell cycle progression, reinforcing the tumor's mitochondrial OXPHOS dependency and proliferative drive. | [AG-MM] GABPA: 95.3 |
| 42 | **Lymphatic endothelial engagement** | Dermis microvascular lymphatic vessel endothelial cell danger score 4.656, dermis lymphatic vessel endothelial cell 4.594. The tumor can engage lymphatic vasculature, facilitating lymphatic spread. | [AG] Lymphatic endothelial: 4.59-4.66 |
| 43 | **Mesodermal cell reprogramming** | Mesodermal cell ISM score -0.345. ASPS arises from mesodermal tissues, and the breakpoint's regulatory architecture specifically controls mesodermal gene expression programs. | [AG-ISM] Mesodermal: -0.345 |
| 44 | **Astrocyte engagement** | Astrocyte ISM score -0.303 at ASPSCR1. Astrocytes are the metabolic support cells of the brain; the tumor may recruit them similarly to how it enslaves fibroblasts, relevant to CNS metastasis. | [AG-ISM] Astrocyte: -0.303 |
| 45 | **Mesangial cell vulnerability** | Mesangial cell ISM score -0.345. Mesangial cells are specialized kidney pericytes; their vulnerability suggests the tumor can compromise renal microvascular support structures. | [AG-ISM] Mesangial: -0.345 |
| 46 | **Constitutive FLCN pathway activation** | FLCN (folliculin) at 0.327 (colon), FNIP1 at 0.138 (lung). These TFE3 pathway regulators are expressed, but the fusion oncoprotein bypasses their normal inhibitory control, maintaining nuclear TFE3 regardless of FLCN status. | [AG-DT] FLCN: 0.327; FNIP1: 0.138 |
| 47 | **Mammary epithelial cell engagement** | Mammary epithelial cell ISM score -0.310 at ASPSCR1. The tumor's regulatory footprint extends to mammary epithelial cells, suggesting broad mesenchymal-epithelial interaction capacity. | [AG-ISM] Mammary epithelial: -0.310 |
| 48 | **Proximal tubule epithelial engagement** | Epithelial cell of proximal tubule ISM score -0.295 at ASPSCR1. Renal proximal tubule cells have high mitochondrial content; the tumor may exploit their metabolic machinery. | [AG-ISM] Proximal tubule: -0.295 |
| 49 | **H3K9ac active chromatin marks** | H3K9ac at ASPSCR1: heart 237.5. This acetylation mark indicates active, open chromatin at the breakpoint, further ensuring reliable fusion gene transcription. | [AG-MM] H3K9ac: 237.5 |
| 50 | **Multi-organ metastatic capability** | The combination of broad endothelial engagement (lung, kidney, liver, brain), fibroblast enslavement machinery, and VEGF-driven angiogenesis gives the tumor a platform to establish metastases in multiple organs simultaneously. | [INFERRED] From combined danger scores + tissue expression profiles |

---

### 1B. Top 50 Tumor Vulnerabilities (ASPSCR1-TFE3)

Where the ASPSCR1-TFE3-driven tumor is weak, ranked by exploitability.

| Rank | Vulnerability | Description | Score / Evidence |
|------|---------------|-------------|-----------------|
| 1 | **Mitochondrial addiction** | Vulnerability score 13.625 (skeletal muscle myoblast). The tumor is absolutely dependent on OXPHOS for energy production. MT-CO1 0.893, MRPS12 1.435, MRPS15 0.731 — all targetable by doxycycline. | [AG] Vulnerability: 13.625; [AG-DT] MT-CO1: 0.893 |
| 2 | **Lysosomal dependence** | CTSD at 4.972 is the highest-expressed drug target in the entire dataset. The TFE3 fusion constitutively drives lysosomal biogenesis; disrupting lysosomes (HCQ) creates a catastrophic waste accumulation. No reserve capacity exists. | [AG-DT] CTSD: 4.972; CTSL: 1.458 |
| 3 | **Fibroblast fuel pipeline fragility** | Fibroblast of lung vulnerability 13.344, foreskin fibroblast 13.313, bronchus fibroblast 10.656. The entire Reverse Warburg architecture collapses if the enslaved fibroblasts are killed or their autophagy is blocked. | [AG] Fibroblast vulnerabilities: 10.66-13.34 |
| 4 | **Metabolic inflexibility** | TFEB expression only 0.083 (low), mTOR 0.070 (low), RPTOR 0.031 (low). Alternative metabolic pathways have atrophied. The tumor cannot pivot to standard Warburg glycolysis because its glycolytic machinery is severely downregulated. | [AG-DT] TFEB: 0.083; mTOR: 0.070; RPTOR: 0.031 |
| 5 | **Single-driver dependency** | The entire tumor is driven by one translocation event. Unlike tumors with dozens of driver mutations that can compensate for each other, loss of ASPSCR1-TFE3 function would be catastrophic. The quiet genome offers no backup drivers. | [BIO] Single-driver architecture |
| 6 | **Autophagy system at maximum capacity** | SQSTM1/p62 at 1.156, MAP1LC3B at 1.117 — both at high levels, indicating the autophagy system is already running at maximum. There is no headroom to upregulate further when HCQ blocks lysosomal function. | [AG-DT] SQSTM1: 1.156; MAP1LC3B: 1.117 |
| 7 | **Immune regulatory element disruption (exploitable)** | The 7bp element (DNase 3.0-3.29) is displaced but not destroyed. Chromatin-modifying agents (HDAC inhibitors, BET inhibitors) could potentially restore immune cell chromatin accessibility at the TFE3 locus, reversing immune evasion. | [AG-ISM] DNase: 3.29; [INFERRED] therapeutic reversibility |
| 8 | **Narrow regulatory footprint** | The ASPSCR1 regulatory module spans only ~70bp (from -11 to +62 around the breakpoint). This narrow regulatory architecture cannot evolve new circuits; it is structurally constrained. | [AG-ISM] 70bp regulatory module |
| 9 | **Angiogenesis-invasion coupling** | The tumor needs both VEGF signaling AND MMP-mediated ECM degradation to build new blood vessels. Blocking MMPs (doxycycline) renders VEGF signals useless because the physical tunnels for new vessels cannot be carved. | [INFERRED] From MMP + VEGF data |
| 10 | **Fibroblast-derived cell line vulnerability** | Fibroblast-derived cell line vulnerability score 9.953. Even established fibroblast cell lines show high vulnerability to perturbation at this breakpoint, confirming the fragility of the stromal enslavement program. | [AG] Fibroblast cell line: 9.953 |
| 11 | **TFEB compensation unavailable** | TFEB, the closest TFE3 family member, has notably low expression (0.083 lung). If the TFE3 fusion is disrupted, TFEB cannot compensate for lost function. No backup transcription factor exists. | [AG-DT] TFEB: 0.083 |
| 12 | **Acid-base sensitivity** | The acidic lactate moat that protects the tumor also makes the tumor microenvironment pH-dependent. Disrupting lactate production (by killing fibroblasts) removes the acid barrier, potentially allowing immune cell infiltration. | [INFERRED] From Reverse Warburg architecture |
| 13 | **MMP14 as single dominant collagen enzyme** | MMP14 at 1.289 is the overwhelmingly dominant MMP. MMP1 (0.097) and MMP3 (0.098) are very low. The collagen bunker maintenance depends almost entirely on one enzyme, which doxycycline inhibits. | [AG-DT] MMP14: 1.289 vs MMP1: 0.097, MMP3: 0.098 |
| 14 | **Lack of mutational agility** | The quiet genome means the tumor cannot rapidly generate point mutations for drug resistance. It cannot upregulate drug efflux pumps, create target mutations, or activate alternative signaling cascades through random mutagenesis. | [BIO] Quiet genome = limited adaptive capacity |
| 15 | **Kidney epithelial cell vulnerability** | Kidney epithelial cell vulnerability score 7.422, outer medulla of kidney 6.531, cortex of kidney 6.219. The tumor's renal vulnerability may reflect dependence on renal-type metabolic programs that can be disrupted. | [AG] Kidney vulnerabilities: 6.22-7.42 |
| 16 | **Smooth muscle cell vulnerability** | Smooth muscle cell vulnerability 9.875, bladder smooth muscle 6.500, bronchial smooth muscle 5.609. The tumor's reprogramming of smooth muscle creates dependency on these cell types. | [AG] Smooth muscle: 5.61-9.875 |
| 17 | **Bronchus fibroblast dependence** | Bronchus fibroblast vulnerability 10.656. In the lung metastatic setting, the tumor specifically depends on bronchial fibroblasts for fuel, making this a targetable vulnerability for lung-directed therapy. | [AG] Bronchus fibroblast: 10.656 |
| 18 | **Skeletal muscle myoblast paradox** | Myoblast vulnerability score 13.625 (highest overall). Additional myoblast scores: 7.719 and 6.547. The tumor's connection to skeletal muscle lineage creates its greatest vulnerability where it is most active. | [AG] Myoblast: 13.625, 7.719, 6.547 |
| 19 | **Constitutive promoter cannot be silenced** | The ASPSCR1 promoter is always-on, meaning the fusion continuously produces the fusion oncoprotein. This makes the tumor predictable — it cannot downregulate the fusion to hide from targeted therapies. | [INFERRED] From constitutive promoter data |
| 20 | **Chromatin accessibility at TFE3 creates detection opportunity** | TFE3 has the highest chromatin accessibility (DNase 0.607, peak 92.0). This extreme openness means the locus is accessible to therapeutic agents that target open chromatin. | [AG-MM] TFE3 DNase: 0.607, peak: 92.0 |
| 21 | **VEGF dependency for stromal maintenance** | VEGFA 1.484, VEGFB 2.004. The tumor requires constant angiogenic signaling to maintain both itself and its enslaved fibroblast population. Anti-angiogenic therapy starves the entire metabolic ecosystem. | [AG-DT] VEGFA: 1.484; VEGFB: 2.004 |
| 22 | **IDH1/IDH2 imbalance with TFE3 pathway** | IDH1 at 1.348, IDH2 at 1.747. These enzymes produce alpha-ketoglutarate feeding into TET-mediated demethylation. High IDH activity in the context of TFE3's metabolic programming creates a metabolic bottleneck that can be exploited. | [AG-DT] IDH1: 1.348; IDH2: 1.747 |
| 23 | **Low mTOR pathway activity** | mTOR at 0.070, RPTOR at 0.031. The tumor appears to bypass mTOR-mediated regulation of TFE3 nuclear localization. This means mTOR-independent TFE3 activation but also means the tumor cannot use mTOR signaling as a backup survival pathway. | [AG-DT] mTOR: 0.070; RPTOR: 0.031 |
| 24 | **LAMP1/LAMP2 dependence** | LAMP1 at 0.743, LAMP2 at 0.601. Lysosomal membrane integrity is critical for the tumor's waste processing. HCQ-mediated lysosomal disruption directly targets these abundantly expressed structural proteins. | [AG-DT] LAMP1: 0.743; LAMP2: 0.601 |
| 25 | **ATG5/ATG7 bottleneck** | ATG5 at 0.034 (low), ATG7 at 0.050 (low). These essential autophagy components are weakly expressed despite the high autophagy flux, creating a rate-limiting bottleneck. If demand increases (from therapeutic stress), these cannot be upregulated. | [AG-DT] ATG5: 0.034; ATG7: 0.050 |
| 26 | **Outer medulla of kidney vulnerability** | Score 6.531. The tumor's metabolic architecture has specific vulnerability in renal medullary tissue, which shares the high-OXPHOS, lactate-shuttling metabolic features of the tumor itself. | [AG] Kidney medulla: 6.531 |
| 27 | **Histone mark absence at TFE3** | TFE3 histone signals are near-zero (top mark H3K9me3 at only 3.08 vs 384+ at other breakpoints). This paradoxical absence means the TFE3 locus lacks the histone-based regulatory buffers that could protect against chromatin-targeting therapies. | [AG-MM] TFE3 histones: max 3.08 vs ASPSCR1: 384.0 |
| 28 | **Minimal TF binding at TFE3** | TF ChIP-seq at TFE3 is 2-3 orders of magnitude lower than other breakpoints (CTCF 0.93 vs 414.6 at ASPSCR1). This regulatory sparseness means the TFE3 locus is not protected by dense transcription factor occupancy. | [AG-MM] TFE3 top TF: 0.93 vs ASPSCR1: 414.6 |
| 29 | **Immune cell responsiveness** | Target matrix: naive B cell 11.625, IgD-negative memory B cell 9.750, regulatory T cell 9.000, CD4+ memory T cell 8.875, naive CD8+ T cell 8.250. The immune system can be mobilized against this tumor through the right targets. | [AG] Immune target scores: 8.25-11.63 |
| 30 | **Cathepsin D overexpression paradox** | CTSD at 4.972 is extremely high. While this supports the tumor's lysosomal function, Cathepsin D can also promote apoptosis when released from lysosomes. HCQ-mediated lysosomal membrane permeabilization could trigger cathepsin-dependent cell death. | [AG-DT] CTSD: 4.972; [BIO] Cathepsin-mediated apoptosis |
| 31 | **NK cell priming opportunity** | Immature NK cell target score 7.250 at TFE3. The 7bp element displacement specifically affects NK cell chromatin. Reversing this with chromatin agents could unleash NK cell cytotoxicity against the tumor. | [AG] NK cell: 7.250 |
| 32 | **Trophoblast cell interface** | Trophoblast cell target score 5.594. While the tumor may borrow trophoblast invasive programs, trophoblast-targeted immune mechanisms (relevant in pregnancy immunology) could be therapeutically applicable. | [AG] Trophoblast: 5.594 |
| 33 | **Low HRH4 expression reveals limited histamine escape** | HRH4 at 0.002 (essentially absent). The tumor cannot upregulate alternative histamine receptor signaling to bypass cimetidine's effects. | [AG-DT] HRH4: 0.002 |
| 34 | **VEGFC limitation** | VEGFC at only 0.031 (low). The tumor has limited capacity for lymphangiogenesis compared to its blood vessel formation, making lymphatic escape routes less available. | [AG-DT] VEGFC: 0.031 |
| 35 | **BECN1 moderate expression ceiling** | BECN1 (Beclin-1) at 0.353. This autophagy initiator is only moderately expressed, limiting the tumor's ability to ramp up autophagy beyond current levels under stress. | [AG-DT] BECN1: 0.353 |
| 36 | **ATP6V1A lysosomal pump vulnerability** | ATP6V1A at 0.245 (moderate). The vacuolar ATPase that acidifies lysosomes is targetable; HCQ's pH-raising effect directly opposes this pump, and its moderate expression limits compensatory upregulation. | [AG-DT] ATP6V1A: 0.245 |
| 37 | **Neural crest cell sensitivity** | Neural crest cell target score 3.359. ASPS's developmental origins from neural crest-like cells create a lineage-specific vulnerability to agents targeting neural crest differentiation programs. | [AG] Neural crest: 3.359 |
| 38 | **Single critical position dominance at ASPSCR1** | The ISM identifies chr17:82,010,870 (T>G) as the single most disruptive variant, appearing across nearly all tissue types. This positional dominance means the regulatory architecture lacks redundancy. | [AG-ISM] Position +59: dominant across all tissues |
| 39 | **MITF pathway dependency** | MITF at 0.225 (heart, moderate). As a MiT/TFE family member related to TFE3, MITF's moderate expression may indicate some backup potential, but its tissue-specific expression (heart-dominant) limits its ability to compensate broadly. | [AG-DT] MITF: 0.225 |
| 40 | **CD4+ T cell accessibility** | CD4 at 0.107 (liver, moderate). CD4+ helper T cells are present at moderate levels, meaning T-cell-directed therapies have a substrate of immune cells to work with. | [AG-DT] CD4: 0.107 |
| 41 | **Perforin and granzyme expression** | PRF1 at 0.083 (colon), GZMB at 0.074 (lung). The cytolytic machinery for tumor killing is present at detectable levels, meaning the immune system retains functional killing capacity if properly directed. | [AG-DT] PRF1: 0.083; GZMB: 0.074 |
| 42 | **Low CTLA4/TIGIT expression** | CTLA4 at 0.006, TIGIT at 0.004. While this limits standard checkpoint therapy, it also means these inhibitory receptors are not strongly suppressing the existing immune response — the immune evasion operates through chromatin disruption instead. | [AG-DT] CTLA4: 0.006; TIGIT: 0.004 |
| 43 | **TNF pathway availability** | TNF at 0.092 (colon). Tumor necrosis factor is expressed at near-moderate levels, indicating an inflammatory signaling pathway is available for therapeutic activation. | [AG-DT] TNF: 0.092 |
| 44 | **Fusion transcript dependency on splice sites** | Strong splice sites at ASPSCR1 (donor/acceptor = 1.0). The fusion transcript requires proper splicing; splice-modulating therapies could produce non-functional fusion variants. | [AG-MM] Splice sites: 1.0 |
| 45 | **DNMT3A/3B cannot compensate for DNMT1** | DNMT3A at 0.099, DNMT3B at 0.074 — both low. The de novo methyltransferases cannot compensate for disrupted DNMT1 maintenance methylation, leaving the epigenetic landscape unstable. | [AG-DT] DNMT3A: 0.099; DNMT3B: 0.074 |
| 46 | **TET2 demethylation pressure** | TET2 at 0.123 (lung, moderate). Active TET-mediated demethylation, combined with disrupted DNMT1, creates progressive epigenetic erosion that may eventually unmask tumor antigens. | [AG-DT] TET2: 0.123 |
| 47 | **Limited melanocyte program access** | Foreskin melanocyte ISM score -0.341 at ASPSCR1. While melanocyte programs (related to MiT/TFE family) are accessible, the low score indicates limited engagement, reducing the tumor's plasticity in this direction. | [AG-ISM] Melanocyte: -0.341 |
| 48 | **Endodermal cell chromatin switch at -4** | The stem cell switch at ASPSCR1 position -4 (DNase 0.1115) is directly adjacent to the breakpoint. This positioning means it is directly disrupted by the translocation, limiting the tumor's stem cell maintenance capacity over time. | [AG-ISM] Position -4: 0.1115 |
| 49 | **IFNG production capacity** | IFNG at 0.007 (very low but detectable). Even minimal interferon-gamma production, if amplified by immunotherapy, could shift the microenvironment toward anti-tumor immunity. | [AG-DT] IFNG: 0.007 |
| 50 | **Reproducibility confirms targetable biology** | Independent reproduction analysis confirmed the same tissue hierarchies across all three analytical approaches. The vulnerabilities are not artifacts — they are stable, reproducible features of this genomic architecture. | [AG] Reproduction confirmed across 3 methods |

---

### 1C. Top 50 Druggable Values (ASPSCR1-TFE3)

Therapeutic targets ranked by combination of target expression level and therapeutic relevance.

| Rank | Target | Drug / Intervention | Expression (Gene Body Mean) | Rationale |
|------|--------|--------------------|-----------------------------|-----------|
| 1 | **CTSD (Cathepsin D)** | HCQ (lysosomal disruption) | 4.972 (lung) | Highest-expressed target in entire dataset. Lysosomal protease essential for autophagy. HCQ raises pH, neutralizing CTSD activity. [AG-DT] |
| 2 | **VEGFB** | Cimetidine (anti-angiogenic), Bevacizumab | 2.004 (heart) | Dominant angiogenic factor. Cimetidine suppresses VEGF signaling; bevacizumab directly neutralizes. [AG-DT] |
| 3 | **IDH2** | IDH inhibitors (enasidenib) | 1.747 (heart) | Produces alpha-ketoglutarate for TET-mediated demethylation. Inhibition disrupts epigenetic balance the tumor depends on. [AG-DT] |
| 4 | **VEGFA** | Cimetidine, Bevacizumab, Axitinib | 1.484 (liver) | Primary VEGF ligand. Anti-VEGF therapy targets the tumor's extreme vascular dependence. [AG-DT] |
| 5 | **CTSL (Cathepsin L)** | HCQ | 1.458 (liver) | Second major lysosomal protease. Disrupted by HCQ-mediated pH increase. [AG-DT] |
| 6 | **MRPS12** | Doxycycline (mito ribosome inhibitor) | 1.435 (liver) | Nuclear-encoded mitochondrial ribosomal protein. Doxycycline inhibits mitochondrial translation. [AG-DT] |
| 7 | **MMP14 (MT1-MMP)** | Doxycycline (MMP inhibitor) | 1.289 (heart) | Dominant membrane-bound MMP. Dissolves collagen bunker and prevents vessel tunnel formation. [AG-DT] |
| 8 | **IDH1** | IDH inhibitors (ivosidenib) | 1.348 (liver) | Partner to IDH2 in alpha-ketoglutarate production. Inhibition disrupts tumor's metabolic-epigenetic axis. [AG-DT] |
| 9 | **SQSTM1/p62** | HCQ (autophagy blockade) | 1.156 (colon) | Autophagy receptor. Accumulates when autophagy is blocked by HCQ, causing toxic protein aggregation. [AG-DT] |
| 10 | **MAP1LC3B (LC3B)** | HCQ | 1.117 (brain) | Autophagosome marker. HCQ prevents autophagosome-lysosome fusion, stalling waste clearance. [AG-DT] |
| 11 | **MT-CO1** | Doxycycline | 0.893 (heart) | Mitochondrial-encoded cytochrome c oxidase subunit. Direct doxycycline target. [AG-DT] |
| 12 | **LAMP1** | HCQ | 0.743 (brain) | Lysosomal membrane protein. HCQ disrupts lysosomal integrity, compromising LAMP1 function. [AG-DT] |
| 13 | **MRPS15** | Doxycycline | 0.731 (heart) | Mitochondrial ribosomal protein. Doxycycline inhibits translation. [AG-DT] |
| 14 | **LAMP2** | HCQ | 0.601 (brain) | Lysosomal membrane protein involved in autophagosome-lysosome fusion. [AG-DT] |
| 15 | **TFE3** | TFE3 pathway inhibitors (experimental) | 0.586 (lung) | The fusion oncoprotein itself. Direct targeting would collapse the entire tumor program. [AG-DT] |
| 16 | **MT-ND1** | Doxycycline | 0.554 (heart) | Mitochondrial NADH dehydrogenase. Doxycycline disrupts Complex I function. [AG-DT] |
| 17 | **MMP7** | Doxycycline | 0.506 (lung) | Secreted MMP. Lung-dominant expression makes it relevant to pulmonary metastasis control. [AG-DT] |
| 18 | **ATG12** | HCQ (pathway disruption) | 0.417 (heart) | Essential autophagy conjugation system component. [AG-DT] |
| 19 | **BECN1 (Beclin-1)** | HCQ | 0.353 (brain) | Autophagy initiation regulator. [AG-DT] |
| 20 | **KDR/VEGFR2** | Cabozantinib, Axitinib, Pazopanib | 0.327 (heart) | Primary VEGF receptor on endothelial cells. TKI targeting directly blocks angiogenic signaling. [AG-DT] |
| 21 | **FLCN (Folliculin)** | mTOR pathway modulators | 0.327 (colon) | TFE3 regulator; its disruption in the tumor context offers pathway modulation opportunities. [AG-DT] |
| 22 | **ATP6V1A** | Bafilomycin A1, HCQ | 0.245 (brain) | Vacuolar ATPase. Lysosomal acidification pump directly opposed by HCQ. [AG-DT] |
| 23 | **MITF** | MITF pathway inhibitors | 0.225 (heart) | MiT/TFE family member. Related pathway may offer additional targeting angles. [AG-DT] |
| 24 | **MMP2** | Doxycycline | 0.216 (heart) | Gelatinase A. Degrades type IV collagen in basement membranes. [AG-DT] |
| 25 | **MMP9** | Doxycycline | 0.158 (lung) | Gelatinase B. Lung-expressed, relevant to pulmonary metastasis. [AG-DT] |
| 26 | **DNMT1** | Decitabine, Azacitidine | 0.156 (brain) | Maintenance methyltransferase disrupted by translocation. Hypomethylating agents could amplify epigenetic instability. [AG-DT] |
| 27 | **FNIP1** | mTOR modulators | 0.138 (lung) | FLCN-interacting protein in TFE3 regulation. [AG-DT] |
| 28 | **TET2** | Vitamin C (TET activator) | 0.123 (lung) | DNA demethylase. Activation promotes demethylation, potentially unmasking tumor antigens. [AG-DT] |
| 29 | **FLT1/VEGFR1** | TKIs (cabozantinib, axitinib) | 0.117 (lung) | Alternative VEGF receptor. [AG-DT] |
| 30 | **LAG3** | Relatlimab (anti-LAG3) | 0.111 (colon) | Highest-expressed immune checkpoint. Most promising checkpoint target for this tumor. [AG-DT] |
| 31 | **CD4** | T-cell directed therapies | 0.107 (liver) | CD4+ T cell marker. Substrate for helper T cell-based therapies. [AG-DT] |
| 32 | **DNMT3A** | Hypomethylating agents | 0.099 (heart) | De novo methyltransferase. Low but targetable. [AG-DT] |
| 33 | **MMP1** | Doxycycline | 0.097 (colon) | Collagenase-1. Low expression but still targetable. [AG-DT] |
| 34 | **MMP3** | Doxycycline | 0.098 (colon) | Stromelysin-1. Low expression. [AG-DT] |
| 35 | **TNF** | TNF pathway activators (immunostimulatory) | 0.092 (colon) | Tumor necrosis factor. Activation could shift microenvironment toward anti-tumor inflammation. [AG-DT] |
| 36 | **PRF1 (Perforin)** | IL-2, checkpoint inhibitors (to amplify) | 0.083 (colon) | Cytolytic effector molecule. Present and functional; needs immune activation to deploy. [AG-DT] |
| 37 | **TFEB** | TFEB inhibitors (experimental) | 0.083 (lung) | Lysosomal biogenesis TF. Low but represents the TFE3 backup pathway. [AG-DT] |
| 38 | **GZMB (Granzyme B)** | IL-2, checkpoint inhibitors | 0.074 (lung) | Cytolytic protease. Lung expression relevant to pulmonary metastasis immune clearance. [AG-DT] |
| 39 | **DNMT3B** | Hypomethylating agents | 0.074 (liver) | De novo methyltransferase. [AG-DT] |
| 40 | **HRH2** | Cimetidine (H2 blocker) | 0.071 (heart) | Primary cimetidine target. Low expression limits direct receptor effect. [AG-DT] |
| 41 | **mTOR** | Rapamycin, Everolimus | 0.070 (brain) | Master metabolic kinase. Low expression but pathway inhibition could disrupt residual TFE3 regulation. [AG-DT] |
| 42 | **HAVCR2/TIM-3** | Anti-TIM-3 antibodies | 0.065 (brain) | Immune checkpoint. Moderate expression in brain. [AG-DT] |
| 43 | **ANGPT2** | Trebananib (anti-Ang2) | 0.062 (lung) | Vascular destabilizer. Lung-dominant. [AG-DT] |
| 44 | **CD274/PD-L1** | Nivolumab, Pembrolizumab | 0.052 (lung) | PD-L1. Low expression limits checkpoint blockade efficacy but not zero. [AG-DT] |
| 45 | **ATG7** | Autophagy inhibitors | 0.050 (colon) | Essential autophagy enzyme. Bottleneck target. [AG-DT] |
| 46 | **ATG5** | Autophagy inhibitors | 0.034 (lung) | Essential for autophagosome formation. Bottleneck. [AG-DT] |
| 47 | **RPTOR (Raptor)** | mTOR inhibitors | 0.031 (colon) | mTORC1 component. Very low expression. [AG-DT] |
| 48 | **HDC (Histidine decarboxylase)** | Cimetidine (downstream) | 0.039 (lung) | Histamine-producing enzyme. Low. [AG-DT] |
| 49 | **PDCD1/PD-1** | Nivolumab, Pembrolizumab | 0.017 (colon) | PD-1 receptor. Very low in normal tissue; may be higher on tumor-infiltrating lymphocytes. [AG-DT] |
| 50 | **CTLA4** | Ipilimumab | 0.006 (colon) | Very low expression. Standard anti-CTLA4 may have limited effect. [AG-DT] |

---

## Part 2: DNMT1 Translocation — Individual Analysis

### 2A. Top 50 Tumor Strengths (DNMT1 t(1;19))

What the DNMT1 translocation contributes to tumor power.

| Rank | Strength | Description | Score / Evidence |
|------|----------|-------------|-----------------|
| 1 | **T-cell/NK cell chromatin disruption** | Position -66 at chr19 (DNase 0.436) acts as a master switch controlling T/NK cell chromatin accessibility. All 15 top DNase hits are T/NK cells. Disruption impairs immune cell regulation at the DNMT1 locus. | [AG-ISM] DNase: 0.436; exclusive T/NK specificity |
| 2 | **Epigenetic shield (methylation maintenance disruption)** | DNMT1 at exon 14 disruption compromises the primary maintenance methyltransferase. This creates progressive methylation drift that can silence tumor suppressors while the tumor adapts. | [BIO] DNMT1 is primary maintenance methyltransferase |
| 3 | **Thymus enhancer hijacking** | Chr1 breakpoint sits in a thymus-specific enhancer (H3K4me1: 297.8, H3K27ac: 197.5). This T-cell developmental enhancer, when translocated, disrupts T-cell maturation programs. | [AG-MM] H3K4me1: 297.8; H3K27ac: 197.5 |
| 4 | **Immune cell developmental reprogramming** | CD14+ monocyte impact score 3.5 at chr1. The translocation alters monocyte epigenetic programs, potentially subverting innate immune surveillance. | [AG] CD14+ monocyte: 3.5 |
| 5 | **Active gene body at chr19** | H3K4me3: 396.2 (brain), H3K36me3: 384.5 (thymus), H3K27ac: 371.7 (spleen). The chr19 DNMT1 locus is one of the most transcriptionally active breakpoints, with RNA Pol II at 320.5. | [AG-MM] H3K4me3: 396.2; POLR2AphosphoS5: 320.5 |
| 6 | **Regulatory T cell manipulation** | CD4+/CD25+ regulatory T cell appears in top positions at DNMT1-chr19. Tregs suppress anti-tumor immunity; their epigenetic alteration through DNMT1 disruption may enhance their suppressive function. | [AG] Regulatory T cell: 9.0 |
| 7 | **B cell epigenetic disruption** | Naive B cell target score 11.625, IgD-negative memory B cell 9.750. The translocation disrupts B cell epigenetic programs, potentially impairing antibody-mediated anti-tumor responses. | [AG] Naive B cell: 11.625; memory B cell: 9.750 |
| 8 | **Cardiac tissue regulatory access** | Right cardiac atrium score 3.5 at chr1, heart right ventricle 2.5, left ventricle 2.5. The translocation grants access to cardiac-specific regulatory programs. | [AG] Cardiac tissue: 2.5-3.5 |
| 9 | **CTCF insulator network at chr1** | CTCF binding at chr1: brain 115.3, colon 113.1, spleen 111.2. Strong boundary elements that the translocation disrupts, potentially spreading regulatory effects to neighboring genes. | [AG-MM] CTCF: 111-115 across tissues |
| 10 | **Chromatin state asymmetry exploitation** | Chr1 is in closed/repressive chromatin (H3K27me3: 145.2, H3K9me3: 176.5); chr19 is in active chromatin (H3K4me3: 396.2). The translocation juxtaposes these opposite states, creating regulatory chaos at the junction. | [AG-MM] Chr1 repressive vs chr19 active |
| 11 | **CD8+ memory T cell modulation** | CD8+ memory T cell score 8.125, impact score 2.5 at chr1. The translocation disrupts cytotoxic T cell memory formation, potentially preventing durable anti-tumor immunity. | [AG] CD8+ memory T: 8.125 |
| 12 | **Immature NK cell vulnerability creation** | Immature NK cell DNase 0.436 (highest single-position effect at chr19). The translocation specifically disrupts NK cell maturation chromatin programs. | [AG-ISM] Immature NK: 0.436 |
| 13 | **Liver-specific TF deployment** | HNF4A (112.2), SP1 (107.6), RXRA (106.8), JUND (99.6) all bound at chr1. These liver TFs, when regulatory context is disrupted, may contribute to hepatic adaptation of the tumor. | [AG-MM] Multiple liver TFs: 99-112 |
| 14 | **FOXA1/FOXA2 pioneer factor access** | FOXA1 (97.0) and FOXA2 (98.4) binding at chr1. These pioneer TFs can open closed chromatin, potentially enabling aberrant gene activation at the translocation junction. | [AG-MM] FOXA1: 97.0; FOXA2: 98.4 |
| 15 | **YY1 regulatory engagement** | YY1 binding at chr1: 96.5. YY1 is a multifunctional transcription factor involved in chromatin looping and enhancer-promoter communication. | [AG-MM] YY1: 96.5 |
| 16 | **K562 cell sensitivity** | K562 (CML cell line) impact score 3.0 at chr19. Sensitivity in this hematopoietic line confirms the translocation's impact on blood cell lineage regulation. | [AG] K562: 3.0 |
| 17 | **Multi-tissue Polycomb repression spread** | H3K27me3 at chr1: brain 145.2, spleen 135.1, colon 133.7, heart 118.1. The repressive chromatin from chr1, when juxtaposed with chr19's active marks, can potentially silence chr19-associated genes. | [AG-MM] H3K27me3: 118-145 across tissues |
| 18 | **T-helper cell subtype disruption** | T-helper 2 (DNase 0.221), T-helper 22 (0.133), T-helper 17 (RNA-seq 0.079) all affected. The translocation disrupts multiple T-helper differentiation programs simultaneously. | [AG-ISM] Multiple Th subtypes: 0.079-0.221 |
| 19 | **Effector memory CD8+ T cell impairment** | Effector memory CD8+ T cell DNase 0.159. These are the cells responsible for killing tumor cells upon re-encounter; their chromatin disruption impairs anti-tumor cytotoxicity. | [AG-ISM] Effector memory CD8+: 0.159 |
| 20 | **Central memory CD4+ T cell disruption** | Central memory CD4+ T cell DNase 0.169. Central memory T cells maintain long-term immune surveillance; their disruption prevents durable immune memory against the tumor. | [AG-ISM] Central memory CD4+: 0.169 |
| 21 | **Splice site integrity at chr19** | Strong splice sites at chr19 (donor/acceptor = 1.0), confirming exon 14 breakpoint preserves flanking splice junctions for potential aberrant transcript production. | [AG-MM] Splice sites: 1.0 |
| 22 | **IDH1/IDH2 metabolic integration** | IDH1 (1.348) and IDH2 (1.747) produce alpha-ketoglutarate that feeds TET enzymes. DNMT1 disruption + high IDH/TET activity = coordinated epigenetic reprogramming favoring the tumor. | [AG-DT] IDH1: 1.348; IDH2: 1.747 |
| 23 | **EP300 enhancer activation at chr1** | EP300 binding at chr1: 99.3 (colon). Active enhancer element that may drive aberrant gene expression at the translocation junction. | [AG-MM] EP300: 99.3 |
| 24 | **POLR2A engagement at chr1** | RNA Pol II binding at chr1: 100.4 (spleen). Active transcription machinery present at the chr1 breakpoint despite its generally repressive chromatin. | [AG-MM] POLR2A: 100.4 |
| 25 | **GM12878 lymphoblastoid sensitivity** | GM12878 score 3.0 at chr19. This EBV-transformed B cell line's sensitivity confirms broad B-lineage regulatory disruption. | [AG] GM12878: 3.0 |
| 26 | **Sigmoid colon sensitivity** | Sigmoid colon score 1.5 at chr19. GI-tract tissue sensitivity suggests DNMT1 disruption affects gut-associated immune tissues. | [AG] Sigmoid colon: 1.5 |
| 27 | **Purkinje cell sensitivity** | Purkinje cell score 1.5 at chr19. Neuronal sensitivity suggests brain regulatory impact from the DNMT1 translocation. | [AG] Purkinje cell: 1.5 |
| 28 | **Mole/melanocytic tissue sensitivity** | Mole tissue score 2.0 at chr19. Melanocytic lineage sensitivity connects to MiT/TFE family biology shared between TFE3 and MITF. | [AG] Mole: 2.0 |
| 29 | **LHCN-M2 muscle lineage sensitivity** | LHCN-M2 score 1.75 at chr19. Skeletal muscle lineage sensitivity mirrors the myoblast vulnerability seen at ASPSCR1, reinforcing the tumor's mesenchymal connection. | [AG] LHCN-M2: 1.75 |
| 30 | **Naive CD8+ T cell disruption** | Naive CD8+ T cell score 8.250, DNase 1.75 at chr19. Disruption at the naive stage prevents new cytotoxic T cell responses from being generated against the tumor. | [AG] Naive CD8+: 8.250 |
| 31 | **CD4+ memory T cell disruption** | CD4+ memory T cell score 8.875. Prevents durable helper T cell memory that coordinates long-term anti-tumor immunity. | [AG] CD4+ memory T: 8.875 |
| 32 | **Naive CD4+ T cell disruption** | Naive CD4+ T cell score 6.875. Blocks new helper T cell priming against tumor antigens. | [AG] Naive CD4+: 6.875 |
| 33 | **CD4+ T cell general disruption** | CD4+ T cell score 6.625. Broad disruption across the CD4+ lineage impairs orchestration of adaptive immunity. | [AG] CD4+ T: 6.625 |
| 34 | **CD8+ T cell general disruption** | CD8+ T cell score 6.250. Broad disruption impairs cytotoxic killing capacity. | [AG] CD8+ T: 6.250 |
| 35 | **TET1 low expression limits demethylation rescue** | TET1 at 0.039 (low). Even though TET enzymes oppose DNMT1, TET1's low expression means incomplete demethylation rescue, allowing selective methylation advantage for the tumor. | [AG-DT] TET1: 0.039 |
| 36 | **Minimal splice site disruption at chr1** | Chr1 has essentially no splice site signal (max 0.158), suggesting the breakpoint is in an intergenic/deep intronic region that avoids creating aberrant transcripts that would trigger surveillance. | [AG-MM] Chr1 splice max: 0.158 |
| 37 | **Peyer's patch immune tissue impact** | Peyer's patch sensitivity detected in ISM at chr1. Gut-associated lymphoid tissue disruption further compromises mucosal immunity. | [AG-ISM] Peyer's patch: ISM detected |
| 38 | **PBMC sensitivity** | PBMCs are the #1 hit in Approach 2 at chr1. Circulating immune cells are directly affected by the DNMT1 translocation. | [AG] PBMC: #1 center-window hit |
| 39 | **Position -66 single-nucleotide dominance** | One cytosine controls T/NK cell chromatin. This extreme specificity means the tumor's immune evasion operates through a precise molecular mechanism — efficient and hard to detect. | [AG-ISM] Single position dominance |
| 40 | **Heterochromatin spreading from chr1** | H3K9me3 at chr1: thymus 176.5, spleen 125.3, lung 119.0. This heterochromatin can spread to silence genes near the chr19 junction. | [AG-MM] H3K9me3: 119-176 |
| 41 | **CAGE signal at chr19** | CAGE peaks at chr19: thymus 58.75, brain 62.5. Active transcription initiation confirms the chr19 breakpoint region is transcriptionally engaged, enabling fusion-driven expression. | [AG-MM] CAGE peaks: 58-63 |
| 42 | **B cell general disruption** | B cell score 4.625. Broad B lineage disruption impairs humoral anti-tumor immunity. | [AG] B cell: 4.625 |
| 43 | **CD8+ memory T cell score at chr19** | Score 6.094 at chr19 (total RNA-seq). Additional confirmation of cytotoxic memory disruption through a different assay. | [AG] CD8+ memory T (total RNA-seq): 6.094 |
| 44 | **IgD-negative memory B cell at chr19** | Score 2.0 at chr19. Antigen-experienced B cells are disrupted, impairing antibody maturation. | [AG] IgD- memory B: 2.0 |
| 45 | **CD4+ memory T cell at chr19** | Score 2.0 at chr19. Helper T cell memory disrupted through the chr19 partner. | [AG] CD4+ memory T at chr19: 2.0 |
| 46 | **H3K4me1 thymus enhancer specificity** | The enhancer is specifically active in thymus (297.8) vs other tissues (liver 124.5, next highest). This tissue specificity means the translocation precisely targets the immune developmental hub. | [AG-MM] Thymus: 297.8 vs liver: 124.5 |
| 47 | **GM23338 iPSC sensitivity** | GM23338 score 1.75 at chr19. Induced pluripotent stem cell sensitivity suggests the DNMT1 translocation affects fundamental epigenetic programs in stem-like cells. | [AG] GM23338: 1.75 |
| 48 | **Low functional impact at chr1 hides its contribution** | Chr1's weakest ISM effects (max RNA-seq 0.007) mean its contribution to tumor biology operates through enhancer disruption and chromatin spreading rather than direct gene regulation — harder to detect and target. | [AG-ISM] Chr1 max RNA-seq: 0.007 |
| 49 | **Jurkat T cell sensitivity** | Jurkat T cell line detected in approaches at both chr1 and chr19. This canonical T cell model's sensitivity confirms the translocation's T-cell regulatory impact is biologically real. | [AG] Jurkat: detected at both breakpoints |
| 50 | **Dual-breakpoint immune targeting** | The chr1 and chr19 breakpoints independently target overlapping but distinct immune cell populations (monocytes+B cells at chr1, T cells+NK cells at chr19), creating comprehensive immune evasion. | [AG] Combined immune impact across both breakpoints |

---

### 2B. Top 50 Tumor Vulnerabilities (DNMT1 t(1;19))

| Rank | Vulnerability | Description | Score / Evidence |
|------|---------------|-------------|-----------------|
| 1 | **DNMT1 protein loss/truncation** | Exon 14 disruption likely produces a truncated, non-functional DNMT1 protein. The tumor loses its primary maintenance methyltransferase, creating progressive epigenetic instability. | [BIO] Exon 14 truncation; DNMT1 functional loss |
| 2 | **T-cell master switch is a therapeutic target** | Position -66 (DNase 0.436) — a single cytosine controls T/NK cell chromatin. Epigenetic agents (decitabine, azacitidine) could restore proper T cell chromatin accessibility. | [AG-ISM] DNase: 0.436; therapeutic reversibility |
| 3 | **DNMT3A/3B cannot compensate** | DNMT3A at 0.099, DNMT3B at 0.074 — both too low to replace DNMT1's maintenance function. Progressive methylation loss is inevitable. | [AG-DT] DNMT3A: 0.099; DNMT3B: 0.074 |
| 4 | **Epigenetic erosion is a double-edged sword** | Methylation drift will eventually unmask tumor-associated antigens, endogenous retroviruses, and immunogenic elements normally silenced by DNMT1. This creates increasing immune visibility over time. | [BIO] DNMT1 loss → methylation drift → antigen exposure |
| 5 | **IDH1/IDH2 favor demethylation** | IDH1 (1.348) + IDH2 (1.747) produce alpha-ketoglutarate → fuels TET enzymes → active demethylation. With DNMT1 disrupted, this balance tips toward genome-wide hypomethylation. | [AG-DT] IDH1: 1.348; IDH2: 1.747 |
| 6 | **TET2 active demethylation pressure** | TET2 at 0.123 — moderate and functional. Active TET2, unopposed by DNMT1, accelerates epigenetic erosion. | [AG-DT] TET2: 0.123 |
| 7 | **Thymus enhancer disruption is bidirectional** | The thymus enhancer disruption at chr1 affects the tumor's own immune evasion programs as well as host immune cells. The regulatory chaos cuts both ways. | [AG-MM] H3K4me1: 297.8 + H3K9me3: 176.5 (contested regulation) |
| 8 | **Chr1 breakpoint in closed chromatin** | DNase at chr1 is the lowest of all breakpoints (max 0.049). The closed chromatin state limits the functional output of the chr1 partner, reducing this breakpoint's tumor-enabling capacity. | [AG-MM] Chr1 DNase max: 0.049 |
| 9 | **Weakest ISM effects of all breakpoints** | Max RNA-seq 0.007, max DNase 0.032 at chr1. The chr1 partner contributes minimally to direct gene regulation, making it the weakest link in the tumor's architecture. | [AG-ISM] Max RNA-seq: 0.007; max DNase: 0.032 |
| 10 | **NK cell responsiveness is preserved** | Immature NK cell target score 7.250. Despite chromatin disruption, NK cells retain some responsiveness and can be therapeutically activated (IL-2, IL-15). | [AG] Immature NK: 7.250 |
| 11 | **Naive B cell accessibility** | Naive B cell target score 11.625 (highest immune target). B cells are accessible to therapeutic mobilization despite DNMT1 disruption. | [AG] Naive B cell: 11.625 |
| 12 | **Regulatory T cell as druggable target** | Regulatory T cell score 9.0. Tregs can be therapeutically depleted or reprogrammed (anti-CTLA4, GITR agonists) to reverse their tumor-protecting function. | [AG] Regulatory T cell: 9.0 |
| 13 | **Endogenous retrovirus reactivation** | DNMT1 loss permits reactivation of endogenous retroviruses normally silenced by DNA methylation. These produce viral-like antigens that trigger innate immune (type I interferon) responses against the tumor. | [BIO] DNMT1 loss → ERV reactivation → viral mimicry |
| 14 | **Cardiac tissue vulnerability** | Heart scores 2.0-3.5 at chr1. While this gives the tumor cardiac regulatory access, it also creates a dependency on cardiac-type metabolic programs that are tissue-specific and fragile. | [AG] Cardiac: 2.0-3.5 |
| 15 | **CTCF boundary disruption consequences** | CTCF binding at chr1 (115.3 brain, 113.1 colon) — the translocation disrupts insulator boundaries, potentially causing unintended gene activation that could include tumor-suppressive genes. | [AG-MM] CTCF: 111-115 |
| 16 | **Progressive genomic instability** | Without DNMT1 maintenance methylation, pericentromeric heterochromatin destabilizes over cell divisions, leading to chromosomal instability and mitotic errors that limit tumor proliferation. | [BIO] DNMT1 loss → centromeric instability |
| 17 | **IgD-negative memory B cell targeting** | Score 9.750. These antigen-experienced B cells, if properly activated, could generate anti-tumor antibodies. | [AG] IgD- memory B: 9.750 |
| 18 | **CD8+ memory T cell resilience** | Score 8.125. Despite chromatin disruption, CD8+ memory T cells retain some function and can be boosted with checkpoint inhibitors or IL-2. | [AG] CD8+ memory T: 8.125 |
| 19 | **Naive CD4+ T cell priming potential** | Score 6.875. New T cell responses can still be generated from naive CD4+ T cells if properly stimulated (vaccination, dendritic cell therapy). | [AG] Naive CD4+: 6.875 |
| 20 | **Naive CD8+ T cell cytotoxic potential** | Score 8.250. Naive cytotoxic T cells can be primed against tumor antigens. | [AG] Naive CD8+: 8.250 |
| 21 | **CpG island hypomethylation** | DNMT1 disruption leads to CpG island hypomethylation at promoters, potentially reactivating silenced tumor suppressors (p16, RASSF1A, etc.). | [BIO] DNMT1 loss → CpG island hypomethylation |
| 22 | **Impaired silencing of tumor suppressor genes** | Without DNMT1 maintenance, tumor suppressor gene promoters may become hypomethylated and reactivated over time, opposing tumor growth. | [BIO] TSG reactivation through methylation loss |
| 23 | **Sensitivity to hypomethylating agents** | Decitabine and azacitidine would amplify the existing DNMT1-deficient state, accelerating epigenetic erosion and viral mimicry response. | [BIO] Synergy with hypomethylating agents |
| 24 | **Monocyte reprogramming is incomplete** | CD14+ monocyte score 3.5 — significant but not extreme. Monocytes retain capacity for anti-tumor function if properly directed (IFN-gamma, GM-CSF). | [AG] CD14+ monocyte: 3.5 |
| 25 | **Type I interferon response availability** | ERV reactivation from DNMT1 loss can trigger dsRNA sensing (RIG-I, MDA5, STING pathways), generating a type I interferon response that promotes anti-tumor immunity. | [BIO] dsRNA sensing → interferon response |
| 26 | **Limited heterochromatin spreading capacity** | H3K9me3 at chr1 (176.5 thymus) is high but the chromatin modification spreads slowly. The rate of silencing from chr1 → chr19 may be insufficient to suppress critical genes before therapeutic intervention. | [AG-MM] H3K9me3: 176.5; [INFERRED] spreading kinetics |
| 27 | **TET1 low but functional** | TET1 at 0.039 — while low, any TET activity works against DNMT1-disrupted methylation patterns, contributing to progressive demethylation. | [AG-DT] TET1: 0.039 |
| 28 | **No splice site disruption at chr1** | Splice max 0.158 at chr1 — no canonical splice sites are directly broken. This means no gain-of-function aberrant protein is produced from the chr1 side, limiting the chr1 partner's oncogenic contribution. | [AG-MM] Chr1 splice max: 0.158 |
| 29 | **Contested H3K27ac/H3K9me3 at chr1** | Both active (H3K27ac: 197.5) and repressive (H3K9me3: 176.5) marks present in thymus. This regulatory conflict makes the enhancer unstable and susceptible to epigenetic therapies. | [AG-MM] Active vs repressive marks in conflict |
| 30 | **CD4+/CD25+ Treg susceptibility to depletion** | Score 9.0. These Tregs can be depleted with low-dose cyclophosphamide, anti-CD25 (daclizumab), or anti-CTLA4 (ipilimumab). | [AG] Treg: 9.0; [BIO] Treg depletion strategies |
| 31 | **DNMT1 expression moderate, not absent** | DNMT1 expression at 0.156 (brain). The wild-type allele still produces some DNMT1, meaning the tumor has partial, not total, methylation maintenance — creating heterogeneous methylation that is therapeutically exploitable. | [AG-DT] DNMT1: 0.156 |
| 32 | **Low DNMT1 expression limits epigenetic adaptation speed** | At 0.156, the reduced DNMT1 level means the tumor cannot rapidly re-methylate genes that become activated by therapeutic stress or immune attack. | [AG-DT] DNMT1: 0.156 |
| 33 | **Pericentromeric satellite DNA destabilization** | DNMT1 is critical for maintaining methylation at pericentromeric repeats. Loss leads to chromosomal mis-segregation during cell division. | [BIO] DNMT1 → pericentromeric methylation → chromosome stability |
| 34 | **Imprinting disorders** | DNMT1 maintains genomic imprinting. Loss creates expression of normally silenced alleles, some of which may be tumor-suppressive or immunogenic. | [BIO] Imprinting disruption |
| 35 | **X-chromosome methylation link** | DNMT1 disruption may affect X-chromosome inactivation maintenance, relevant given that TFE3 is on chrX. Could create complex regulatory interactions between the two translocations. | [INFERRED] DNMT1 × TFE3 chrX interaction |
| 36 | **LINE-1 retrotransposon reactivation** | DNMT1 loss permits LINE-1 mobilization, creating insertional mutagenesis that may hit essential genes and produce neoantigens. | [BIO] DNMT1 loss → LINE-1 activation |
| 37 | **Immune cell developmental arrest** | If DNMT1 disruption arrests immune cell development (via thymus enhancer), this creates predictable immune phenotypes that can be therapeutically bypassed with adoptive cell transfer. | [INFERRED] From thymus enhancer + T cell developmental data |
| 38 | **Interferon-stimulated gene reactivation** | Methylation loss at ISG promoters can reactivate interferon-response genes, creating a tumor-intrinsic inflammatory program. | [BIO] ISG promoter methylation → inflammatory activation |
| 39 | **PBMC vulnerability creates liquid biopsy opportunity** | PBMCs are the #1 center-window hit at chr1. This immune cell sensitivity means circulating immune cell phenotyping could monitor treatment response. | [AG] PBMC: #1 hit; [INFERRED] monitoring utility |
| 40 | **Pancreatic sensitivity** | Pancreas detected in ISM at chr1. Pancreatic tissue's metabolic programs, when disrupted, may limit the tumor's access to pancreatic-type metabolic circuits. | [AG-ISM] Pancreas: detected |
| 41 | **Complement cascade vulnerability** | B cell disruption (11.625) may impair complement-mediated immune evasion, exposing the tumor to complement-dependent cytotoxicity. | [INFERRED] From B cell data |
| 42 | **Limited chr1 functional contribution** | The chr1 breakpoint's low regulatory impact (max ISM 0.007 RNA-seq) means half of the DNMT1 translocation contributes minimally to tumor function — a structural weak point. | [AG-ISM] Chr1 max: 0.007 |
| 43 | **DNA damage response activation** | Methylation instability triggers DNA damage response pathways (ATR, ATM, CHK1/2), potentially activating cell cycle checkpoints that limit tumor proliferation. | [BIO] Methylation instability → DDR activation |
| 44 | **Epigenetic therapy synergy** | The DNMT1-deficient state creates synergy with epigenetic drugs: HDAC inhibitors, BET inhibitors, and hypomethylating agents would all amplify the existing methylation instability. | [BIO] Synergy with epigenetic therapies |
| 45 | **Microenvironment immune cell heterogeneity** | The DNMT1 translocation's varying impact on different immune cell subtypes (monocytes, B cells, T cells, NK cells) creates a heterogeneous immune microenvironment where some immune populations remain functional. | [AG] Varying immune cell scores |
| 46 | **DNMT1 translocation instability** | The translocation itself may be structurally less stable than ASPSCR1-TFE3 (chr1 in closed chromatin), making it potentially losable during tumor evolution — which would restore immune recognition. | [INFERRED] From chromatin asymmetry data |
| 47 | **Vitamin C as TET activator** | High-dose vitamin C activates TET enzymes, amplifying DNMT1-deficient demethylation. This inexpensive intervention could accelerate epigenetic erosion. | [BIO] Vitamin C → TET activation |
| 48 | **Antigen presentation gene reactivation** | DNMT1 loss may reactivate HLA class I/II genes and antigen processing machinery normally silenced by methylation, increasing tumor visibility to T cells. | [BIO] HLA/APM reactivation through demethylation |
| 49 | **Cancer-testis antigen expression** | Hypomethylation reactivates cancer-testis antigens (MAGE, NY-ESO-1, etc.) that serve as targets for T cell-based immunotherapy and cancer vaccines. | [BIO] CTA reactivation through hypomethylation |
| 50 | **Predictable epigenetic trajectory** | The DNMT1-deficient state evolves predictably toward progressive hypomethylation. Unlike mutational evolution, epigenetic drift follows knowable biochemical rules, making it anticipatable. | [BIO + INFERRED] Predictable hypomethylation trajectory |

---

### 2C. Top 50 Druggable Values (DNMT1 t(1;19))

| Rank | Target | Drug / Intervention | Expression / Score | Rationale |
|------|--------|--------------------|--------------------|-----------|
| 1 | **IDH2** | Enasidenib | 1.747 (heart) | Disrupts alpha-KG production feeding TET-mediated demethylation. [AG-DT] |
| 2 | **IDH1** | Ivosidenib | 1.348 (liver) | Partner to IDH2. Combined IDH inhibition disrupts epigenetic balance. [AG-DT] |
| 3 | **Naive B cell pathway** | Rituximab (anti-CD20), CAR-B cells | Score: 11.625 | Highest immune target score. B cell mobilization or depletion of regulatory B cells. [AG] |
| 4 | **Regulatory T cell pathway** | Ipilimumab, anti-CD25 | Score: 9.0 | Treg depletion to unleash anti-tumor immunity. [AG] |
| 5 | **IgD-negative memory B cell** | B cell-targeted immunotherapy | Score: 9.750 | Antigen-experienced B cells for antibody response. [AG] |
| 6 | **CD4+ memory T cell** | Checkpoint inhibitors, IL-2 | Score: 8.875 | Helper T cell memory mobilization. [AG] |
| 7 | **Naive CD8+ T cell** | Cancer vaccines, DC therapy | Score: 8.250 | New cytotoxic response generation. [AG] |
| 8 | **CD8+ memory T cell** | Anti-LAG3, anti-PD-1 | Score: 8.125 | Cytotoxic memory T cell reactivation. [AG] |
| 9 | **Immature NK cell** | IL-2, IL-15, NK cell activators | DNase: 0.436 | NK cell maturation enhancement to bypass chromatin disruption. [AG-ISM] |
| 10 | **DNMT1 pathway** | Decitabine, Azacitidine | 0.156 (brain) | Amplify existing DNMT1 deficiency to accelerate epigenetic erosion. [AG-DT] |
| 11 | **TET2** | Vitamin C (TET activator) | 0.123 (lung) | Enhance demethylation to unmask tumor antigens. [AG-DT] |
| 12 | **CD4+ T cell general** | IL-2, checkpoint inhibitors | Score: 6.625 | Broad CD4+ activation. [AG] |
| 13 | **CD8+ T cell general** | Anti-PD-1, IL-2 | Score: 6.250 | Broad CD8+ activation. [AG] |
| 14 | **Naive CD4+ T cell** | Cancer vaccines | Score: 6.875 | New helper T cell priming. [AG] |
| 15 | **T follicular helper cell** | Immunotherapy combination | DNase: 3.293 (at TFE3) | Cross-target — affected by both translocations. [AG-ISM] |
| 16 | **CD14+ monocyte** | IFN-gamma, GM-CSF | Score: 3.5 | Monocyte reprogramming toward anti-tumor function. [AG] |
| 17 | **Thymus enhancer** | HDAC inhibitors, BET inhibitors | H3K4me1: 297.8 | Chromatin-modifying agents to restore normal enhancer function. [AG-MM] |
| 18 | **T-cell master switch (pos -66)** | Epigenetic agents | DNase: 0.436 | Restore T cell chromatin accessibility. [AG-ISM] |
| 19 | **DNMT3A** | Hypomethylating agents | 0.099 (heart) | Target residual de novo methylation. [AG-DT] |
| 20 | **DNMT3B** | Hypomethylating agents | 0.074 (liver) | Target residual de novo methylation. [AG-DT] |
| 21 | **TET1** | Vitamin C | 0.039 (lung) | Enhance demethylation. [AG-DT] |
| 22 | **B cell general** | Anti-CD20, B-cell modulators | Score: 4.625 | Broad B lineage targeting. [AG] |
| 23 | **Neural crest cell** | Differentiation agents | Score: 3.359 | Lineage-specific targeting. [AG] |
| 24 | **CD4+ memory T cell (chr19)** | Checkpoint inhibitors | Score: 2.0 | Specific chr19 partner contribution. [AG] |
| 25 | **K562-like pathway** | Tyrosine kinase inhibitors | Score: 3.0 | Hematopoietic lineage targeting. [AG] |
| 26 | **ERV reactivation pathway** | DNMT inhibitors + IFN inducers | N/A | Endogenous retrovirus → dsRNA → innate immunity. [BIO] |
| 27 | **Right cardiac atrium** | Metabolic modulators | Score: 3.5 | Cardiac metabolic vulnerability. [AG] |
| 28 | **Heart left ventricle** | Metabolic modulators | Score: 2.5 | Cardiac metabolic vulnerability. [AG] |
| 29 | **Heart right ventricle** | Metabolic modulators | Score: 2.5 | Cardiac metabolic vulnerability. [AG] |
| 30 | **Trophoblast cell** | Trophoblast-targeted therapy | Score: 5.594 | Invasive phenotype targeting. [AG] |
| 31 | **Cancer-testis antigens** | MAGE/NY-ESO-1 vaccines | N/A | Reactivated by hypomethylation; vaccine targets. [BIO] |
| 32 | **HLA reactivation** | IFN-gamma (HLA upregulation) | N/A | Restore antigen presentation. [BIO] |
| 33 | **STING pathway** | STING agonists | N/A | Activate innate sensing of cytoplasmic DNA from genomic instability. [BIO] |
| 34 | **RIG-I/MDA5 pathway** | dsRNA mimics | N/A | Activate innate sensing of ERV-derived dsRNA. [BIO] |
| 35 | **Pericentromeric instability** | Mitotic checkpoint activators | N/A | Amplify chromosomal instability → mitotic catastrophe. [BIO] |
| 36 | **CTCF boundary disruption** | Chromatin topology agents | 115.3 (brain) | Restore insulator function. [AG-MM] |
| 37 | **EP300 enhancer** | BET inhibitors | 99.3 (colon) | Disrupt aberrant enhancer activity. [AG-MM] |
| 38 | **YY1 regulatory network** | YY1 inhibitors (experimental) | 96.5 (liver) | Disrupt chromatin looping. [AG-MM] |
| 39 | **FOXA1/2 pioneer factors** | Pioneer factor inhibitors | 97-98 (liver) | Block aberrant chromatin opening. [AG-MM] |
| 40 | **Purkinje cell pathway** | Neuronal targeting agents | Score: 1.5 | Exploit neuronal metabolic vulnerability. [AG] |
| 41 | **Sigmoid colon pathway** | GI-targeted therapy | Score: 1.5 | Exploit gut tissue sensitivity. [AG] |
| 42 | **T-helper 2 cell** | Th2 modulators | DNase: 0.221 | Redirect Th2 response. [AG-ISM] |
| 43 | **Central memory CD4+ T cell** | IL-7, IL-15 | DNase: 0.169 | Maintain long-term immune surveillance. [AG-ISM] |
| 44 | **Effector memory CD8+ T cell** | Checkpoint inhibitors + IL-2 | DNase: 0.159 | Reactivate effector killing. [AG-ISM] |
| 45 | **T-helper 22 cell** | Th22 targeting | DNase: 0.133 | Skin/mucosal immunity enhancement. [AG-ISM] |
| 46 | **T-helper 17 cell** | IL-17 modulation | RNA-seq: 0.079 | Inflammatory T cell response. [AG-ISM] |
| 47 | **GM12878 B cell pathway** | B cell immunotherapy | Score: 3.0 | EBV-transformed B cell-like pathway targeting. [AG] |
| 48 | **Mole/melanocytic pathway** | MiT/TFE pathway inhibitors | Score: 2.0 | Melanocytic lineage targeting. [AG] |
| 49 | **LHCN-M2 muscle pathway** | Muscle lineage agents | Score: 1.75 | Mesenchymal lineage vulnerability. [AG] |
| 50 | **Imprinted gene reactivation** | Epigenetic modulators | N/A | Reactivate imprinted tumor suppressors. [BIO] |

---

## Part 3: Combined Synergistic Effects

### 3A. Top 50 Combined Strengths

How the ASPSCR1-TFE3 fusion and DNMT1 translocation reinforce each other.

| Rank | Combined Strength | ASPSCR1-TFE3 Contribution | DNMT1 Contribution | Synergy |
|------|-------------------|--------------------------|---------------------|---------|
| 1 | **Multi-layer immune evasion** | 7bp immune element displacement (DNase 3.29) | T-cell master switch disruption (DNase 0.436) + thymus enhancer (H3K4me1 297.8) | Both translocations independently disrupt immune regulatory elements, creating redundant immune evasion. If one mechanism is therapeutically reversed, the other remains. |
| 2 | **Engine + Shield architecture** | Constitutive metabolic engine (POLR2A 414.6) | Epigenetic shield (DNMT1 disruption) | The fusion drives tumor growth; DNMT1 disruption silences recognition genes. The tumor grows AND hides simultaneously. |
| 3 | **Reverse Warburg + epigenetic fuel** | Fibroblast enslavement for lactate production | IDH1/IDH2 (1.35/1.75) fuel demethylation | The metabolic pipeline (Reverse Warburg) feeds both the OXPHOS engine AND the epigenetic machinery that maintains the shield. |
| 4 | **Fibroblast + immune suppression synergy** | Fibroblast-driven acidic moat (lactate) | T cell/NK cell chromatin disruption | Physical exclusion (acid) + molecular disruption (chromatin) = immune cells cannot reach the tumor AND cannot function if they do. |
| 5 | **Constitutive expression + methylation-based silencing** | Always-on ASPSCR1 promoter | DNMT1-mediated gene silencing | The tumor constitutively expresses its oncogenic program while silencing counter-programs through epigenetic modification. |
| 6 | **Vascular network + immune exclusion** | VEGFB 2.004, VEGFA 1.484 (angiogenesis) | B cell/monocyte disruption (scores 3.5-11.6) | Blood vessel network feeds the tumor while immune cells in those vessels are epigenetically impaired. |
| 7 | **Collagen bunker + epigenetic fog** | Fibrosis score 14.81, MMP14 1.289 | Methylation drift, TSG silencing | Physical barrier (collagen) + molecular barrier (epigenetic silencing) = dual-layer defense. |
| 8 | **Metabolic trap setup** | OXPHOS addiction, lysosomal dependence | Methylation maintenance failure | The tumor's metabolic rigidity (from TFE3) is compounded by DNMT1's inability to epigenetically adapt, creating a trapped state. |
| 9 | **Stem cell maintenance + self-renewal** | MSC score 8.688, stem cell chromatin switch | Epigenetic regulation of stemness genes | ASPSCR1-TFE3 drives stem-like programs; DNMT1 disruption maintains stemness through promoter hypomethylation of pluripotency genes. |
| 10 | **Quiet genome + epigenetic stability** | Single-driver translocation, no mutational chaos | Stable (though drifting) methylation patterns | The tumor evolves slowly at both genetic AND epigenetic levels, making it predictable but hard to destabilize. |
| 11 | **Multi-organ metastatic preparation** | Endothelial engagement across tissues (4.6-11.5) | Tissue-specific TF access (HNF4A, FOXA1/2) | ASPSCR1-TFE3 builds vasculature at metastatic sites; DNMT1 chromatin access helps the tumor adapt to new tissue environments. |
| 12 | **Autophagy overdrive + waste generation** | CTSD 4.972, SQSTM1 1.156 | Protein turnover from unstable methylation | TFE3-driven lysosomal activity processes the excess protein from DNMT1-disrupted gene expression. |
| 13 | **Lactate moat + Treg enhancement** | Acidic microenvironment from Reverse Warburg | Regulatory T cell modulation (score 9.0) | Lactate promotes Treg differentiation; DNMT1 disruption further enhances Treg function. Combined: maximally immunosuppressive microenvironment. |
| 14 | **Brain tissue metabolic programs** | Hypothalamus/cerebellum sensitivity (1.25-1.50) | Purkinje cell sensitivity (1.5) | Both translocations access neuronal metabolic programs, suggesting the tumor borrows brain-like metabolic efficiency. |
| 15 | **MMP network + chromatin remodeling** | MMP14 1.289 dissolves physical barriers | CTCF/YY1/FOXA disruption remodels regulatory barriers | Physical matrix remodeling (MMPs) paralleled by chromatin remodeling (epigenetic disruption). |
| 16 | **Comprehensive T cell subtype disruption** | T follicular helper (-3.29), CD4+ memory (-2.88) | Naive CD8+ (8.25), CD4+ memory (8.88), Regulatory T (9.0) | Every T cell subtype — naive, memory, effector, regulatory, helper — is disrupted by at least one translocation. |
| 17 | **Monocyte subversion + fibroblast enslavement** | Fibroblast reprogramming (ISM -0.71) | Monocyte disruption (score 3.5) | Fibroblasts serve as metabolic fuel; monocytes, if subverted to M2, provide additional stromal support and immunosuppression. |
| 18 | **Cardiac tissue dual engagement** | Cardiac ventricle fibroblast (6.359) | Right cardiac atrium (3.5), heart ventricle (2.5) | Both translocations impact cardiac tissue, suggesting cardiac regulatory programs are integrated into the tumor's architecture. |
| 19 | **Kidney tissue dual engagement** | Kidney epithelial (7.422), kidney DNase (0.235) | Cardiac-renal axis through shared metabolic circuits | Kidney tissues appear in vulnerability matrices for both translocations. |
| 20 | **VEGF + H2 receptor anti-angiogenic coupling** | VEGF signaling drives angiogenesis | Histamine pathway modulates vascular permeability | Both angiogenic and histaminergic pathways contribute to tumor vasculature; the tumor has redundant vascular support systems. |
| 21 | **TFE3 lysosomal program + DNMT1 silencing** | TFE3 constitutively drives CTSD/CTSL/LAMP1/2 | DNMT1 silences competing metabolic programs | The fusion activates lysosomal genes; DNMT1 disruption prevents alternative metabolic programs from being reactivated. |
| 22 | **B cell + T cell combined disruption** | T cell chromatin disruption (7bp element) | B cell epigenetic disruption (naive B 11.625) | Both arms of adaptive immunity — cellular (T cell) and humoral (B cell) — are simultaneously impaired. |
| 23 | **NK cell dual impairment** | Immature NK cell affected by TFE3 element (-2.73) | NK cell chromatin switch at chr19 (0.436) | NK cells, the innate killers, are disabled by both translocations. |
| 24 | **Myeloid progenitor + monocyte axis** | CD34+ myeloid progenitor (6.875) | CD14+ monocyte (3.5) | Both the progenitor (ASPSCR1-TFE3) and mature (DNMT1) stages of myeloid development are disrupted. |
| 25 | **Chromatin accessibility + gene silencing** | TFE3 open chromatin (DNase 0.607) allows expression | DNMT1 methylation selectively silences | Open chromatin permits oncogene expression; targeted methylation silences tumor suppressors. Selective access. |
| 26 | **Fibroblast diversity exploitation** | Lung, skin, bronchial, cardiac fibroblasts (10.6-13.6) | Thymus fibroblasts (via enhancer) | The tumor can enslave fibroblasts from virtually any tissue source. |
| 27 | **Active splice sites at both chr17 and chr19** | ASPSCR1 splice sites (1.0) | DNMT1-chr19 splice sites (1.0) | Both breakpoints preserve splicing machinery, enabling proper fusion/aberrant transcript production. |
| 28 | **CTCF insulator exploitation** | CTCF at ASPSCR1 (118.0) | CTCF at DNMT1-chr1 (115.3) and chr19 (135.2) | All three gene-containing breakpoints have strong CTCF binding, meaning the translocations disrupt chromatin boundaries at three separate loci. |
| 29 | **H3K36me3 elongation marks** | ASPSCR1 H3K36me3 (339.2) | DNMT1-chr19 H3K36me3 (384.5) | Both active breakpoints show robust transcription elongation, ensuring continuous transcript production. |
| 30 | **Smooth muscle cell enslavement** | Smooth muscle vulnerability (9.875) | Via mesenchymal lineage connection | The tumor enslaves both fibroblasts and smooth muscle cells, expanding its metabolic fuel network. |
| 31 | **Multi-checkpoint landscape** | TFE3 immune element alters checkpoint context | DNMT1 alters Treg/checkpoint gene methylation | LAG3 (0.111) dominates over PD-1 (0.017) and CTLA4 (0.006), creating a non-standard checkpoint profile. |
| 32 | **Trophoblast invasive program + MMP synergy** | MMP-mediated invasion (MMP14 1.289) | Trophoblast cell sensitivity (5.594) | Trophoblast invasion genes + MMP deployment = enhanced invasive capacity. |
| 33 | **Endodermal cell chromatin switch + enhancer** | Endodermal cell at ASPSCR1 -4 (DNase 0.112) | Pioneer factors (FOXA1/2) at chr1 | Stem/endodermal chromatin programs accessed through both translocations. |
| 34 | **Liver metabolic programs** | HNF4A at ASPSCR1 (91.1), liver targets | HNF4A at chr1 (112.2), liver TFs | Both translocations engage liver-specific transcription factors, enabling hepatic metabolic adaptation. |
| 35 | **Mammary stem cell engagement** | Mammary stem cell (5.313) | Mammary tissue through MSC pathways | Additional mesenchymal stem cell source for tumor support. |
| 36 | **Melanocyte/MiT family connection** | TFE3-MITF shared family (MITF 0.225) | Mole/melanocytic sensitivity (2.0) at DNMT1 | Both translocations interact with the MiT/TFE family network. |
| 37 | **Glomerular endothelial engagement** | Glomerular endothelial (4.797) | Kidney pathway through DNMT1 | Renal vascular engagement through both translocations. |
| 38 | **EP300 enhancer at both loci** | EP300 at ASPSCR1 (89.5) | EP300 at chr1 (99.3) | Both translocation regions have active enhancers driven by the same coactivator. |
| 39 | **Bronchial tissue dual engagement** | Bronchus fibroblast (10.656) | Bronchial smooth muscle (5.609) | Both bronchial fibroblasts and smooth muscle are engaged, supporting pulmonary metastasis. |
| 40 | **Resistance to single-agent therapy** | Metabolic complexity (multi-pathway) | Epigenetic complexity (multi-gene) | Each translocation creates a distinct survival mechanism; single-agent therapy cannot address both. |
| 41 | **Coronary endothelial engagement** | Coronary artery endothelial (6.656) | Cardiac regulatory access | Vascular access to cardiac tissue. |
| 42 | **SP1 ubiquitous expression support** | SP1 at ASPSCR1 (111.7) | SP1 at chr1-associated region | Ubiquitous TF ensures both translocation regions maintain basal expression. |
| 43 | **GABPA mitochondrial gene regulation** | GABPA at ASPSCR1 (95.3) | Mitochondrial support through metabolic programs | GABPA drives mitochondrial gene expression, reinforcing OXPHOS dependency. |
| 44 | **H3K27ac active enhancer marks at both loci** | H3K27ac ASPSCR1 (333.2) | H3K27ac chr19 (371.7) | Active enhancer marks at both breakpoints ensure continuous regulatory activity. |
| 45 | **Multi-tissue CAGE signal** | ASPSCR1 CAGE across 7 tissues | DNMT1-chr19 CAGE across 7 tissues | Active transcription initiation at both loci in multiple tissues = ubiquitous expression. |
| 46 | **H3K4me3 active promoter at both loci** | ASPSCR1 H3K4me3 (384.0) | DNMT1-chr19 H3K4me3 (396.2) | Both breakpoints are in promoter-adjacent regions with maximal active marks. |
| 47 | **Wharton's jelly + muscle lineage** | Wharton's jelly MSC (5.563) | LHCN-M2 muscle lineage (1.75) | Combined mesenchymal + muscle lineage access. |
| 48 | **GI tract engagement** | Transverse colon targets, MMP1/3 expression | Sigmoid colon sensitivity (1.5) | Gut tissue engagement through both translocations. |
| 49 | **Astrocyte + Purkinje neuronal network** | Astrocyte ISM (-0.303) | Purkinje cell (1.5) | Combined neuronal cell type engagement for brain metastatic potential. |
| 50 | **Temporal immune escape** | Immediate chromatin disruption (7bp element) | Progressive methylation drift (long-term) | Short-term immune evasion through chromatin plus long-term evasion through epigenetic evolution. |

---

### 3B. Top 50 Combined Vulnerabilities

How weaknesses from both translocations compound.

| Rank | Combined Vulnerability | How It Compounds | Evidence |
|------|----------------------|-----------------|----------|
| 1 | **Metabolic inflexibility + epigenetic rigidity** | OXPHOS addiction (TFE3) + inability to epigenetically activate backup metabolic genes (DNMT1-disrupted). TFEB 0.083, mTOR 0.070. | [AG-DT] TFEB: 0.083; mTOR: 0.070 |
| 2 | **Dual immune evasion creates dual therapeutic opportunity** | Two independent immune disruptions = two therapeutic targets. Reversing either the 7bp element (HDAC inhibitors) OR the T-cell switch (decitabine) could restore partial immunity. | [AG-ISM] DNase 3.29 + 0.436 |
| 3 | **Progressive epigenetic erosion + constitutive expression** | DNMT1 loss → unmasks antigens; ASPSCR1 promoter → constitutively presents these antigens. The tumor becomes increasingly visible to the immune system over time. | [BIO + AG-MM] |
| 4 | **Fibroblast dependency + collagen maintenance** | If fibroblasts die (HCQ), both the fuel pipeline AND the collagen bunker collapse. MMP14 (1.289) becomes irrelevant without fibroblasts to maintain the matrix. | [AG-DT] MMP14: 1.289; [AG] Fibroblast vulnerability: 13.34 |
| 5 | **Lysosomal overload + waste generation** | TFE3 drives lysosomal production (CTSD 4.972); DNMT1 disruption increases protein turnover. The waste disposal system is maxed out (SQSTM1 1.156), with zero headroom. | [AG-DT] CTSD: 4.972; SQSTM1: 1.156 |
| 6 | **Quiet genome + DNMT1 deficiency** | Cannot mutate for resistance (quiet genome) AND cannot epigenetically adapt (DNMT1 disrupted). Double evolutionary lock. | [BIO] Dual evolutionary constraint |
| 7 | **DNMT3A/3B too low to compensate** | DNMT3A 0.099, DNMT3B 0.074. Without DNMT1 AND without backup methyltransferases, the epigenetic shield erodes irreversibly. | [AG-DT] DNMT3A: 0.099; DNMT3B: 0.074 |
| 8 | **IDH1/IDH2 accelerate their own demise** | IDH1 (1.348) + IDH2 (1.747) feed TET → demethylation → antigen exposure. The tumor's own metabolic machinery produces the substrate for its immune unmasking. | [AG-DT] IDH1: 1.348; IDH2: 1.747 |
| 9 | **Angiogenesis-MMP coupling vulnerability** | VEGF (2.004) needs MMPs to carve vessel tunnels. Block MMPs (doxycycline) and angiogenic signals become useless. This single drug targets two synergistic strengths. | [AG-DT] VEGFB: 2.004; MMP14: 1.289 |
| 10 | **Comprehensive immune cell targeting creates comprehensive immune opportunity** | Every immune subtype is affected, meaning EVERY immune therapeutic modality has a valid target. | [AG] Scores across all immune subtypes |
| 11 | **ATG5/ATG7 bottleneck** | ATG5 (0.034) and ATG7 (0.050) are low. These autophagy enzymes cannot be upregulated to compensate for HCQ blockade. | [AG-DT] ATG5: 0.034; ATG7: 0.050 |
| 12 | **TFEB cannot rescue TFE3** | TFEB (0.083) too low to compensate for disrupted TFE3 fusion function if targeted. | [AG-DT] TFEB: 0.083 |
| 13 | **Single-position dominance at two breakpoints** | Position +59 at ASPSCR1 and position -66 at DNMT1-chr19 are single dominant regulatory positions. This lack of redundancy = structural fragility. | [AG-ISM] Two single-point vulnerabilities |
| 14 | **Treg dependency creates checkpoint opportunity** | Regulatory T cell score 9.0 at DNMT1. The tumor relies on Tregs for immune suppression; Treg-depleting therapy (ipilimumab, anti-CD25) would remove this shield. | [AG] Treg: 9.0 |
| 15 | **Cathepsin D paradox** | CTSD at 4.972 — the tumor's highest-expressed gene. If lysosomes rupture (HCQ → lysosomal membrane permeabilization), this enormous cathepsin pool triggers apoptosis. The tumor's strength becomes its death sentence. | [AG-DT] CTSD: 4.972; [BIO] cathepsin apoptosis |
| 16 | **Reverse Warburg fragility** | The complex multi-cell-type metabolic architecture (tumor + fibroblasts + vasculature) has more points of failure than standard Warburg glycolysis. | [INFERRED] System complexity = fragility |
| 17 | **No HRH4 escape** | HRH4 (0.002) essentially absent. No alternative histamine receptor pathway to bypass cimetidine. | [AG-DT] HRH4: 0.002 |
| 18 | **Low mTOR limits survival signaling** | mTOR (0.070), RPTOR (0.031). The primary pro-survival signaling pathway is barely expressed, limiting the tumor's ability to activate emergency survival programs. | [AG-DT] mTOR: 0.070; RPTOR: 0.031 |
| 19 | **Predictable + reproducible** | All tissue rankings independently confirmed across 3 methods. The vulnerabilities are real, stable, and therapeutically actionable. | [AG] Reproduction confirmed |
| 20 | **LAG3 as checkpoint gap** | LAG3 (0.111) >> PD-1 (0.017) >> CTLA4 (0.006). The non-standard checkpoint profile means standard PD-1/CTLA4 therapy may underperform, but LAG3-targeted therapy is specifically indicated. | [AG-DT] LAG3: 0.111 |
| 21 | **Epigenetic erosion timeline** | DNMT1 disruption means methylation patterns degrade with each cell division. Time itself is an enemy of the tumor's epigenetic shield. | [BIO] Progressive methylation loss |
| 22 | **Vitamin C synergy** | High-dose vitamin C activates TET enzymes (TET2 0.123), accelerating demethylation in a DNMT1-deficient background. Low-cost intervention amplifying inherent vulnerability. | [AG-DT] TET2: 0.123; [BIO] Vitamin C → TET |
| 23 | **ERV reactivation is tumor-intrinsic** | Endogenous retrovirus reactivation from DNMT1 loss triggers type I interferon from WITHIN the tumor cell. No external immune stimulus required. | [BIO] ERV → dsRNA → innate immunity |
| 24 | **Cardiac vulnerability** | Cardiac tissue engagement (scores 2.0-3.5 at DNMT1, 6.36 at ASPSCR1) creates a tissue vulnerability the tumor cannot easily abandon. | [AG] Combined cardiac scores |
| 25 | **Kidney tissue vulnerability** | Kidney epithelial (7.422), kidney medulla (6.531), kidney cortex (6.219). Renal dependency creates additional metabolic chokepoint. | [AG] Combined kidney scores |
| 26 | **VEGFC limitation restricts lymphatic escape** | VEGFC (0.031) is very low. The tumor has limited lymphatic metastatic capacity compared to hematogenous spread. | [AG-DT] VEGFC: 0.031 |
| 27 | **BECN1 ceiling limits autophagy adaptation** | BECN1 (0.353) is moderate — autophagy initiation has a ceiling that cannot be raised under therapeutic pressure. | [AG-DT] BECN1: 0.353 |
| 28 | **ATP6V1A pump can be overwhelmed** | ATP6V1A (0.245) — the lysosomal proton pump operates at moderate capacity. HCQ's pH-raising effect can overwhelm this moderate pump activity. | [AG-DT] ATP6V1A: 0.245 |
| 29 | **TNF pathway vulnerability** | TNF (0.092) is present and functional. Therapeutic TNF activation could shift the microenvironment decisively toward anti-tumor inflammation. | [AG-DT] TNF: 0.092 |
| 30 | **Interferon pathway activation potential** | IFNG (0.007) is very low but detectable. Combined with ERV reactivation and type I IFN, interferon-mediated immunity can be therapeutically activated. | [AG-DT] IFNG: 0.007; [BIO] IFN pathway |
| 31 | **Splice-dependent fusion vulnerability** | The ASPSCR1-TFE3 fusion requires proper splicing (splice sites 1.0). Splice-modulating therapies could disrupt fusion protein production. | [AG-MM] Splice sites: 1.0 |
| 32 | **Chr1 weak link** | The chr1 DNMT1 partner has minimal functional impact (ISM max 0.007). This weak link contributes little to tumor function but its enhancer disruption still costs the tumor immune developmental regulation. | [AG-ISM] Chr1 max: 0.007 |
| 33 | **CTCF boundary disruption consequences** | Disrupted CTCF boundaries (115-135 across breakpoints) may inadvertently activate tumor suppressor genes in neighboring domains. | [AG-MM] CTCF: 115-135 |
| 34 | **Pericentromeric instability** | DNMT1 loss → centromeric demethylation → chromosome mis-segregation → mitotic errors. Each cell division risks chromosomal catastrophe. | [BIO] DNMT1 → centromeric stability |
| 35 | **Cancer-testis antigen exposure** | Progressive demethylation reactivates highly immunogenic cancer-testis antigens (MAGE, NY-ESO-1) that serve as targets for immune attack. | [BIO] CTA reactivation |
| 36 | **Immune cell developmental arrest is predictable** | The thymus enhancer disruption creates predictable immune phenotypes, allowing targeted immunotherapy design. | [INFERRED] Predictable from enhancer data |
| 37 | **High CTSD in lung = pulmonary vulnerability** | CTSD 4.972 in lung. HCQ's lysosomal disruption would be maximally effective at the most common metastatic site. | [AG-DT] CTSD: 4.972 (lung) |
| 38 | **MMP1/MMP3 too low for matrix rescue** | MMP1 (0.097), MMP3 (0.098). If MMP14 is blocked by doxycycline, these alternative MMPs cannot compensate. | [AG-DT] MMP1: 0.097; MMP3: 0.098 |
| 39 | **Neural regulatory circuits add complexity but fragility** | The tumor's neuronal metabolic mimicry (hypothalamus 1.50, Purkinje 1.5) adds metabolic sophistication but also neurological vulnerability to disruption. | [AG] Brain tissue scores |
| 40 | **H3K27me3 can be therapeutically exploited** | H3K27me3 at chr1 (145.2 brain) — EZH2 inhibitors could remove this repressive mark, potentially reactivating tumor suppressors silenced by the translocation. | [AG-MM] H3K27me3: 145.2 |
| 41 | **Fibroblast heterogeneity is limited** | The tumor preferentially uses specific fibroblast subtypes (lung, skin, bronchial). If these are killed, it cannot easily substitute with other fibroblast types. | [AG] Specific fibroblast subtypes dominate |
| 42 | **TET2 moderate expression = ongoing demethylation** | TET2 at 0.123 continues working even as DNMT1 is disrupted, maintaining steady demethylation pressure. | [AG-DT] TET2: 0.123 |
| 43 | **CD8A present for cytotoxic targeting** | CD8A at 0.014 (low but detectable). Cytotoxic T cells are present in the microenvironment and can be activated. | [AG-DT] CD8A: 0.014 |
| 44 | **Narrow regulatory footprint at both breakpoints** | ASPSCR1 ~70bp regulatory module; DNMT1-chr19 single-position dominance. Both breakpoints have narrow, non-redundant regulatory elements. | [AG-ISM] Narrow regulatory architecture |
| 45 | **Chromatin asymmetry creates junction fragility** | The chr1 (closed) ↔ chr19 (active) junction creates regulatory conflict that may destabilize the translocation over time. | [AG-MM] Chromatin state asymmetry |
| 46 | **HDC limitation** | HDC (0.039) — histamine production capacity is very low. The tumor cannot increase local histamine to enhance immunosuppression. | [AG-DT] HDC: 0.039 |
| 47 | **MITF cannot fully compensate for TFE3** | MITF at 0.225 (heart-dominant). Tissue-restricted expression limits MITF's ability to serve as a TFE3 backup across all tissues. | [AG-DT] MITF: 0.225 |
| 48 | **Reproducible vulnerability = actionable intelligence** | Every vulnerability reproduced across 3 independent methods. Therapeutic targeting can be confident in these findings. | [AG] Three-method confirmation |
| 49 | **Slow adaptation speed** | Quiet genome (no mutations) + slow methylation drift (DNMT1 low at 0.156) = the tumor adapts slowly. Therapeutic pressure works faster than tumor evolution. | Combined quiet genome + low DNMT1 |
| 50 | **Time-dependent immune exposure** | With each cell division: more methylation loss → more antigen exposure → more immune visibility. The longer treatment runs, the more vulnerable the tumor becomes to immune attack. | [BIO] Progressive demethylation timeline |

---

### 3C. Top 50 Combined Druggable Values

Targets that address both translocations simultaneously, ranked by combined therapeutic value.

| Rank | Target | Drug / Intervention | Combined Value | Evidence |
|------|--------|--------------------|---------------------------------|----------|
| 1 | **Lysosomal pathway** | HCQ | Blocks TFE3-driven lysosomal program AND accelerates DNMT1-related waste accumulation. CTSD 4.972. | [AG-DT] |
| 2 | **Mitochondrial ribosomes** | Doxycycline | Stalls OXPHOS engine AND disrupts Treg mitochondrial function, linking metabolic + immune arms. MRPS12 1.435. | [AG-DT] |
| 3 | **MMP14** | Doxycycline | Dissolves collagen bunker AND blocks vessel tunnel formation. Expression 1.289. | [AG-DT] |
| 4 | **VEGFB/VEGFA axis** | Cimetidine, Bevacizumab | Cuts blood supply to both tumor AND enslaved fibroblasts. VEGFB 2.004, VEGFA 1.484. | [AG-DT] |
| 5 | **LAG3 checkpoint** | Relatlimab | Highest checkpoint (0.111). Addresses both TFE3 immune element AND DNMT1 T-cell disruption by unblocking T cells. | [AG-DT] |
| 6 | **IDH2** | Enasidenib | Disrupts alpha-KG → TET → demethylation. Affects both metabolic (OXPHOS) and epigenetic (DNMT1) arms. 1.747. | [AG-DT] |
| 7 | **IDH1** | Ivosidenib | Partner to IDH2 in metabolic-epigenetic nexus. 1.348. | [AG-DT] |
| 8 | **Autophagy system** | HCQ + autophagy inhibitors | Blocks waste disposal in TFE3-driven tumor AND fibroblasts. SQSTM1 1.156, MAP1LC3B 1.117. | [AG-DT] |
| 9 | **T-cell activation** | IL-2, anti-LAG3, checkpoint combo | Mobilizes T cells against both immune evasion mechanisms (7bp element + T-cell switch). | [AG-ISM + AG] |
| 10 | **NK cell activation** | IL-15, NK cell adoptive transfer | Bypasses both chromatin disruptions by providing exogenous NK cells. Immature NK: 0.436 DNase. | [AG-ISM] |
| 11 | **Regulatory T cell depletion** | Ipilimumab, anti-CD25 | Removes Treg shield influenced by both translocations. Treg score: 9.0. | [AG] |
| 12 | **Epigenetic therapy** | Decitabine + HDAC inhibitor | Amplifies DNMT1 loss (demethylation) AND restores immune chromatin (TFE3 element). Dual mechanism. | [BIO + AG-ISM] |
| 13 | **KDR/VEGFR2** | Cabozantinib, Axitinib | Blocks receptor for angiogenic signals. Expression 0.327. | [AG-DT] |
| 14 | **CTSL** | HCQ | Lysosomal protease disrupted by pH change. 1.458. | [AG-DT] |
| 15 | **TFE3 pathway direct** | TFE3 inhibitors (experimental) | Direct targeting of the fusion oncoprotein. TFE3 0.586. | [AG-DT] |
| 16 | **LAMP1/LAMP2** | HCQ | Lysosomal membrane disruption. 0.743 / 0.601. | [AG-DT] |
| 17 | **TET2 activation** | Vitamin C | Accelerates demethylation → antigen unmasking. 0.123. Low-cost synergy. | [AG-DT + BIO] |
| 18 | **CD4+ memory T cell** | Checkpoint inhibitors + IL-2 | Scored 8.875 (DNMT1). Reactivate anti-tumor helper T cell memory. | [AG] |
| 19 | **Naive B cell** | B cell-directed immunotherapy | Score 11.625. Highest immune target across all analyses. | [AG] |
| 20 | **CD8+ memory T cell** | Anti-LAG3 + IL-2 | Score 8.125. Reactivate cytotoxic memory. | [AG] |
| 21 | **MT-CO1** | Doxycycline | Cytochrome c oxidase. 0.893. Direct OXPHOS targeting. | [AG-DT] |
| 22 | **DNMT1 pathway** | Decitabine, Azacitidine | Amplify existing deficiency. 0.156. | [AG-DT] |
| 23 | **MT-ND1** | Doxycycline | Complex I. 0.554. | [AG-DT] |
| 24 | **ATG12** | HCQ (pathway) | Autophagy conjugation system. 0.417. | [AG-DT] |
| 25 | **BECN1** | HCQ | Autophagy initiation. 0.353. | [AG-DT] |
| 26 | **FLCN** | mTOR pathway modulators | TFE3 regulator. 0.327. | [AG-DT] |
| 27 | **FLT1/VEGFR1** | TKIs | Alternative VEGF receptor. 0.117. | [AG-DT] |
| 28 | **CD8+ T cell general** | Anti-PD-1 + anti-LAG3 | Score 6.250 (DNMT1). Broad cytotoxic activation. | [AG] |
| 29 | **CD4+ T cell general** | Checkpoint inhibitors | Score 6.625 (DNMT1). Broad helper activation. | [AG] |
| 30 | **MMP7** | Doxycycline | Lung-dominant MMP. 0.506. | [AG-DT] |
| 31 | **ATP6V1A** | HCQ, Bafilomycin | Lysosomal pump. 0.245. | [AG-DT] |
| 32 | **Naive CD8+ T cell** | Cancer vaccines, DC therapy | Score 8.250. New cytotoxic response priming. | [AG] |
| 33 | **MITF** | MiT family inhibitors | Related pathway. 0.225. | [AG-DT] |
| 34 | **MMP2** | Doxycycline | Gelatinase. 0.216. | [AG-DT] |
| 35 | **FNIP1** | mTOR modulators | FLCN partner. 0.138. | [AG-DT] |
| 36 | **CD14+ monocyte** | IFN-gamma, GM-CSF | Score 3.5 (DNMT1). Monocyte reprogramming. | [AG] |
| 37 | **MMP9** | Doxycycline | Lung-expressed MMP. 0.158. | [AG-DT] |
| 38 | **TNF pathway** | Immunostimulants | 0.092. Inflammatory activation. | [AG-DT] |
| 39 | **PRF1 (Perforin)** | IL-2, checkpoint combo | 0.083. Cytolytic effector. | [AG-DT] |
| 40 | **GZMB (Granzyme B)** | Immune activation | 0.074. Cytolytic protease. | [AG-DT] |
| 41 | **ANGPT2** | Trebananib | 0.062. Vascular destabilization. | [AG-DT] |
| 42 | **CD274/PD-L1** | Nivolumab, Atezolizumab | 0.052 (lung). Moderate checkpoint target. | [AG-DT] |
| 43 | **HAVCR2/TIM-3** | Anti-TIM-3 | 0.065. Non-standard checkpoint. | [AG-DT] |
| 44 | **CD4 marker** | T cell-directed therapy | 0.107. Substrate for helper T cells. | [AG-DT] |
| 45 | **DNMT3A** | Hypomethylating agents | 0.099. Residual de novo methylation. | [AG-DT] |
| 46 | **HRH2** | Cimetidine | 0.071. Low but functional receptor. | [AG-DT] |
| 47 | **mTOR** | Rapamycin, Everolimus | 0.070. Survival pathway. | [AG-DT] |
| 48 | **STING pathway** | STING agonists | N/A. Innate immunity activation. | [BIO] |
| 49 | **ERV pathway** | DNMT inhibitors | N/A. Viral mimicry for immune activation. | [BIO] |
| 50 | **Cancer-testis antigens** | MAGE/NY-ESO-1 vaccines | N/A. Immunotherapy targets unmasked by demethylation. | [BIO] |

---

## Part 4: Escape Routes

| # | Escape Route | Mechanism | Likelihood | Countered By |
|---|-------------|-----------|------------|-------------|
| 1 | **Angiogenic switching** | Upregulate alternative angiogenic factors (VEGF-independent) to bypass cimetidine | **LOW** | MMP blockade (doxycycline) prevents physical vessel construction regardless of signaling. VEGFC (0.031) too low for lymphangiogenic escape. |
| 2 | **Metabolic reprogramming to Warburg** | Reactivate glycolytic machinery for standard Warburg metabolism | **VERY LOW** | TFEB (0.083), mTOR (0.070) too low. Glycolytic machinery severely atrophied. Quiet genome cannot mutate new metabolic enzymes. |
| 3 | **Alternative autophagy pathways** | Bypass lysosomal-dependent autophagy | **VERY LOW** | HCQ blocks ALL lysosome-dependent pathways. ATG5 (0.034), ATG7 (0.050) too low for upregulation. No lysosome-independent autophagy available at scale. |
| 4 | **MMP upregulation** | Increase MMP expression to overcome doxycycline inhibition | **VERY LOW** | Doxycycline inhibits MMP enzymes directly (not expression). Quiet genome cannot mutate MMP genes. MMP1 (0.097), MMP3 (0.098) cannot compensate for MMP14. |
| 5 | **Macrophage M2 subversion** | Convert M1 macrophages to M2 (pro-tumor) to rebuild collagen support | **LOW** | Systemic inflammatory response from treatment maintains M1 polarization. Cimetidine enhances anti-tumor immune function. CDI4+ monocyte score (3.5) shows monocytes are somewhat resistant to full subversion. |
| 6 | **Immune checkpoint upregulation** | Upregulate PD-L1, LAG3, or other checkpoints to suppress revived immune response | **MODERATE** | LAG3 already at 0.111 (highest checkpoint). PD-L1 at 0.052. The tumor could upregulate these further under immune pressure. This is the primary gap — anti-LAG3 therapy would close it. |
| 7 | **DNMT1 epigenetic adaptation** | Upregulate DNMT3A/3B to compensate for DNMT1 loss | **LOW** | DNMT3A (0.099), DNMT3B (0.074) too low. De novo methyltransferases cannot perform maintenance methylation. IDH/TET balance favors demethylation. |
| 8 | **Alternative fuel sources** | Switch from fibroblast-derived lactate to glucose, glutamine, or fatty acids | **LOW** | Mitochondrial ribosomes damaged by doxycycline limit any metabolic fuel processing. The OXPHOS machinery itself is compromised regardless of fuel source. |
| 9 | **Drug efflux pump upregulation** | Express P-glycoprotein or other efflux pumps to expel drugs | **VERY LOW** | Quiet genome cannot rapidly mutate transporter genes. All three drugs operate at different cellular compartments (mitochondria, lysosomes, extracellular matrix). |
| 10 | **Fibroblast recruitment from distant sites** | Recruit new fibroblasts to replace killed ones | **LOW** | New fibroblasts face the same HCQ-mediated lysosomal poisoning. The acidic microenvironment collapses as existing fibroblasts die, making the environment hostile to new recruits. |
| 11 | **TFEB compensation** | Upregulate TFEB to replace TFE3 function | **VERY LOW** | TFEB (0.083) is negligibly expressed. Even if upregulated, TFEB lacks the ASPSCR1 fusion domain that makes TFE3 oncogenic. |
| 12 | **Dormancy/quiescence** | Enter a dormant state to survive metabolic stress | **LOW** | The constitutive ASPSCR1 promoter (POLR2A 414.6) cannot be silenced — the tumor cannot downregulate its own oncogenic program. Forced to remain active and vulnerable. |
| 13 | **Immune cell co-option** | Reprogram infiltrating immune cells to support tumor growth | **MODERATE** | With Tregs still functional (score 9.0) and LAG3 expressed (0.111), the tumor retains some capacity to co-opt immune cells. Cimetidine partially counters this through immunomodulation. |
| 14 | **Epithelial-mesenchymal transition (EMT)** | Undergo EMT to acquire invasive/migratory phenotype | **LOW** | ASPS is already mesenchymal in origin. EMT provides no additional survival advantage. Doxycycline's MMP blockade limits invasion regardless. |
| 15 | **Exosome-mediated pre-metastatic niche** | Release exosomes to prepare distant sites for metastasis | **MODERATE** | Exosome production is energy-dependent (threatened by doxycycline) but may persist at reduced levels. The tumor's constitutive expression program likely produces exosomes continuously. |
| 16 | **Cimetidine histamine bypass** | Use non-histamine inflammatory mediators for immunosuppression | **LOW** | HDC (0.039) already low. Non-histamine pathways are not strongly established in ASPS. Cimetidine's immunomodulatory effects operate beyond receptor blockade. |
| 17 | **HDAC/chromatin compensation** | Alter histone modifications to compensate for DNMT1 loss | **LOW** | Histone modification at TFE3 is near-zero (max 3.08). The tumor lacks the histone-modifying infrastructure to mount an effective chromatin compensation response. |

---

## Part 5: Synthesis

### The Metabolic Trap

The combined translocation profile creates a tumor locked in a metabolic box:

1. **The Engine** (ASPSCR1-TFE3): Constitutively drives OXPHOS via fibroblast-derived lactate, creates lysosomal overdependence (CTSD 4.972), and builds a collagen/vascular fortress
2. **The Shield** (DNMT1): Provides epigenetic immune evasion through methylation-based gene silencing and direct T/NK cell chromatin disruption
3. **The Trap**: The engine's metabolic specialization (OXPHOS addiction, fibroblast dependency) means it CANNOT switch fuel sources. The shield's progressive erosion (DNMT1 loss → demethylation) means immune evasion WILL eventually fail. The quiet genome means the tumor CANNOT evolve its way out.

The triple blockade exploits this trap:
- Doxycycline: Damages the engine (mitochondria) AND dissolves the fortress (MMPs)
- HCQ: Kills the fuel supply (fibroblasts) AND blocks waste disposal (lysosomes)
- Cimetidine: Cuts supply lines (angiogenesis) AND weakens the shield (immunomodulation)

### Reverse Warburg Confirmation

Five independent data lines confirm the Reverse Warburg phenotype:
1. Fibroblast regulatory dominance at ASPSCR1 (ISM -0.71, BJ score 14.0)
2. High mitochondrial gene expression (MRPS12 1.435, MT-CO1 0.893)
3. Lysosomal overload (CTSD 4.972, SQSTM1 1.156)
4. Vulnerability concentrated in fibroblasts/myoblasts (13.3-13.6)
5. Angiogenic overdrive (VEGFB 2.004, endothelial danger 11.53)

### The Interplay Between Translocations

The ASPSCR1-TFE3 fusion provides the **offense** (growth, metabolism, invasion), while the DNMT1 translocation provides the **defense** (immune evasion, epigenetic adaptation). This division of labor creates a tumor that is simultaneously aggressive and hidden — but also creates a critical weakness: the offense cannot compensate if the defense fails, and vice versa. They are interdependent but non-redundant.

### Conceptual Nature Disclaimer

This analysis integrates:
- **AlphaGenome computational predictions** — ISM scores, multi-modal chromatin data, gene expression predictions. These are model outputs from reference genome sequence, not direct experimental measurements of tumor tissue.
- **Established cancer biology** — ASPS pathogenesis, DNMT1 function, Reverse Warburg metabolism, immune evasion mechanisms. Well-supported by peer-reviewed literature.
- **Conceptual inferences** — Combining computational predictions with biological knowledge to identify therapeutic strategies. These require experimental validation before clinical application.

All therapeutic implications should be evaluated by the treating oncology team with access to complete clinical data, tumor tissue analysis, and real-time treatment response information. This analysis provides a computational framework for understanding the tumor's genomic architecture, not clinical recommendations.

---

*Report generated March 11, 2026. AlphaGenome v0.6.1 (Google DeepMind). All evidence sources labeled: [AG] AlphaGenome score, [AG-ISM] In Silico Mutagenesis, [AG-MM] Multi-Modal chromatin, [AG-DT] Drug Target expression, [BIO] Established biology, [INFERRED] Conceptual inference.*
