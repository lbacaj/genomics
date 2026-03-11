# Splice Site Usage & Splice Junction Analysis Report
### Date: March 11, 2026
### Patient: Johnny | ASPS Genomic Profile
### Genomic Drivers: ASPSCR1-TFE3 Fusion (chr17/chrX) + DNMT1 Translocation (chr19/chr1)

---

## What We Ran

We used AlphaGenome's `SPLICE_SITE_USAGE` and `SPLICE_JUNCTIONS` output types — which go beyond the basic `SPLICE_SITES` used in the initial analysis — to predict:

1. **Which splice sites are actively used** at each breakpoint (fraction of transcripts using each site, stranded, tissue-resolved)
2. **Splice junction counts** (split-read predictions showing which exon-exon junctions form)
3. **Variant effects on splicing** (whether mutations at the breakpoints alter splice site usage)
4. **Standard splice site density** (donor/acceptor counts near each breakpoint)

**Four breakpoints analyzed:**
- ASPSCR1 — chr17:82,010,811 (+ strand gene)
- TFE3 — chrX:49,043,986 (- strand gene)
- DNMT1 partner — chr1:31,048,832 (near LAPTM5)
- DNMT1 primary — chr19:10,160,241 (DNMT1 gene body)

**Prediction parameters:**
- Context: 1MB (SEQUENCE_LENGTH_1MB)
- Output types: SPLICE_SITE_USAGE (20 tracks, 5 tissues, both strands), SPLICE_JUNCTIONS (10 tracks, JunctionData format)
- Tissues: Brain, Transverse colon, Lung, Spleen, Liver
- Analysis windows: 1kb, 5kb, 25kb around each breakpoint
- Variant scoring: CenterMaskScorer on SPLICE_SITE_USAGE (width=501, DIFF_MEAN aggregation)

---

## Key Findings

### 1. ASPSCR1 breakpoint sits in a densely spliced + strand region

The ASPSCR1 breakpoint at chr17:82,010,811 is surrounded by active splice sites exclusively on the + strand, consistent with ASPSCR1 being a + strand gene.

| Window | Active splice sites | Strand | Max usage | Mean usage |
|--------|-------------------|--------|-----------|------------|
| 1kb | 4 per tissue track | + only | 0.977 (brain, liver) | 0.95-0.97 |
| 5kb | 10 per tissue track | + only | 0.977 | 0.90-0.97 |
| 25kb | 65 (+ strand), 9 (- strand) | Both | 0.981 | 0.86-0.95 |

**Key positions within 5kb:**
- **chr17:82,010,867 (bp+56):** Usage 0.93-0.98 across all tissues — this is the ASPSCR1 exon 10 splice site identified in the fusion junction analysis
- **chr17:82,011,604 (bp+793):** Usage 0.93-0.98 — next downstream splice site
- **chr17:82,011,542 (bp+731):** Usage 0.93-0.98
- **chr17:82,012,230 (bp+1,419):** Usage 0.93-0.98
- **chr17:82,009,190 to 82,009,485 (bp-1,621 to bp-1,326):** Usage 0.91-0.97

**Splice junctions:** Strong junction signal (max scores 35-61 across tissues, sum 489-783 within 25kb window). The highest junction scores are in transverse colon (max 60.9) and spleen (max 52.6), indicating these tissues have the most active splicing at this locus.

**Standard splice sites:** 1 donor + 1 acceptor within 500bp; 6 donors + 6 acceptors within 2kb; 18 donors + 17 acceptors within 10kb.

### 2. TFE3 breakpoint has sparse, - strand-only splice activity

The TFE3 breakpoint at chrX:49,043,986 shows a strikingly different pattern — only a single active splice site within 1kb, exclusively on the - strand (consistent with TFE3 being a - strand gene).

| Window | Active splice sites | Strand | Max usage | Mean usage |
|--------|-------------------|--------|-----------|------------|
| 1kb | 1 per tissue track | - only | 0.973 (brain) | 0.92-0.97 |
| 5kb | 6 per tissue track | - only | 0.973 | 0.77-0.85 |
| 25kb | 21 (+ strand), 19 (- strand) | Both | 0.977 (- strand) | 0.57-0.72 (+ strand), 0.85-0.93 (- strand) |

**Key positions within 5kb:**
- **chrX:49,043,110 (bp-876):** The nearest splice site — usage 0.92-0.97 across all tissues. This is the first TFE3 exon splice site downstream of the breakpoint (the same site identified as appearing at junction+875 in the fusion junction analysis).
- **chrX:49,040,454 (bp-3,532):** Usage 0.91-0.97 — a TFE3 exon boundary
- **chrX:49,040,567 (bp-3,419):** Usage 0.88-0.96
- **chrX:49,039,106 (bp-4,880):** Usage 0.86-0.94
- **chrX:49,039,409 (bp-4,577):** Usage 0.80-0.91

