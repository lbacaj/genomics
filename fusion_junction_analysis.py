"""Fusion Junction Sequence Modeling.

Constructs the actual chimeric DNA sequence from the ASPSCR1-TFE3
translocation and runs AlphaGenome predictions on:
1. The fusion sequence (chimeric der chromosome)
2. The normal ASPSCR1 locus (for comparison)
3. The normal TFE3 locus (for comparison)

This predicts what the fusion transcript actually looks like — its
expression, splicing, chromatin state — rather than inferring from
the breakpoints separately.

ASPSCR1 is on chr17 + strand.
TFE3 is on chrX - strand.

The oncogenic fusion (der(X)) joins:
  chr17 sequence up to breakpoint (reading + strand) →
  reverse complement of chrX from breakpoint downward
  (so TFE3 coding exons are read in the correct orientation)
"""

import os
import sys
sys.path = [p for p in sys.path if p not in ('', '.', os.getcwd())]

with open('/Users/lbacaj/genomics/.env') as f:
    for line in f:
        if '=' in line:
            k, v = line.strip().split('=', 1)
            os.environ[k] = v

import matplotlib
matplotlib.use('Agg')

from alphagenome.models import dna_client
from alphagenome.data import genome
from alphagenome.data import gene_annotation
from alphagenome.data import transcript as transcript_utils
from alphagenome.visualization import plot_components
import matplotlib.pyplot as plt
import numpy as np
import json
import urllib.request
import pandas as pd

print("Connecting to AlphaGenome API...")
dna_model = dna_client.create(os.environ['ALPHA_GENOME_API_KEY'])
print("Connected.\n")

# Load GTF
print("Loading gene annotations...")
gtf = pd.read_feather(
    'https://storage.googleapis.com/alphagenome/reference/gencode/'
    'hg38/gencode.v46.annotation.gtf.gz.feather'
)
gtf_transcripts = gene_annotation.filter_protein_coding(gtf)
gtf_transcripts = gene_annotation.filter_to_mane_select_transcript(gtf_transcripts)
transcript_extractor = transcript_utils.TranscriptExtractor(gtf_transcripts)
print("Done.\n")

OUTPUT_DIR = '/Users/lbacaj/genomics/fusion_analysis'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Breakpoint coordinates (hg38)
ASPSCR1_BP = 82010811   # chr17
TFE3_BP = 49043986      # chrX

# Use 500KB total sequence (250KB from each side)
HALF_LEN = dna_client.SEQUENCE_LENGTH_500KB // 2  # 262,144 bp


def fetch_sequence(chrom, start, end):
    """Fetch reference genome sequence from UCSC API."""
    # UCSC API has a limit, so fetch in chunks
    chunk_size = 100000
    seq = ''
    for chunk_start in range(start, end, chunk_size):
        chunk_end = min(chunk_start + chunk_size, end)
        url = (f'https://api.genome.ucsc.edu/getData/sequence'
               f'?genome=hg38&chrom={chrom}'
               f'&start={chunk_start}&end={chunk_end}')
        with urllib.request.urlopen(url) as resp:
            data = json.loads(resp.read())
            seq += data['dna']
        print(f"    Fetched {chrom}:{chunk_start:,}-{chunk_end:,} "
              f"({len(seq):,}bp total)")
    return seq.upper()


def reverse_complement(seq):
    """Reverse complement a DNA sequence."""
    comp = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'N': 'N'}
    return ''.join(comp.get(b, 'N') for b in reversed(seq))


# =============================================
# STEP 1: Fetch reference sequences
# =============================================
print("=" * 70)
print("STEP 1: Fetching reference sequences from UCSC (hg38)")
print("=" * 70)

# ASPSCR1 side: chr17, upstream of breakpoint
print(f"\n  Fetching ASPSCR1 side: chr17:{ASPSCR1_BP - HALF_LEN:,}-{ASPSCR1_BP:,}")
aspscr1_seq = fetch_sequence('chr17', ASPSCR1_BP - HALF_LEN, ASPSCR1_BP)
print(f"  ASPSCR1 sequence: {len(aspscr1_seq):,}bp")
print(f"  Last 20bp (at breakpoint): ...{aspscr1_seq[-20:]}")

