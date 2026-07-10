#!/usr/bin/env python3

from pathlib import Path
import pandas as pd

TOP_GENES = Path("results/featurecounts/top20_expressed_genes.tsv")
LOOKUP = Path("results/featurecounts/gene_id_to_symbol.tsv")
OUTPUT = Path("results/featurecounts/top20_expressed_genes_with_symbols.tsv")

top = pd.read_csv(TOP_GENES, sep="\t")

lookup = pd.read_csv(
    LOOKUP,
    sep="\t",
    names=["Geneid", "GeneSymbol"],
    dtype=str
).drop_duplicates(subset="Geneid")

merged = top.merge(lookup, on="Geneid", how="left")

merged["GeneSymbol"] = merged["GeneSymbol"].fillna(merged["Geneid"])

merged = merged[
    [
        "Geneid",
        "GeneSymbol",
        "SRR222175",
        "SRR222176",
        "SRR222177",
        "SRR222178",
        "Total_Count",
    ]
]

merged.to_csv(OUTPUT, sep="\t", index=False)

print(f"Saved: {OUTPUT}")