**Splice junctions:** Lower junction signal than ASPSCR1 (max scores 3.5-12.7, sum 122-360 within 25kb). Spleen shows highest activity (max 11.4), liver the lowest (max 4.5). The 876bp gap between breakpoint and nearest splice site is consistent with the ~875bp "intron-like" region spanning the fusion junction identified in the fusion analysis.

**Standard splice sites:** 0 donors, 0 acceptors within 500bp; 1 donor within 2kb; 9 donors + 7 acceptors within 10kb.

### 3. DNMT1-chr1 breakpoint is in a splice-silent desert

The chr1:31,048,832 breakpoint (near LAPTM5) has **no detectable splice site usage within 10kb** and only 5 sites on the - strand at 25kb distance.

| Window | Active splice sites | Strand | Max usage | Mean usage |
|--------|-------------------|--------|-----------|------------|
| 1kb | 0 | — | — | — |
| 5kb | 0 | — | — | — |
| 25kb | 5 (- strand only) | - only | 0.977 (brain) | 0.90-0.97 |

**Splice junctions:** Only 10,399 junction rows returned (vs 50,000 for other breakpoints), with weak signal (max scores 1.2-4.6, sum 12-40). This confirms the breakpoint sits in a transcriptionally quiet intergenic/intronic region.

**Standard splice sites:** 0 donors, 0 acceptors within 10kb.

**Variant splice effect:** Effectively zero (max 0.000000) — mutations at this position have no impact on splicing.

### 4. DNMT1-chr19 breakpoint is in the middle of a heavily spliced gene body

The chr19:10,160,241 breakpoint sits directly within the DNMT1 gene body, which is densely packed with splice sites on the - strand (DNMT1 is a - strand gene).

| Window | Active splice sites | Strand | Max usage | Mean usage |
|--------|-------------------|--------|-----------|------------|
| 1kb | 8 per tissue track | - only | 0.981 (brain) | 0.90-0.97 |
| 5kb | 16 per tissue track | - only | 0.981 | 0.88-0.97 |
| 25kb | 76 per tissue track | - only | 0.981 | 0.88-0.95 |

**Key positions within 5kb:**
- **chr19:10,159,657 (bp-584):** Usage 0.93-0.98 — splice site immediately upstream
- **chr19:10,160,062 (bp-179):** Usage 0.92-0.96 — splice site just 179bp from breakpoint
- **chr19:10,159,841 (bp-400):** Usage 0.92-0.96
- **chr19:10,162,747 (bp+2,506):** Usage 0.92-0.97 — splice site downstream
- **chr19:10,156,508 (bp-3,733):** Usage 0.92-0.97

The splice site at bp-179 is particularly notable — the translocation breaks the gene only 179bp from an active splice site, which could disrupt exon definition in the rearranged chromosome.

**Splice junctions:** Strong signal (max scores 5.9-16.4, sum 144-382). Spleen shows highest junction activity (max 16.4), followed by transverse colon (max 15.1) and lung (max 14.7). The junction density is comparable to ASPSCR1, confirming this is an actively spliced gene body.

**Standard splice sites:** 3 donors + 4 acceptors within 500bp; 4 donors + 4 acceptors within 2kb; 16 donors + 16 acceptors within 10kb.

### 5. Variant effects on splicing are negligible at all breakpoints

Single-nucleotide substitutions at each breakpoint position were scored for their impact on splice site usage:

| Breakpoint | Max variant splice effect |
|-----------|--------------------------|
| ASPSCR1 | 0.000047 |
| TFE3 | 0.000002 |
| DNMT1-chr1 | 0.000000 |
| DNMT1-chr19 | 0.000031 |

All effects are essentially zero. This means that point mutations at the breakpoint positions have no measurable impact on splice site usage in the surrounding region. The splicing machinery is robust to single-nucleotide changes at these positions — it takes the full translocation (which relocates entire genomic segments) to alter splicing, not subtle point mutations.

---

## Biological Significance

### The four breakpoints represent three distinct splicing environments

1. **ASPSCR1 (dense + strand splicing):** The breakpoint sits in the middle of a well-spliced gene body with 4 active splice sites within 1kb. The exon 10 splice site at bp+56 has near-perfect usage (0.93-0.98) across all tissues. This is the last exon included in the fusion transcript.

2. **TFE3 (sparse - strand splicing with 876bp gap):** The breakpoint is 876bp from the nearest splice site. This 876bp gap explains why the fusion junction analysis found a clean "intron-like" read-through region at the fusion junction — there is no splice site to catch within that gap, so the fusion transcript must splice to the first TFE3 exon at position bp-876.

3. **DNMT1-chr1 (splice desert):** The partner breakpoint is in a transcriptionally quiet region with no splice activity for 10kb in either direction. This means the translocation does not disrupt any active splicing at the chr1 side — the damage is exclusively to DNMT1 on chr19.

4. **DNMT1-chr19 (dense - strand splicing):** The breakpoint sits in one of the most densely spliced regions analyzed, with 8 active splice sites within 1kb and a splice site just 179bp away. Breaking DNMT1 here severs the gene in the middle of its actively spliced exon structure.