# TFE3 side: chrX, from breakpoint going toward lower coordinates
# (because TFE3 is on - strand, we need sequence BELOW the breakpoint)
print(f"\n  Fetching TFE3 side: chrX:{TFE3_BP - HALF_LEN:,}-{TFE3_BP:,}")
tfe3_seq_raw = fetch_sequence('chrX', TFE3_BP - HALF_LEN, TFE3_BP)
print(f"  TFE3 raw sequence: {len(tfe3_seq_raw):,}bp")

# Reverse complement the TFE3 side so TFE3 coding exons read correctly
# on the derivative chromosome
tfe3_seq_rc = reverse_complement(tfe3_seq_raw)
print(f"  TFE3 reverse complement: {len(tfe3_seq_rc):,}bp")
print(f"  First 20bp after junction: {tfe3_seq_rc[:20]}...")

# =============================================
# STEP 2: Construct fusion sequence
# =============================================
print("\n" + "=" * 70)
print("STEP 2: Constructing chimeric fusion sequence")
print("=" * 70)

fusion_seq = aspscr1_seq + tfe3_seq_rc
print(f"  Fusion sequence length: {len(fusion_seq):,}bp")
print(f"  Junction at position: {len(aspscr1_seq):,} (center of sequence)")
print(f"  ASPSCR1 side: chr17:{ASPSCR1_BP - HALF_LEN:,}-{ASPSCR1_BP:,} (+ strand)")
print(f"  TFE3 side: chrX:{TFE3_BP - HALF_LEN:,}-{TFE3_BP:,} (rev comp)")
print(f"  Junction sequence: ...{aspscr1_seq[-10:]}|{tfe3_seq_rc[:10]}...")

# Also fetch normal reference sequences for comparison
print(f"\n  Fetching normal ASPSCR1 locus (full 500KB centered on breakpoint)...")
aspscr1_normal = fetch_sequence('chr17',
                                ASPSCR1_BP - HALF_LEN,
                                ASPSCR1_BP + HALF_LEN)
print(f"  Normal ASPSCR1: {len(aspscr1_normal):,}bp")

print(f"\n  Fetching normal TFE3 locus (full 500KB centered on breakpoint)...")
tfe3_normal = fetch_sequence('chrX',
                             TFE3_BP - HALF_LEN,
                             TFE3_BP + HALF_LEN)
print(f"  Normal TFE3: {len(tfe3_normal):,}bp")

# =============================================
# STEP 3: Run AlphaGenome predictions
# =============================================
print("\n" + "=" * 70)
print("STEP 3: Running AlphaGenome predictions")
print("=" * 70)

# Output types to predict
output_types = [
    dna_client.OutputType.RNA_SEQ,
    dna_client.OutputType.SPLICE_SITES,
    dna_client.OutputType.DNASE,
    dna_client.OutputType.CAGE,
]

# Tissues to predict
ontology_terms = [
    'UBERON:0002048',  # Lung
    'UBERON:0000955',  # Brain
    'UBERON:0002107',  # Liver
    'UBERON:0001157',  # Transverse colon
    'UBERON:0002106',  # Spleen
]

sequences = {
    'fusion': fusion_seq,
    'normal_ASPSCR1': aspscr1_normal,
    'normal_TFE3': tfe3_normal,
}

all_outputs = {}

for seq_name, seq in sequences.items():
    print(f"\n  --- Predicting: {seq_name} ({len(seq):,}bp) ---")

    try:
        # Splice sites don't need ontology terms, run separately
        print(f"    Running SPLICE_SITES...")
        splice_out = dna_model.predict_sequence(
            sequence=seq,
            requested_outputs=[dna_client.OutputType.SPLICE_SITES],
            ontology_terms=None,
        )
        all_outputs[f'{seq_name}_splice'] = splice_out
        print(f"    Splice sites shape: {splice_out.splice_sites.values.shape}")

        # RNA_SEQ, DNASE, CAGE with ontology terms
        for otype in [dna_client.OutputType.RNA_SEQ,
                      dna_client.OutputType.DNASE,
                      dna_client.OutputType.CAGE]:
            print(f"    Running {otype.name}...")
            out = dna_model.predict_sequence(
                sequence=seq,
                requested_outputs=[otype],
                ontology_terms=ontology_terms,
            )
            all_outputs[f'{seq_name}_{otype.name}'] = out
            attr = otype.name.lower()
            tdata = getattr(out, attr)
            print(f"    {otype.name} shape: {tdata.values.shape}, "
                  f"tracks: {len(tdata.metadata)}")

    except Exception as e:
        print(f"    ERROR: {e}")
        import traceback
        traceback.print_exc()

