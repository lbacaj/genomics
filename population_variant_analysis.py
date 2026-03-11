"""Population Variant Overlap Analysis.

Cross-references the critical ISM positions against gnomAD and ClinVar
to check whether known variants exist at positions identified as
functionally important by the AlphaGenome ISM analysis.

Critical positions (from extend_ism_deep.py results):
- TFE3: chrX:49,043,887-49,043,893 (7bp immune regulatory element, DNase 3.0+)
- DNMT1-chr19: chr19:10,160,175 (T-cell/NK cell chromatin switch, 0.436 DNase)
- ASPSCR1: chr17:82,010,867-82,010,870 (fibroblast regulatory hotspot)

Also queries the breakpoint positions themselves and key nearby positions.
"""

import os
import sys
import json
import time
import urllib.request
import urllib.error

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

OUTPUT_DIR = '/Users/lbacaj/genomics/population_variants'
os.makedirs(OUTPUT_DIR, exist_ok=True)

# =============================================
# Query positions
# =============================================

query_positions = {
    'TFE3_ISM_regulatory': {
        'chrom': 'X', 'positions': list(range(49043887, 49043894)),
        'description': '7bp immune regulatory element (DNase 3.0+)',
        'breakpoint': 'TFE3',
    },
    'DNMT1_chr19_ISM_switch': {
        'chrom': '19', 'positions': [10160175],
        'description': 'T-cell/NK cell chromatin switch (0.436 DNase)',
        'breakpoint': 'DNMT1_chr19',
    },
    'ASPSCR1_ISM_hotspot': {
        'chrom': '17', 'positions': list(range(82010867, 82010871)),
        'description': 'Fibroblast regulatory hotspot',
        'breakpoint': 'ASPSCR1',
    },
    'ASPSCR1_breakpoint': {
        'chrom': '17', 'positions': [82010811],
        'description': 'ASPSCR1 breakpoint position',
        'breakpoint': 'ASPSCR1',
    },
    'TFE3_breakpoint': {
        'chrom': 'X', 'positions': [49043986],
        'description': 'TFE3 breakpoint position',
        'breakpoint': 'TFE3',
    },
    'DNMT1_chr1_breakpoint': {
        'chrom': '1', 'positions': [31048832],
        'description': 'DNMT1-chr1 breakpoint (inside PUM1)',
        'breakpoint': 'DNMT1_chr1',
    },
    'DNMT1_chr19_breakpoint': {
        'chrom': '19', 'positions': [10160241],
        'description': 'DNMT1-chr19 breakpoint position',
        'breakpoint': 'DNMT1_chr19',
    },
}

# =============================================
# gnomAD GraphQL API
# =============================================

GNOMAD_API = 'https://gnomad.broadinstitute.org/api'

def query_gnomad_region(chrom, start, end, dataset='gnomad_r4'):
    """Query gnomAD for variants in a region."""
    query = """
    query {
      region(chrom: "%s", start: %d, stop: %d, reference_genome: GRCh38) {
        variants(dataset: %s) {
          variant_id
          pos
          ref
          alt
          exome {
            ac
            an
            af
          }
          genome {
            ac
            an
            af
          }
          rsids
          consequence
          flags
        }
      }
    }
    """ % (chrom, start, end, dataset)

    data = json.dumps({'query': query}).encode('utf-8')
    req = urllib.request.Request(
        GNOMAD_API,
        data=data,
        headers={'Content-Type': 'application/json'},
    )

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            result = json.loads(resp.read().decode('utf-8'))
            if 'data' in result and result['data'] and 'region' in result['data']:
                return result['data']['region']['variants']
            elif 'errors' in result:
                print(f"    gnomAD API error: {result['errors']}")
                return []
            return []
    except Exception as e:
        print(f"    gnomAD query error: {e}")
        return []


# =============================================
# ClinVar / NCBI E-utilities
# =============================================

NCBI_EUTILS = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils'

