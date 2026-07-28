import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

input_file = "results/featurecounts/top20_expressed_genes_with_symbols.tsv"
df = pd.read_csv(input_file, sep='\t')

# Extract just the count data and transpose it so samples are rows
counts = df[["SRR222175", "SRR222176", "SRR222177", "SRR222178"]].T
labels = ["P1 Normal", "P1 Tumor", "P2 Normal", "P2 Tumor"]
conditions = ["Normal", "Tumor", "Normal", "Tumor"]
colors = {"Normal": "#4C72B0", "Tumor": "#C44E52"}

# Standardize and run PCA
scaler = StandardScaler()
scaled_data = scaler.fit_transform(counts)
pca = PCA(n_components=2)
pca_results = pca.fit_transform(scaled_data)

# Plot
plt.figure(figsize=(8, 6))
for i, label in enumerate(labels):
    plt.scatter(pca_results[i, 0], pca_results[i, 1], 
                color=colors[conditions[i]], s=150, label=conditions[i] if i < 2 else "")
    plt.text(pca_results[i, 0] + 0.5, pca_results[i, 1], label)

plt.title('PCA of Top Expressed Genes')
plt.xlabel(f'PC1 ({pca.explained_variance_ratio_[0]*100:.1f}%)')
plt.ylabel(f'PC2 ({pca.explained_variance_ratio_[1]*100:.1f}%)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.savefig('figures/pca_plot.png')
print("Figure 3 saved as pca_plot.png")
