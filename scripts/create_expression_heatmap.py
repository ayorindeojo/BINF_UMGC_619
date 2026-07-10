#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

INPUT_FILE = "results/featurecounts/top20_expressed_genes_with_symbols.tsv"
OUTPUT_FILE = "figures/top20_expression_heatmap.png"

# Read the top-gene table.
df = pd.read_csv(INPUT_FILE, sep="\t")

# Use gene symbols as row labels.
counts = df.set_index("GeneSymbol")[
    ["SRR222175", "SRR222176", "SRR222177", "SRR222178"]
]

# Replace run accessions with biological sample labels.
counts.columns = [
    "P1 Normal",
    "P1 Tumor",
    "P2 Normal",
    "P2 Tumor",
]

# Log transformation reduces the effect of very large raw counts.
log_counts = np.log2(counts + 1)

plt.figure(figsize=(9, 10))
plt.imshow(log_counts, aspect="auto")

plt.colorbar(label="Log2(Read Count + 1)")

plt.xticks(
    range(len(log_counts.columns)),
    log_counts.columns,
    rotation=45,
    ha="right"
)

plt.yticks(
    range(len(log_counts.index)),
    log_counts.index
)

plt.xlabel("RNA-seq sample")
plt.ylabel("Top Expressed Genes")
plt.title("Top 20 Highly Expressed Genes: Normal vs Tumor")

plt.tight_layout()
plt.savefig(OUTPUT_FILE, dpi=300)
plt.close()

print(f"Heatmap saved to {OUTPUT_FILE}")