def query_clinvar_position(chrom, pos):
    """Query ClinVar for variants at a specific position (hg38)."""
    # Search ClinVar using chromosome position
    search_term = f'{chrom}[Chromosome] AND {pos}:{pos}[Base Position for Assembly GRCh38]'

    search_url = (f'{NCBI_EUTILS}/esearch.fcgi?db=clinvar'
                  f'&term={urllib.request.quote(search_term)}'
                  f'&retmax=20&retmode=json')

    try:
        with urllib.request.urlopen(search_url, timeout=30) as resp:
            result = json.loads(resp.read().decode('utf-8'))

        id_list = result.get('esearchresult', {}).get('idlist', [])
        if not id_list:
            return []

        # Fetch details for found variants
        ids = ','.join(id_list)
        summary_url = (f'{NCBI_EUTILS}/esummary.fcgi?db=clinvar'
                       f'&id={ids}&retmode=json')

        with urllib.request.urlopen(summary_url, timeout=30) as resp:
            summary = json.loads(resp.read().decode('utf-8'))

        variants = []
        for uid in id_list:
            if uid in summary.get('result', {}):
                entry = summary['result'][uid]
                variants.append({
                    'clinvar_id': uid,
                    'title': entry.get('title', ''),
                    'clinical_significance': entry.get('clinical_significance', {}).get('description', ''),
                    'gene': entry.get('genes', [{}])[0].get('symbol', '') if entry.get('genes') else '',
                    'review_status': entry.get('clinical_significance', {}).get('review_status', ''),
                    'condition': '; '.join([t.get('trait_name', '') for t in entry.get('trait_set', [])]) if entry.get('trait_set') else '',
                })
        return variants

    except Exception as e:
        print(f"    ClinVar query error: {e}")
        return []


# =============================================
# Run queries
# =============================================

all_results = {}

for region_name, info in query_positions.items():
    chrom = info['chrom']
    positions = info['positions']
    desc = info['description']

    print("=" * 70)
    print(f"REGION: {region_name}")
    print(f"  {desc}")
    print(f"  chr{chrom}:{min(positions):,}-{max(positions):,}")
    print("=" * 70)

    region_results = {
        'description': desc,
        'chrom': chrom,
        'positions': positions,
        'gnomad_variants': [],
        'clinvar_variants': [],
    }

    # Query gnomAD for the region (with 10bp padding)
    start = min(positions) - 10
    end = max(positions) + 10
    print(f"\n  Querying gnomAD (region chr{chrom}:{start}-{end})...")

    gnomad_variants = query_gnomad_region(chrom, start, end)
    time.sleep(1)  # Rate limiting

    if gnomad_variants:
        # Filter to exact positions of interest
        exact_hits = [v for v in gnomad_variants if v['pos'] in positions]
        nearby = [v for v in gnomad_variants if v['pos'] not in positions]

        print(f"  gnomAD results: {len(gnomad_variants)} total variants in region")
        print(f"  At exact ISM positions: {len(exact_hits)}")
        print(f"  Nearby (within 10bp): {len(nearby)}")

        for v in exact_hits:
            af_genome = v.get('genome', {})
            af_exome = v.get('exome', {})
            af = af_genome.get('af', 0) if af_genome else (af_exome.get('af', 0) if af_exome else 0)
            ac = af_genome.get('ac', 0) if af_genome else (af_exome.get('ac', 0) if af_exome else 0)
            rsids = v.get('rsids', [])
            rsid = rsids[0] if rsids else 'none'
            print(f"    EXACT HIT: pos={v['pos']} {v['ref']}>{v['alt']}  "
                  f"AF={af:.6f}  AC={ac}  rs={rsid}  "
                  f"consequence={v.get('consequence', 'N/A')}")

        for v in nearby[:5]:
            af_genome = v.get('genome', {})
            af_exome = v.get('exome', {})
            af = af_genome.get('af', 0) if af_genome else (af_exome.get('af', 0) if af_exome else 0)
            rsids = v.get('rsids', [])
            rsid = rsids[0] if rsids else 'none'
            print(f"    Nearby: pos={v['pos']} {v['ref']}>{v['alt']}  "
                  f"AF={af:.6f}  rs={rsid}")

        region_results['gnomad_variants'] = gnomad_variants
        region_results['gnomad_exact_hits'] = exact_hits
        region_results['gnomad_nearby'] = nearby
    else:
        print(f"  gnomAD: No variants found in region")
        region_results['gnomad_exact_hits'] = []
        region_results['gnomad_nearby'] = []

    # Query ClinVar for each position
    print(f"\n  Querying ClinVar...")
    clinvar_results = []
    for pos in positions:
        cv = query_clinvar_position(chrom, pos)
        if cv:
            print(f"  ClinVar hits at chr{chrom}:{pos}:")
            for c in cv:
                print(f"    {c['title']}  significance={c['clinical_significance']}  "
                      f"gene={c['gene']}")
            clinvar_results.extend(cv)
        time.sleep(0.5)  # Rate limiting

    if not clinvar_results:
        print(f"  ClinVar: No variants at these positions")

    region_results['clinvar_variants'] = clinvar_results
    all_results[region_name] = region_results
    print()

