import pandas as pd
import matplotlib.pyplot as plt

INPUT_FILE = "results/featurecounts/top20_expressed_genes_with_symbols.tsv"
TARGET_GENE = "CEACAM5"  # <-- Change this to your most interesting gene!

df = pd.read_csv(INPUT_FILE, sep='\t')
gene_data = df[df['GeneSymbol'] == TARGET_GENE]

if gene_data.empty:
    print(f"Gene {TARGET_GENE} not found in the dataset.")
else:
    counts = gene_data[["SRR222175", "SRR222176", "SRR222177", "SRR222178"]].values[0]
    labels = ["P1 Normal", "P1 Tumor", "P2 Normal", "P2 Tumor"]
    
    plt.figure(figsize=(8, 6))
    plt.bar(labels, counts, color=['#4C72B0', '#C44E52', '#4C72B0', '#C44E52'])
    plt.title(f'{TARGET_GENE} Expression Levels')
    plt.ylabel('Raw Read Count')
    plt.savefig('figures/top_gene_expression.png')
    print("Figure 4 saved as top_gene_expression.png")