# =============================================
# STEP 4: Compare fusion vs normal at junction
# =============================================
print("\n" + "=" * 70)
print("STEP 4: Analyzing differences at the fusion junction")
print("=" * 70)

junction_pos = HALF_LEN  # center of fusion sequence
window = 25000  # 25kb each side of junction for analysis
center_slice = slice(junction_pos - window, junction_pos + window)

results = {}

# --- RNA-SEQ comparison ---
print("\n  RNA-SEQ at junction (50kb window):")
for seq_name in ['fusion', 'normal_ASPSCR1', 'normal_TFE3']:
    key = f'{seq_name}_RNA_SEQ'
    if key not in all_outputs:
        continue
    rna = all_outputs[key].rna_seq
    vals = rna.values[center_slice, :]
    meta = rna.metadata

    print(f"\n    {seq_name}:")
    for i, (_, row) in enumerate(meta.iterrows()):
        tissue = row.get('biosample_name', row.get('name', ''))
        strand = row.get('strand', '.')
        mean_val = float(np.mean(vals[:, i]))
        max_val = float(np.max(vals[:, i]))
        if mean_val > 0.01:
            print(f"      {tissue:40s} strand={strand}  "
                  f"mean={mean_val:.4f}  max={max_val:.4f}")

# --- SPLICE SITES at junction ---
print("\n  SPLICE SITES at junction:")
for seq_name in ['fusion', 'normal_ASPSCR1', 'normal_TFE3']:
    key = f'{seq_name}_splice'
    if key not in all_outputs:
        continue
    splice = all_outputs[key].splice_sites
    vals = splice.values
    meta = splice.metadata

    # Find splice sites near junction
    near_junction = slice(junction_pos - 5000, junction_pos + 5000)
    junction_vals = vals[near_junction, :]

    print(f"\n    {seq_name} (10kb around junction/center):")
    for i, (_, row) in enumerate(meta.iterrows()):
        track_name = row.get('name', '')
        col = junction_vals[:, i]
        # Find positions with high splice scores
        high_pos = np.where(col > 0.3)[0]
        if len(high_pos) > 0:
            print(f"      {track_name}: {len(high_pos)} splice sites (score > 0.3)")
            for p in high_pos[:10]:
                actual_pos = junction_pos - 5000 + p
                dist = actual_pos - junction_pos
                print(f"        Position {actual_pos} (junction{dist:+d}): "
                      f"score={col[p]:.4f}")

# --- DNase accessibility at junction ---
print("\n  DNASE accessibility at junction:")
for seq_name in ['fusion', 'normal_ASPSCR1', 'normal_TFE3']:
    key = f'{seq_name}_DNASE'
    if key not in all_outputs:
        continue
    dnase = all_outputs[key].dnase
    vals = dnase.values[center_slice, :]
    meta = dnase.metadata

    print(f"\n    {seq_name}:")
    for i, (_, row) in enumerate(meta.iterrows()):
        tissue = row.get('biosample_name', row.get('name', ''))
        mean_val = float(np.mean(vals[:, i]))
        max_val = float(np.max(vals[:, i]))
        print(f"      {tissue:40s} mean={mean_val:.4f}  max={max_val:.4f}")

# --- CAGE (transcription initiation) ---
print("\n  CAGE transcription initiation at junction:")
for seq_name in ['fusion', 'normal_ASPSCR1', 'normal_TFE3']:
    key = f'{seq_name}_CAGE'
    if key not in all_outputs:
        continue
    cage = all_outputs[key].cage
    vals = cage.values[center_slice, :]
    meta = cage.metadata

    print(f"\n    {seq_name}:")
    for i, (_, row) in enumerate(meta.iterrows()):
        tissue = row.get('biosample_name', row.get('name', ''))
        strand = row.get('strand', '.')
        mean_val = float(np.mean(vals[:, i]))
        max_val = float(np.max(vals[:, i]))
        if mean_val > 0.1 or max_val > 5.0:
            print(f"      {tissue:40s} strand={strand}  "
                  f"mean={mean_val:.4f}  max={max_val:.4f}")

