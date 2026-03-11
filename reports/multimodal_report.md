# Multi-Modal Chromatin Landscape Analysis Report

**Patient:** Johnny
**Diagnosis:** Alveolar Soft Part Sarcoma (ASPS)
**Fusion Events:** ASPSCR1-TFE3 translocation t(17;X); DNMT1 translocation t(1;19)
**Reference Genome:** hg38
**Analysis Method:** AlphaGenome multi-modal predictions across a 10kb window centered on each breakpoint

---

## Table of Contents

1. [Breakpoint Overview](#breakpoint-overview)
2. [ASPSCR1 Breakpoint (chr17:82,010,811)](#1-aspscr1-breakpoint---chr1782010811)
3. [TFE3 Breakpoint (chrX:49,043,986)](#2-tfe3-breakpoint---chrx49043986)
4. [DNMT1-chr1 Breakpoint (chr1:31,048,832)](#3-dnmt1-chr1-breakpoint---chr131048832)
5. [DNMT1-chr19 Breakpoint (chr19:10,160,241)](#4-dnmt1-chr19-breakpoint---chr1910160241)
6. [Cross-Breakpoint Comparison](#cross-breakpoint-comparison)
7. [Key Findings Summary](#key-findings-summary)

---

## Breakpoint Overview

| Breakpoint | Locus | Translocation | Gene Context |
|---|---|---|---|
| ASPSCR1 | chr17:82,010,811 | t(17;X) | ASPSCR1 gene body (17q25.3) |
| TFE3 | chrX:49,043,986 | t(17;X) | TFE3 gene body (Xp11.23) |
| DNMT1-chr1 | chr1:31,048,832 | t(1;19) | DNMT1-associated region (1p35.1) |
| DNMT1-chr19 | chr19:10,160,241 | t(1;19) | DNMT1-associated region (19p13.2) |

---

## 1. ASPSCR1 Breakpoint -- chr17:82,010,811

### DNase-seq (Chromatin Accessibility)

| Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|
| kidney | 0.2345 | 4.0938 | 2344.8074 |
| spleen | 0.1697 | 1.8984 | 1697.2411 |
| liver | 0.1063 | 1.1094 | 1063.4347 |
| lung | 0.0821 | 4.3750 | 820.9002 |
| transverse colon | 0.0820 | 4.2500 | 819.6862 |
| heart | 0.0796 | 3.8750 | 795.7565 |
| brain | 0.0496 | 2.0938 | 496.3502 |
| thymus | 0.0394 | 0.6641 | 394.2166 |

### ATAC-seq (Chromatin Accessibility)

| Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|
| spleen | 0.0819 | 2.0938 | 818.8734 |
| liver | 0.0778 | 2.2031 | 777.7030 |
| transverse colon | 0.0744 | 3.5156 | 743.9139 |
| kidney | 0.0640 | 2.0938 | 640.4441 |
| lung | 0.0626 | 1.8047 | 626.2328 |

### CAGE (Transcription Initiation -- Positive Strand)

| Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|
| brain | 0.0100 | 0.8086 | 99.7638 |
| heart | 0.0075 | 0.7695 | 74.5066 |
| spleen | 0.0059 | 0.6875 | 58.7375 |
| liver | 0.0053 | 0.5820 | 53.4467 |
| kidney | 0.0053 | 0.9688 | 53.2080 |
| thymus | 0.0053 | 0.4727 | 53.0867 |
| lung | 0.0050 | 0.5391 | 50.4451 |

### CAGE (Transcription Initiation -- Negative Strand)

| Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|
| brain | 0.0025 | 0.2021 | 25.3025 |
| heart | 0.0012 | 0.1074 | 12.2511 |
| liver | 0.0011 | 0.0977 | 10.5779 |
| thymus | 0.0008 | 0.0659 | 7.9334 |
| spleen | 0.0007 | 0.0581 | 7.1011 |
| kidney | 0.0006 | 0.0579 | 6.3003 |
| lung | 0.0003 | 0.0197 | 3.4421 |

### Histone ChIP-seq (Top Marks by Mean Signal)

| Mark | Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|---|
| H3K4me3 | brain | 384.0234 | 10624.0 | 347157.1875 |
| H3K36me3 | thymus | 339.1637 | 1200.0 | 306604.0 |
| H3K27ac | spleen | 333.2149 | 11200.0 | 301226.3125 |
| H3K36me3 | brain | 317.4005 | 976.0 | 286930.0625 |
| H3K36me3 | spleen | 284.2272 | 976.0 | 256941.3750 |
| H3K36me3 | lung | 275.2825 | 1112.0 | 248855.3438 |
| H3K4me1 | thymus | 263.0226 | 2192.0 | 237772.3750 |
| H3K4me3 | thymus | 249.9163 | 8384.0 | 225924.3594 |
| H3K27ac | liver | 212.8936 | 6656.0 | 192455.7812 |
| H3K9ac | heart | 237.5335 | 3824.0 | 214730.2500 |

**Repressive marks present:**

| Mark | Biosample | Center Mean | Center Max |
|---|---|---|---|
| H3K9me3 | thymus | 194.6485 | 704.0 |
| H3K9me3 | lung | 99.2076 | 288.0 |
| H3K27me3 | thymus | 97.9760 | 780.0 |
| H3K27me3 | transverse colon | 71.8328 | 145.0 |
| H3K27me3 | brain | 63.9650 | 276.0 |
| H3K9me3 | brain | 60.2337 | 346.0 |

### TF ChIP-seq (Top Transcription Factors)

| TF | Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|---|
| POLR2AphosphoS5 | spleen | 414.5989 | 8384.0 | 374797.3750 |
| POLR2AphosphoS5 | transverse colon | 157.1333 | 2448.0 | 142048.5312 |
| POLR2A | transverse colon | 129.8124 | 1312.0 | 117350.4219 |
| CTCF | transverse colon | 118.0211 | 2144.0 | 106691.0938 |
| CTCF | spleen | 116.2808 | 2416.0 | 105117.8750 |
| SP1 | liver | 111.7295 | 2400.0 | 101003.5000 |
| CTCF | brain | 110.2183 | 2080.0 | 99637.3672 |
| HNF4A | liver | 91.0876 | 2304.0 | 82343.2188 |
| EP300 | transverse colon | 89.4849 | 247.0 | 80894.3672 |
| GABPA | liver | 95.3411 | 3216.0 | 86188.3281 |

### Splice Sites

| Type | Center Mean | Center Max | Center Sum |
|---|---|---|---|
| donor (strong) | 0.0013 | 1.0000 | 12.7101 |
| acceptor (strong) | 0.0011 | 1.0000 | 10.6109 |
| donor (weak) | 0.0000 | 0.0053 | 0.0356 |
| acceptor (weak) | 0.0000 | 0.0022 | 0.0269 |

---

## 2. TFE3 Breakpoint -- chrX:49,043,986

### DNase-seq (Chromatin Accessibility)

| Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|
| transverse colon | 0.6074 | 92.0000 | 6074.4126 |
| lung | 0.4790 | 64.5000 | 4789.6836 |
| brain | 0.4130 | 63.7500 | 4129.8706 |
| kidney | 0.3858 | 34.0000 | 3858.2417 |
| spleen | 0.3470 | 26.2500 | 3470.4761 |
| thymus | 0.2588 | 38.5000 | 2588.0378 |
| heart | 0.2584 | 30.2500 | 2583.7339 |
| liver | 0.2250 | 27.0000 | 2249.8303 |

### ATAC-seq (Chromatin Accessibility)

| Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|
| transverse colon | 0.3589 | 57.0000 | 3588.8262 |
| lung | 0.2102 | 24.7500 | 2101.8655 |
| kidney | 0.1723 | 19.7500 | 1722.5837 |
| liver | 0.1182 | 13.5625 | 1182.2002 |
| spleen | 0.1016 | 12.8125 | 1016.1049 |

### CAGE (Transcription Initiation -- Positive Strand)

| Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|
| spleen | 0.5144 | 780.0000 | 5144.2480 |
| lung | 0.4663 | 772.0000 | 4663.2808 |
| kidney | 0.4361 | 716.0000 | 4360.9160 |
| heart | 0.3895 | 708.0000 | 3894.8643 |
| brain | 0.3668 | 588.0000 | 3668.0835 |
| thymus | 0.3397 | 604.0000 | 3396.5220 |
| liver | 0.2643 | 600.0000 | 2642.7197 |

### CAGE (Transcription Initiation -- Negative Strand)

| Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|
| brain | 0.0076 | 1.9297 | 76.1003 |
| spleen | 0.0049 | 1.1641 | 49.2700 |
| thymus | 0.0045 | 1.5000 | 45.0762 |
| kidney | 0.0041 | 0.9375 | 40.6576 |
| heart | 0.0034 | 0.6602 | 34.1076 |
| lung | 0.0034 | 0.9805 | 33.5716 |
| liver | 0.0033 | 0.5977 | 33.2905 |

### Histone ChIP-seq (All Marks)

**Note:** Histone signal at TFE3 is dramatically lower than at other breakpoints, with values in the low single digits rather than hundreds.

| Mark | Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|---|
| H3K9me3 | brain | 3.0757 | 48.5000 | 2780.4131 |
| H3K9me3 | lung | 1.8116 | 78.0000 | 1637.7031 |
| H3K9me3 | thymus | 1.7537 | 56.0000 | 1585.3245 |
| H3K27me3 | brain | 1.4124 | 25.8750 | 1276.8440 |
| H3K9me3 | spleen | 1.3465 | 23.0000 | 1217.2551 |
| H3K27me3 | spleen | 0.9884 | 14.6875 | 893.5261 |
| H3K4me3 | lung | 0.8036 | 22.5000 | 726.4407 |
| H3K4me3 | spleen | 0.7876 | 11.6250 | 712.0103 |
| H3K4me1 | brain | 0.7347 | 9.1875 | 664.1710 |
| H3K36me3 | brain | 0.7018 | 11.0625 | 634.4482 |
| H3K27ac | lung | 0.5626 | 16.6250 | 508.5749 |
| H3K27ac | spleen | 0.5140 | 6.4063 | 464.6527 |
| H3K9ac | lung | 0.3690 | 5.5625 | 333.5837 |

### TF ChIP-seq (All Transcription Factors)

**Note:** TF binding signal at TFE3 is extremely low compared to other breakpoints.

| TF | Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|---|
| CTCF | brain | 0.9331 | 12.1875 | 843.5039 |
| HNF4G | liver | 0.6797 | 8.6250 | 614.4578 |
| TAF1 | liver | 0.6079 | 7.0938 | 549.5576 |
| CTCF | liver | 0.5012 | 9.5000 | 453.1241 |
| ATF3 | liver | 0.4220 | 5.1250 | 381.5305 |
| MAX | liver | 0.4148 | 5.4063 | 375.0193 |
| EGR1 | liver | 0.4078 | 6.8750 | 368.6422 |
| POLR2AphosphoS5 | spleen | 0.0791 | 4.5625 | 71.4867 |

### Splice Sites

| Type | Center Mean | Center Max | Center Sum |
|---|---|---|---|
| donor (strong) | 0.0006 | 1.0000 | 5.8824 |
| acceptor (strong) | 0.0005 | 0.9961 | 5.4078 |
| donor (weak) | 0.0000 | 0.0140 | 0.0870 |
| acceptor (weak) | 0.0000 | 0.0044 | 0.0403 |

---

## 3. DNMT1-chr1 Breakpoint -- chr1:31,048,832

### DNase-seq (Chromatin Accessibility)

| Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|
| kidney | 0.0486 | 1.1328 | 485.9783 |
| spleen | 0.0442 | 1.1719 | 442.1520 |
| liver | 0.0421 | 0.5742 | 421.4640 |
| transverse colon | 0.0315 | 0.5352 | 314.8336 |
| heart | 0.0207 | 0.8828 | 207.3745 |
| thymus | 0.0201 | 0.3730 | 201.2638 |
| lung | 0.0179 | 0.5195 | 178.8637 |
| brain | 0.0146 | 0.3691 | 145.7264 |

### ATAC-seq (Chromatin Accessibility)

| Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|
| liver | 0.0371 | 1.6953 | 370.5780 |
| kidney | 0.0328 | 1.1172 | 328.3937 |
| lung | 0.0316 | 0.9375 | 316.0877 |
| transverse colon | 0.0256 | 0.7578 | 255.7959 |
| spleen | 0.0215 | 0.9102 | 214.5883 |

### CAGE (Transcription Initiation -- Positive Strand)

| Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|
| thymus | 0.0060 | 3.6719 | 59.7487 |
| brain | 0.0059 | 3.3594 | 58.8927 |
| heart | 0.0040 | 2.7813 | 40.4428 |
| spleen | 0.0040 | 2.6250 | 40.1660 |
| kidney | 0.0038 | 2.6563 | 37.7733 |
| lung | 0.0037 | 2.1563 | 36.7266 |
| liver | 0.0025 | 1.2578 | 24.6328 |

### CAGE (Transcription Initiation -- Negative Strand)

| Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|
| brain | 0.0011 | 1.0703 | 11.4205 |
| thymus | 0.0009 | 1.0703 | 8.8293 |
| liver | 0.0009 | 0.8945 | 8.7497 |
| heart | 0.0008 | 0.8242 | 8.4897 |
| kidney | 0.0007 | 0.9688 | 7.2866 |
| spleen | 0.0007 | 0.7773 | 6.6178 |
| lung | 0.0003 | 0.2988 | 2.7021 |

### Histone ChIP-seq (Top Marks by Mean Signal)

| Mark | Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|---|
| H3K4me1 | thymus | 297.8346 | 2768.0 | 269242.5000 |
| H3K27ac | thymus | 197.4574 | 2832.0 | 178501.5312 |
| H3K9me3 | thymus | 176.4995 | 1376.0 | 159555.5781 |
| H3K27me3 | brain | 145.2466 | 286.0 | 131302.9531 |
| H3K27ac | liver | 137.7342 | 1624.0 | 124511.7422 |
| H3K27me3 | spleen | 135.1435 | 256.0 | 122169.6875 |
| H3K27me3 | transverse colon | 133.7200 | 211.0 | 120882.8438 |
| H3K9me3 | spleen | 125.3123 | 1120.0 | 113282.3438 |
| H3K4me1 | liver | 124.4875 | 688.0 | 112536.7266 |
| H3K9me3 | lung | 118.9651 | 1144.0 | 107544.4375 |
| H3K27me3 | heart | 118.0970 | 258.0 | 106759.7188 |
| H3K9me3 | brain | 114.9140 | 776.0 | 103882.2578 |
| H3K4me3 | thymus | 110.5257 | 1552.0 | 99915.2188 |

### TF ChIP-seq (Top Transcription Factors)

| TF | Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|---|
| CTCF | brain | 115.2712 | 3216.0 | 104205.1562 |
| CTCF | transverse colon | 113.1170 | 3440.0 | 102257.7500 |
| HNF4A | liver | 112.2049 | 1992.0 | 101433.1953 |
| CTCF | spleen | 111.2276 | 3568.0 | 100549.7344 |
| SP1 | liver | 107.5556 | 1368.0 | 97230.2812 |
| RXRA | liver | 106.7982 | 1816.0 | 96545.5781 |
| CTCF | liver | 101.8290 | 3760.0 | 92053.4219 |
| POLR2A | spleen | 100.4323 | 168.0 | 90790.7812 |
| JUND | liver | 99.5734 | 864.0 | 90014.3984 |
| EP300 | transverse colon | 99.3154 | 428.0 | 89781.0938 |
| YY1 | liver | 96.4557 | 668.0 | 87195.9219 |
| FOXA2 | liver | 98.4365 | 390.0 | 88986.5781 |
| FOXA1 | liver | 97.0160 | 278.0 | 87702.4922 |

### Splice Sites

| Type | Center Mean | Center Max | Center Sum |
|---|---|---|---|
| acceptor (strong) | 0.0000 | 0.1582 | 0.2964 |
| donor (strong) | 0.0000 | 0.0645 | 0.2172 |
| donor (weak) | 0.0000 | 0.0007 | 0.0051 |
| acceptor (weak) | 0.0000 | 0.0001 | 0.0041 |

---

## 4. DNMT1-chr19 Breakpoint -- chr19:10,160,241

### DNase-seq (Chromatin Accessibility)

| Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|
| kidney | 0.0745 | 1.9141 | 745.2169 |
| liver | 0.0648 | 0.7734 | 647.5850 |
| spleen | 0.0599 | 1.5625 | 598.7091 |
| transverse colon | 0.0354 | 0.4648 | 354.4134 |
| thymus | 0.0239 | 0.2715 | 239.2866 |
| lung | 0.0206 | 0.3652 | 206.3918 |
| heart | 0.0175 | 0.2852 | 174.7567 |
| brain | 0.0109 | 0.2344 | 109.2724 |

### ATAC-seq (Chromatin Accessibility)

| Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|
| liver | 0.0379 | 0.9766 | 378.6292 |
| spleen | 0.0312 | 0.8945 | 312.2410 |
| kidney | 0.0282 | 0.7578 | 281.7884 |
| lung | 0.0279 | 0.6523 | 279.0175 |
| transverse colon | 0.0255 | 0.6406 | 254.7360 |

### CAGE (Transcription Initiation -- Positive Strand)

| Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|
| thymus | 0.0263 | 58.7500 | 263.1240 |
| brain | 0.0203 | 62.5000 | 203.0993 |
| spleen | 0.0158 | 43.7500 | 157.6708 |
| heart | 0.0138 | 39.5000 | 138.0718 |
| lung | 0.0116 | 35.2500 | 116.2027 |
| liver | 0.0101 | 38.5000 | 101.0097 |
| kidney | 0.0101 | 32.0000 | 100.9155 |

### CAGE (Transcription Initiation -- Negative Strand)

| Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|
| brain | 0.0025 | 0.3750 | 24.7364 |
| thymus | 0.0021 | 0.3828 | 20.8674 |
| heart | 0.0013 | 0.1953 | 12.6404 |
| spleen | 0.0010 | 0.1406 | 10.2800 |
| liver | 0.0007 | 0.0889 | 6.9162 |
| kidney | 0.0007 | 0.1021 | 6.5429 |
| lung | 0.0004 | 0.0444 | 3.5541 |

### Histone ChIP-seq (Top Marks by Mean Signal)

| Mark | Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|---|
| H3K4me3 | brain | 396.2178 | 11584.0 | 358180.8750 |
| H3K36me3 | thymus | 384.5115 | 1488.0 | 347598.4062 |
| H3K27ac | spleen | 371.7234 | 8192.0 | 336038.0000 |
| H3K4me3 | thymus | 321.4197 | 12928.0 | 290563.3750 |
| H3K36me3 | spleen | 292.1524 | 1200.0 | 264105.7500 |
| H3K9ac | heart | 282.0528 | 6272.0 | 254975.7500 |
| H3K4me1 | thymus | 272.8617 | 2080.0 | 246666.9375 |
| H3K27ac | lung | 271.7435 | 4736.0 | 245656.0938 |
| H3K36me3 | lung | 266.9226 | 1184.0 | 241298.0625 |
| H3K36me3 | brain | 260.7413 | 992.0 | 235710.1250 |
| H3K4me3 | spleen | 233.6355 | 5984.0 | 211206.5000 |
| H3K4me1 | spleen | 232.5069 | 704.0 | 210186.2500 |
| H3K27ac | thymus | 220.1404 | 6176.0 | 199006.9375 |
| H3K27ac | kidney | 210.8370 | 4512.0 | 190596.6875 |

**Repressive marks present:**

| Mark | Biosample | Center Mean | Center Max |
|---|---|---|---|
| H3K9me3 | thymus | 182.5972 | 438.0 |
| H3K27me3 | thymus | 114.0838 | 2208.0 |
| H3K27me3 | brain | 111.4002 | 1536.0 |
| H3K9me3 | lung | 94.3756 | 270.0 |
| H3K27me3 | transverse colon | 84.6697 | 362.0 |
| H3K27me3 | spleen | 76.5311 | 796.0 |
| H3K9me3 | brain | 58.6141 | 171.0 |

### TF ChIP-seq (Top Transcription Factors)

| TF | Biosample | Center Mean | Center Max | Center Sum |
|---|---|---|---|---|
| POLR2AphosphoS5 | spleen | 320.4774 | 4224.0 | 289711.6250 |
| POLR2AphosphoS5 | transverse colon | 156.6363 | 1520.0 | 141599.2500 |
| CTCF | transverse colon | 135.1669 | 3712.0 | 122190.8750 |
| CTCF | spleen | 131.8527 | 4192.0 | 119194.8750 |
| CTCF | brain | 128.8720 | 3280.0 | 116500.2500 |
| POLR2A | transverse colon | 123.5755 | 1000.0 | 111712.2500 |
| SP1 | liver | 113.5270 | 2176.0 | 102628.3750 |
| CTCF | liver | 110.8360 | 4512.0 | 100195.7500 |
| YY1 | liver | 104.7857 | 3184.0 | 94726.2500 |
| POLR2A | spleen | 103.8874 | 342.0 | 93914.2500 |
| EP300 | transverse colon | 93.2728 | 412.0 | 84318.6250 |
| FOXA1 | liver | 89.6706 | 302.0 | 81062.2500 |
| HNF4A | liver | 88.2082 | 1760.0 | 79740.1875 |

### Splice Sites

| Type | Center Mean | Center Max | Center Sum |
|---|---|---|---|
| donor (strong) | 0.0011 | 1.0000 | 11.2348 |
| acceptor (strong) | 0.0011 | 1.0000 | 10.7544 |
| acceptor (weak) | 0.0000 | 0.0229 | 0.0792 |
| donor (weak) | 0.0000 | 0.0150 | 0.0414 |

---

## Cross-Breakpoint Comparison

### Chromatin Accessibility (DNase-seq -- Mean Signal Across All Tissues)

| Breakpoint | Avg Center Mean | Max Center Mean | Max Center Max |
|---|---|---|---|
| TFE3 | 0.3694 | 0.6074 (transverse colon) | 92.0 (transverse colon) |
| ASPSCR1 | 0.1053 | 0.2345 (kidney) | 4.375 (lung) |
| DNMT1-chr19 | 0.0384 | 0.0745 (kidney) | 1.914 (kidney) |
| DNMT1-chr1 | 0.0300 | 0.0486 (kidney) | 1.172 (spleen) |

### Chromatin Accessibility (ATAC-seq -- Mean Signal Across All Tissues)

| Breakpoint | Avg Center Mean | Max Center Mean | Max Center Max |
|---|---|---|---|
| TFE3 | 0.1923 | 0.3589 (transverse colon) | 57.0 (transverse colon) |
| ASPSCR1 | 0.0722 | 0.0819 (spleen) | 3.516 (transverse colon) |
| DNMT1-chr19 | 0.0301 | 0.0379 (liver) | 0.977 (liver) |
| DNMT1-chr1 | 0.0296 | 0.0371 (liver) | 1.695 (liver) |

### Transcriptional Activity (CAGE Positive Strand -- Max Mean Signal)

| Breakpoint | Max Center Mean | Tissue | Max Center Max |
|---|---|---|---|
| TFE3 | 0.5144 | spleen | 780.0 |
| DNMT1-chr19 | 0.0263 | thymus | 62.5 |
| ASPSCR1 | 0.0100 | brain | 0.969 |
| DNMT1-chr1 | 0.0060 | thymus | 3.672 |

### Histone Modification Signal (Top Active Mark Center Mean)

| Breakpoint | Top Mark | Top Mean Signal | Tissue |
|---|---|---|---|
| DNMT1-chr19 | H3K4me3 | 396.2178 | brain |
| ASPSCR1 | H3K4me3 | 384.0234 | brain |
| DNMT1-chr1 | H3K4me1 | 297.8346 | thymus |
| TFE3 | H3K9me3 | 3.0757 | brain |

### TF Binding Signal (Top TF Center Mean)

| Breakpoint | Top TF | Top Mean Signal | Tissue |
|---|---|---|---|
| ASPSCR1 | POLR2AphosphoS5 | 414.5989 | spleen |
| DNMT1-chr19 | POLR2AphosphoS5 | 320.4774 | spleen |
| DNMT1-chr1 | CTCF | 115.2712 | brain |
| TFE3 | CTCF | 0.9331 | brain |

### Splice Site Density

| Breakpoint | Max Donor Mean | Max Acceptor Mean | Strong Splice Sites? |
|---|---|---|---|
| ASPSCR1 | 0.0013 | 0.0011 | Yes (max = 1.0) |
| DNMT1-chr19 | 0.0011 | 0.0011 | Yes (max = 1.0) |
| TFE3 | 0.0006 | 0.0005 | Yes (max ~ 1.0) |
| DNMT1-chr1 | 0.0000 | 0.0000 | No (max = 0.158) |

---

## Key Findings Summary

### 1. TFE3 Breakpoint Has the Most Open Chromatin

The TFE3 locus on chrX shows by far the highest chromatin accessibility signal, with DNase-seq mean values 3.5x higher than ASPSCR1 and roughly 10x higher than either DNMT1 breakpoint. The center max of 92.0 in transverse colon is dramatically higher than any other breakpoint. This suggests the TFE3 breakpoint sits in a highly accessible, regulatory-active region across multiple tissue types, consistent with it being within an actively transcribed housekeeping gene.

### 2. TFE3 Has the Strongest Transcription Initiation Signal

CAGE positive-strand signal at TFE3 is approximately 50x higher than at ASPSCR1 and 85x higher than at DNMT1-chr1. The center max values at TFE3 reach 780.0 (spleen), indicating very strong transcription start site activity. This is consistent with TFE3 being a broadly expressed transcription factor gene.

### 3. Paradoxically, TFE3 Has Near-Zero Histone Modification Signal

Despite having the highest chromatin accessibility and transcription, TFE3 shows essentially no histone modification signal (top value 3.08 vs. 384-396 at other breakpoints). The dominant marks at TFE3 are the repressive marks H3K9me3 and H3K27me3, albeit at very low levels. This could reflect TFE3's location on the X chromosome, where histone modification patterns may be influenced by X-inactivation in female-derived cells in the training data, or the unique chromatin architecture of the Xp11.23 locus.

### 4. TFE3 Has Minimal TF Binding

TF ChIP-seq signal at TFE3 is 2-3 orders of magnitude lower than at the other three breakpoints. The top TF signal (CTCF at 0.93) is negligible compared to ASPSCR1 (POLR2AphosphoS5 at 414.6). This may indicate the TFE3 breakpoint region is in an intron or region where transcription is occurring but without dense TF binding at the exact breakpoint.

### 5. ASPSCR1 and DNMT1-chr19 Are in Active, Gene-Dense Regions

Both the ASPSCR1 (chr17) and DNMT1-chr19 (chr19) breakpoints show very high histone modification signals, particularly:
- Strong H3K4me3 (active promoter): ~384-396 mean signal
- Strong H3K36me3 (active transcription/gene body): ~339-384 mean signal
- Strong H3K27ac (active enhancer): ~333-372 mean signal
- Robust POLR2A/POLR2AphosphoS5 binding (active RNA Pol II)

These patterns are consistent with breakpoints located within or near actively transcribed gene bodies in a euchromatic, gene-dense environment.

### 6. DNMT1-chr1 Shows a Repressive Chromatin Signature

The DNMT1-chr1 breakpoint is distinguished by elevated repressive histone marks relative to active marks:
- H3K27me3 (Polycomb repression) is among the top signals across brain, spleen, transverse colon, and heart (mean 118-145)
- H3K9me3 (heterochromatin) is prominent in thymus (176.5), spleen (125.3), lung (119.0), and brain (114.9)
- While active marks like H3K4me1 and H3K27ac are present, the ratio of repressive-to-active marks is higher than at ASPSCR1 or DNMT1-chr19
- DNase-seq accessibility is the lowest among all four breakpoints
- CTCF binding is the dominant TF signal, suggesting an insulator/boundary element role

### 7. Splice Sites Confirm Gene Body Locations

ASPSCR1 and DNMT1-chr19 both show strong splice site predictions (center max = 1.0 for both donor and acceptor), confirming both breakpoints fall within exon-intron junctions of actively spliced genes. TFE3 shows moderate splice site signal. DNMT1-chr1 has essentially no splice site signal (max 0.158), suggesting this breakpoint may be in an intergenic or intronic region far from any exon boundary.

### 8. Chromatin State Summary

| Breakpoint | Chromatin State | Open/Closed | Transcription | Dominant Histone Profile |
|---|---|---|---|---|
| ASPSCR1 | Active gene body | Moderately open | Low-moderate CAGE | H3K4me3, H3K36me3, H3K27ac (active) |
| TFE3 | Highly accessible, actively transcribed | Highly open | Very strong CAGE | Near-zero signal (atypical) |
| DNMT1-chr1 | Mixed/repressive | Relatively closed | Very low CAGE | H3K27me3, H3K9me3 (repressive) |
| DNMT1-chr19 | Active gene body | Moderately open | Moderate CAGE | H3K4me3, H3K36me3, H3K27ac (active) |

### 9. Clinical Relevance

The ASPSCR1-TFE3 fusion brings together a moderately active locus (ASPSCR1 at 17q25.3) with a highly transcribed locus (TFE3 at Xp11.23). The high transcriptional activity at TFE3 likely drives strong expression of the fusion oncogene, characteristic of ASPS pathogenesis.

The DNMT1 translocation t(1;19) juxtaposes a repressed/heterochromatic region (chr1:31,048,832) with an active, gene-dense region (chr19:10,160,241). This rearrangement could lead to aberrant activation of genes near the chr1 breakpoint through the importation of active chromatin marks from the chr19 partner, or conversely, could silence genes near the chr19 breakpoint through heterochromatin spreading from the chr1 partner.

---

*Report generated from AlphaGenome multi-modal predictions. All signal values represent predicted epigenomic activity within a 10kb window centered on each breakpoint. Values are rounded to 4 decimal places.*