# =============================================
# Conservation analysis via gnomAD constraint
# =============================================
print("=" * 70)
print("CONSERVATION ANALYSIS")
print("=" * 70)

# Check if positions are in constrained regions by looking at
# variant density: highly conserved regions have fewer variants
conservation_summary = {}
for region_name, info in query_positions.items():
    chrom = info['chrom']
    positions = info['positions']

    # Query a wider region (1kb) to assess variant density
    center = (min(positions) + max(positions)) // 2
    wide_start = center - 500
    wide_end = center + 500

    print(f"\n  Checking variant density in 1kb around {region_name}...")
    wide_variants = query_gnomad_region(chrom, wide_start, wide_end)
    time.sleep(1)

    n_variants = len(wide_variants) if wide_variants else 0
    density = n_variants / 1000  # variants per bp

    # Count common variants (AF > 0.01)
    common = 0
    rare = 0
    if wide_variants:
        for v in wide_variants:
            af_genome = v.get('genome', {})
            af = af_genome.get('af', 0) if af_genome else 0
            if af > 0.01:
                common += 1
            elif af > 0:
                rare += 1

    conservation_summary[region_name] = {
        'total_variants_1kb': n_variants,
        'density_per_bp': density,
        'common_variants': common,
        'rare_variants': rare,
    }

    constraint_level = ('HIGHLY CONSERVED' if common == 0 and n_variants < 10
                        else 'CONSERVED' if common < 3
                        else 'VARIABLE')

    print(f"    Total variants in 1kb window: {n_variants}")
    print(f"    Common (AF>1%): {common}, Rare: {rare}")
    print(f"    Density: {density:.3f} variants/bp")
    print(f"    Assessment: {constraint_level}")

all_results['conservation'] = conservation_summary

# Save results
output_path = f'{OUTPUT_DIR}/population_variant_results.json'
with open(output_path, 'w') as f:
    json.dump(all_results, f, indent=2, default=str)
print(f"\nResults saved to {output_path}")

# =============================================
# Visualization
# =============================================
print("\nGenerating visualizations...")

# 1. Variant density comparison across regions
regions = list(conservation_summary.keys())
densities = [conservation_summary[r]['density_per_bp'] for r in regions]
common_counts = [conservation_summary[r]['common_variants'] for r in regions]
total_counts = [conservation_summary[r]['total_variants_1kb'] for r in regions]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

# Bar plot of variant density
colors = ['#e74c3c' if 'ISM' in r or 'hotspot' in r or 'switch' in r
          else '#3498db' for r in regions]
labels = [r.replace('_', '\n') for r in regions]

ax1.bar(range(len(regions)), total_counts, color=colors, alpha=0.8)
ax1.set_xticks(range(len(regions)))
ax1.set_xticklabels(labels, fontsize=8, rotation=45, ha='right')
ax1.set_ylabel('Total variants in 1kb window', fontsize=11)
ax1.set_title('gnomAD Variant Density Near Critical Positions\n'
              'Red = ISM regulatory elements | Blue = breakpoints',
              fontsize=12, fontweight='bold')

# Common vs rare
bar_width = 0.35
x = np.arange(len(regions))
ax2.bar(x - bar_width/2, common_counts, bar_width, label='Common (AF>1%)',
        color='#e74c3c', alpha=0.8)