# =============================================
# STEP 5: Generate comparison images
# =============================================
print("\n" + "=" * 70)
print("STEP 5: Generating comparison images")
print("=" * 70)

# Helper to plot comparison
def plot_comparison(fusion_out, normal_out, modality, title_mod,
                    ylabel, fname, zoom_window=50000):
    """Plot fusion vs normal for a given modality."""
    fusion_data = getattr(fusion_out, modality)
    normal_data = getattr(normal_out, modality)

    f_vals = fusion_data.values
    n_vals = normal_data.values
    f_meta = fusion_data.metadata
    n_meta = normal_data.metadata

    n_tracks = min(len(f_meta), len(n_meta), 10)
    center = f_vals.shape[0] // 2
    hw = zoom_window

    fig, axes = plt.subplots(n_tracks, 1, figsize=(20, 3 * n_tracks),
                             sharex=True)
    if n_tracks == 1:
        axes = [axes]

    x = np.arange(center - hw, center + hw)

    for i in range(n_tracks):
        ax = axes[i]
        f_slice = f_vals[center - hw:center + hw, i]
        n_slice = n_vals[center - hw:center + hw, i]

        ax.fill_between(x, n_slice, alpha=0.3, color='gray',
                        label='Normal')
        ax.plot(x, n_slice, color='gray', linewidth=0.8)
        ax.fill_between(x, f_slice, alpha=0.3, color='red',
                        label='Fusion')
        ax.plot(x, f_slice, color='red', linewidth=0.8)
        ax.axvline(center, color='cyan', linewidth=2, linestyle='--',
                   alpha=0.8, label='Junction')

        tissue = f_meta.iloc[i].get('biosample_name',
                 f_meta.iloc[i].get('name', ''))
        strand = f_meta.iloc[i].get('strand', '')
        ax.set_ylabel(f'{tissue}\n{strand}', fontsize=9)
        if i == 0:
            ax.legend(loc='upper right', fontsize=9)

    axes[0].set_title(f'{title_mod}: Fusion vs Normal\n'
                      f'{zoom_window * 2 // 1000}kb window around junction',
                      fontsize=14, fontweight='bold')
    axes[-1].set_xlabel('Position in sequence', fontsize=12)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/{fname}', dpi=150, bbox_inches='tight',
                facecolor='white')
    plt.close('all')
    print(f"  Saved: {OUTPUT_DIR}/{fname}")


# RNA-SEQ comparison (fusion vs normal ASPSCR1)
if 'fusion_RNA_SEQ' in all_outputs and 'normal_ASPSCR1_RNA_SEQ' in all_outputs:
    plot_comparison(
        all_outputs['fusion_RNA_SEQ'],
        all_outputs['normal_ASPSCR1_RNA_SEQ'],
        'rna_seq', 'RNA-seq Expression',
        'Expression', 'fusion_vs_ASPSCR1_rnaseq.png', 50000
    )

# RNA-SEQ fusion vs normal TFE3
if 'fusion_RNA_SEQ' in all_outputs and 'normal_TFE3_RNA_SEQ' in all_outputs:
    plot_comparison(
        all_outputs['fusion_RNA_SEQ'],
        all_outputs['normal_TFE3_RNA_SEQ'],
        'rna_seq', 'RNA-seq Expression',
        'Expression', 'fusion_vs_TFE3_rnaseq.png', 50000
    )

# Splice sites comparison
if 'fusion_splice' in all_outputs and 'normal_ASPSCR1_splice' in all_outputs:
    plot_comparison(
        all_outputs['fusion_splice'],
        all_outputs['normal_ASPSCR1_splice'],
        'splice_sites', 'Splice Sites',
        'Splice score', 'fusion_vs_ASPSCR1_splice.png', 10000
    )