### Neoantigen prediction: Low likelihood from splice aberrations

The original motivation for this analysis was neoantigen prediction — whether aberrant splice products at the breakpoints could generate novel peptide sequences targetable by the immune system.

**The answer is: unlikely from splicing alone.** The data shows:

- **No cryptic splice sites** are activated at any breakpoint (confirmed by the fusion junction analysis)
- **Variant effects on splicing are zero** — the breakpoints don't create new splice donors/acceptors
- **The fusion produces a single clean transcript** (ASPSCR1 exon → 876bp intron → first TFE3 exon)
- **The DNMT1 breakpoint disrupts splicing by severing the gene**, not by creating aberrant splice products

However, the **fusion junction peptide itself** (the amino acids encoded where ASPSCR1 reads into TFE3) remains a potential neoantigen. This would need to be assessed by translating the fusion transcript sequence rather than by splice analysis.

### Connection to DNMT1 function

The finding that the DNMT1-chr19 breakpoint sits 179bp from an active splice site, within a region containing 76 splice sites in 25kb, explains the severity of the DNMT1 disruption. DNMT1 is a large, multi-exon gene (the dense splicing reflects its complex exon structure). Breaking the gene here doesn't just interrupt one exon — it severs the gene in the middle of its most actively spliced region, guaranteeing complete loss of function from the affected allele.

The splice-silent nature of the chr1 partner site confirms this is a one-sided disruption: DNMT1 is destroyed, but nothing is gained from the chr1 side in terms of novel splice products.

---

## Summary Table

| Breakpoint | Splice sites (1kb) | Splice sites (25kb) | Strand | Junction max score | Variant effect | Character |
|-----------|-------------------|--------------------|---------|--------------------|----------------|-----------|
| ASPSCR1 | 4 | 65 (+), 9 (-) | + dominant | 60.9 | 0.000047 | Dense, active gene body |
| TFE3 | 1 | 21 (+), 19 (-) | - dominant | 12.7 | 0.000002 | Sparse, 876bp gap to breakpoint |
| DNMT1-chr1 | 0 | 5 (-) | - only (distant) | 4.6 | 0.000000 | Splice desert |
| DNMT1-chr19 | 8 | 76 (-) | - dominant | 16.4 | 0.000031 | Dense, active gene body |

---

## Images

All images saved in `/Users/lbacaj/genomics/splice_junctions/`:

| File | Description |
|------|-------------|
| `ASPSCR1_splice_usage.png` | Splice site usage across 20 tracks, 50kb window, breakpoint marked |
| `ASPSCR1_splice_junctions.png` | Splice junction scores across 10 tracks, 50kb window |
| `TFE3_splice_usage.png` | Splice site usage, 50kb window — note - strand dominance |
| `TFE3_splice_junctions.png` | Splice junction scores, 50kb window |
| `DNMT1_chr1_splice_usage.png` | Splice site usage — note the silence near the breakpoint |
| `DNMT1_chr19_splice_usage.png` | Splice site usage — note the dense - strand activity |
| `DNMT1_chr19_splice_junctions.png` | Splice junction scores, 50kb window |

**Note:** The DNMT1-chr1 splice junction visualization could not be generated (dimension mismatch due to sparse junction data in the region), but the numerical data was captured. The AlphaGenome built-in context plots (TranscriptAnnotation + Tracks) encountered a `fig_height` parameter incompatibility in this version, but all quantitative data was collected successfully.

---

## Connection to Prior Analyses

1. **Confirms fusion junction findings:** The fusion junction analysis found the first TFE3 splice site at junction+875. This analysis independently confirms that the nearest TFE3 splice site is at bp-876 (chrX:49,043,110), validating the 876bp intron-like region at the fusion junction.

2. **Explains the "clean transcript" finding:** The fusion junction analysis showed no cryptic splice sites at the junction. This analysis explains why — the ASPSCR1 side has its last exon splice site at bp+56, and the TFE3 side has its first at bp-876, with an 876bp gap containing no splice-competent sequences.

3. **Validates the "quiet genome" model:** The negligible variant effects on splicing (max 0.000047) reinforce that this tumor's genomic drivers operate through large structural rearrangements, not through subtle sequence-level disruption. The splicing machinery is unperturbed at the sequence level — it's the chromosomal architecture that's been redesigned.

4. **DNMT1 disruption mechanism clarified:** The contact map analysis showed the DNMT1-chr1 breakpoint at a TAD boundary near LAPTM5. This analysis adds that the chr1 side is a splice desert, confirming the breakpoint is in intergenic space. All the functional damage is to DNMT1 on chr19, where the breakpoint cleaves through a dense splice site cluster.

---

*Analysis performed using AlphaGenome v0.6.1 (Google DeepMind). Splice site usage and junction predictions across 5 UBERON tissue ontology terms. Variant scoring via CenterMaskScorer (width=501, DIFF_MEAN). All raw data saved to splice_junctions/splice_junction_results.json.*