rare_counts = [conservation_summary[r]['rare_variants'] for r in regions]
ax2.bar(x + bar_width/2, rare_counts, bar_width, label='Rare (AF<1%)',
        color='#3498db', alpha=0.8)
ax2.set_xticks(x)
ax2.set_xticklabels(labels, fontsize=8, rotation=45, ha='right')
ax2.set_ylabel('Number of variants', fontsize=11)
ax2.set_title('Common vs Rare Variants\n1kb window around each position',
              fontsize=12, fontweight='bold')
ax2.legend(fontsize=10)

plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/variant_density_comparison.png',
            dpi=150, bbox_inches='tight', facecolor='white')
plt.close('all')
print(f"  Saved: {OUTPUT_DIR}/variant_density_comparison.png")

# 2. Summary table visualization
fig, ax = plt.subplots(figsize=(14, 6))
ax.axis('off')

table_data = []
for region_name in query_positions:
    info = query_positions[region_name]
    result = all_results.get(region_name, {})
    cons = conservation_summary.get(region_name, {})

    n_exact = len(result.get('gnomad_exact_hits', []))
    n_clinvar = len(result.get('clinvar_variants', []))
    n_total = cons.get('total_variants_1kb', 0)
    n_common = cons.get('common_variants', 0)

    constraint = ('HIGHLY CONSERVED' if n_common == 0 and n_total < 10
                  else 'CONSERVED' if n_common < 3
                  else 'VARIABLE')

    table_data.append([
        region_name.replace('_', ' '),
        f"chr{info['chrom']}:{min(info['positions']):,}",
        info['description'][:40],
        str(n_exact),
        str(n_clinvar),
        str(n_total),
        constraint,
    ])

table = ax.table(
    cellText=table_data,
    colLabels=['Region', 'Position', 'Description', 'gnomAD\nExact', 'ClinVar',
               'Variants\nin 1kb', 'Constraint'],
    loc='center',
    cellLoc='center',
)
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1.2, 1.5)

# Color constraint column
for i, row in enumerate(table_data):
    constraint = row[-1]
    cell = table[i + 1, 6]
    if constraint == 'HIGHLY CONSERVED':
        cell.set_facecolor('#27ae60')
        cell.set_text_props(color='white', fontweight='bold')
    elif constraint == 'CONSERVED':
        cell.set_facecolor('#f39c12')
    else:
        cell.set_facecolor('#e74c3c')
        cell.set_text_props(color='white')

ax.set_title('Population Variant Overlap Summary\n'
             'gnomAD v4 + ClinVar at Critical ISM Positions',
             fontsize=13, fontweight='bold', pad=20)
plt.tight_layout()
plt.savefig(f'{OUTPUT_DIR}/variant_summary_table.png',
            dpi=150, bbox_inches='tight', facecolor='white')
plt.close('all')
print(f"  Saved: {OUTPUT_DIR}/variant_summary_table.png")

# Final summary
print("\n" + "=" * 70)
print("POPULATION VARIANT ANALYSIS SUMMARY")
print("=" * 70)

for region_name, info in query_positions.items():
    result = all_results.get(region_name, {})
    cons = conservation_summary.get(region_name, {})

    n_exact = len(result.get('gnomad_exact_hits', []))
    n_clinvar = len(result.get('clinvar_variants', []))
    n_total = cons.get('total_variants_1kb', 0)
    n_common = cons.get('common_variants', 0)

    print(f"\n  {region_name}: {info['description']}")
    print(f"    gnomAD exact hits: {n_exact}")
    print(f"    ClinVar entries: {n_clinvar}")
    print(f"    Variants in 1kb: {n_total} (common: {n_common})")

    # Report specific hits
    for v in result.get('gnomad_exact_hits', []):
        af_genome = v.get('genome', {})
        af = af_genome.get('af', 0) if af_genome else 0
        rsids = v.get('rsids', [])
        print(f"    -> {v['ref']}>{v['alt']} at {v['pos']} AF={af:.6f} rs={rsids}")

    for c in result.get('clinvar_variants', []):
        print(f"    -> ClinVar: {c['title']} [{c['clinical_significance']}]")

print(f"\nAll results saved to {OUTPUT_DIR}/")
print("Done.")