# DNase comparison
if 'fusion_DNASE' in all_outputs and 'normal_ASPSCR1_DNASE' in all_outputs:
    plot_comparison(
        all_outputs['fusion_DNASE'],
        all_outputs['normal_ASPSCR1_DNASE'],
        'dnase', 'DNase Accessibility',
        'DNase', 'fusion_vs_ASPSCR1_dnase.png', 50000
    )

# CAGE comparison
if 'fusion_CAGE' in all_outputs and 'normal_ASPSCR1_CAGE' in all_outputs:
    plot_comparison(
        all_outputs['fusion_CAGE'],
        all_outputs['normal_ASPSCR1_CAGE'],
        'cage', 'CAGE Transcription Initiation',
        'CAGE', 'fusion_vs_ASPSCR1_cage.png', 50000
    )

# =============================================
# STEP 6: Zoomed splice site view at junction
# =============================================
print("\n  Generating zoomed splice site view at junction...")

if 'fusion_splice' in all_outputs:
    splice = all_outputs['fusion_splice'].splice_sites
    vals = splice.values
    meta = splice.metadata
    center = vals.shape[0] // 2

    fig, axes = plt.subplots(len(meta), 1, figsize=(20, 3 * len(meta)),
                             sharex=True)
    if len(meta) == 1:
        axes = [axes]

    zoom = 2000  # 2kb each side
    x = np.arange(center - zoom, center + zoom)

    for i, (_, row) in enumerate(meta.iterrows()):
        ax = axes[i]
        y = vals[center - zoom:center + zoom, i]
        ax.plot(x, y, color='darkblue', linewidth=1)
        ax.fill_between(x, y, alpha=0.3, color='blue')
        ax.axvline(center, color='red', linewidth=2, linestyle='--',
                   label='Fusion junction')
        ax.set_ylabel(row.get('name', ''), fontsize=10)
        if i == 0:
            ax.legend(fontsize=10)

        # Mark high-scoring positions
        high = np.where(y > 0.3)[0]
        for h in high:
            ax.annotate(f'{y[h]:.2f}', xy=(x[h], y[h]),
                        fontsize=7, color='red',
                        ha='center', va='bottom')

    axes[0].set_title('Splice Sites at Fusion Junction (4kb window)\n'
                      'Red line = ASPSCR1-TFE3 junction point',
                      fontsize=14, fontweight='bold')
    axes[-1].set_xlabel('Position in fusion sequence', fontsize=12)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/fusion_splice_junction_zoom.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close('all')
    print(f"  Saved: {OUTPUT_DIR}/fusion_splice_junction_zoom.png")

# =============================================
# STEP 7: Full-length comparison panels
# =============================================
print("\n  Generating full-length RNA-seq comparison panels...")

if 'fusion_RNA_SEQ' in all_outputs and 'normal_ASPSCR1_RNA_SEQ' in all_outputs:
    f_rna = all_outputs['fusion_RNA_SEQ'].rna_seq
    n_rna = all_outputs['normal_ASPSCR1_RNA_SEQ'].rna_seq

    # Pick a representative tissue for each strand
    f_meta = f_rna.metadata
    n_meta = n_rna.metadata

    fig, axes = plt.subplots(2, 1, figsize=(24, 10), sharex=True)

    # Show first + strand and first - strand track
    for track_i, ax in enumerate(axes):
        if track_i >= len(f_meta):
            break

        f_vals = f_rna.values[:, track_i]
        n_vals = n_rna.values[:, track_i]

        # Smooth for visualization
        kernel = 100
        f_smooth = np.convolve(f_vals, np.ones(kernel)/kernel, mode='same')
        n_smooth = np.convolve(n_vals, np.ones(kernel)/kernel, mode='same')

        x = np.arange(len(f_smooth))
        ax.plot(x, n_smooth, color='gray', linewidth=1, alpha=0.7,
                label='Normal ASPSCR1 locus')
        ax.plot(x, f_smooth, color='red', linewidth=1, alpha=0.7,
                label='Fusion sequence')
        ax.axvline(len(f_vals) // 2, color='cyan', linewidth=2,
                   linestyle='--', alpha=0.8, label='Junction')

        tissue = f_meta.iloc[track_i].get('biosample_name', '')
        strand = f_meta.iloc[track_i].get('strand', '')
        ax.set_ylabel(f'{tissue} ({strand})', fontsize=11)
        ax.legend(loc='upper right', fontsize=10)

    axes[0].set_title('Full 500KB RNA-seq: Fusion vs Normal ASPSCR1\n'
                       'Left half = ASPSCR1 promoter region, '
                       'Right half = TFE3 coding region (rev comp)',
                       fontsize=13, fontweight='bold')
    axes[-1].set_xlabel('Position in sequence', fontsize=12)

    plt.tight_layout()
    plt.savefig(f'{OUTPUT_DIR}/fusion_full_length_rnaseq.png',
                dpi=150, bbox_inches='tight', facecolor='white')
    plt.close('all')
    print(f"  Saved: {OUTPUT_DIR}/fusion_full_length_rnaseq.png")


# =============================================
# Save summary data
# =============================================
print("\n" + "=" * 70)
print("SAVING RESULTS")
print("=" * 70)

summary = {
    'fusion_construction': {
        'aspscr1_side': {
            'chromosome': 'chr17',
            'start': ASPSCR1_BP - HALF_LEN,
            'end': ASPSCR1_BP,
            'strand': '+',
            'length': HALF_LEN,
        },
        'tfe3_side': {
            'chromosome': 'chrX',
            'start': TFE3_BP - HALF_LEN,
            'end': TFE3_BP,
            'strand': '- (reverse complemented)',
            'length': HALF_LEN,
        },
        'total_length': len(fusion_seq),
        'junction_position': HALF_LEN,
        'junction_sequence_20bp': aspscr1_seq[-10:] + '|' + tfe3_seq_rc[:10],
    },
}

# Extract key metrics
for seq_name in ['fusion', 'normal_ASPSCR1', 'normal_TFE3']:
    seq_summary = {}

    rna_key = f'{seq_name}_RNA_SEQ'
    if rna_key in all_outputs:
        rna = all_outputs[rna_key].rna_seq
        vals = rna.values
        center = vals.shape[0] // 2
        w = 25000

        tracks = []
        for i, (_, row) in enumerate(rna.metadata.iterrows()):
            center_vals = vals[center - w:center + w, i]
            tracks.append({
                'tissue': row.get('biosample_name', ''),
                'strand': row.get('strand', ''),
                'junction_mean': float(np.mean(center_vals)),
                'junction_max': float(np.max(center_vals)),
            })
        seq_summary['rna_seq_at_junction'] = tracks

    splice_key = f'{seq_name}_splice'
    if splice_key in all_outputs:
        splice = all_outputs[splice_key].splice_sites
        vals = splice.values
        center = vals.shape[0] // 2
        w = 5000

        tracks = []
        for i, (_, row) in enumerate(splice.metadata.iterrows()):
            center_vals = vals[center - w:center + w, i]
            high_count = int(np.sum(center_vals > 0.3))
            tracks.append({
                'track': row.get('name', ''),
                'splice_sites_near_junction': high_count,
                'max_score': float(np.max(center_vals)),
            })
        seq_summary['splice_sites_at_junction'] = tracks

    dnase_key = f'{seq_name}_DNASE'
    if dnase_key in all_outputs:
        dnase = all_outputs[dnase_key].dnase
        vals = dnase.values
        center = vals.shape[0] // 2
        w = 25000

        tracks = []
        for i, (_, row) in enumerate(dnase.metadata.iterrows()):
            center_vals = vals[center - w:center + w, i]
            tracks.append({
                'tissue': row.get('biosample_name', ''),
                'junction_mean': float(np.mean(center_vals)),
                'junction_max': float(np.max(center_vals)),
            })
        seq_summary['dnase_at_junction'] = tracks

    summary[seq_name] = seq_summary

with open(f'{OUTPUT_DIR}/fusion_results.json', 'w') as f:
    json.dump(summary, f, indent=2)
print(f"  Results saved to {OUTPUT_DIR}/fusion_results.json")

print(f"\n  All images saved to {OUTPUT_DIR}/")
print("\nDone.")
