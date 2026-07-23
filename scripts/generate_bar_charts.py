import pandas as pd
import matplotlib.pyplot as plt

# --- FIGURE 5: Total Read Counts per Sample ---
input_file = "results/featurecounts/gene_counts.txt"
# Skip the first metadata line of featureCounts output
df = pd.read_csv(input_file, sep='\t', comment='#')

samples = ["SRR222175", "SRR222176", "SRR222177", "SRR222178"]
labels = ["P1 Normal", "P1 Tumor", "P2 Normal", "P2 Tumor"]

# Sum up all columns to get total assigned reads
total_counts = [df[col].sum() for col in df.columns if any(s in col for s in samples)]

plt.figure(figsize=(8, 6))
plt.bar(labels, total_counts, color=['#4C72B0', '#C44E52', '#4C72B0', '#C44E52'])
plt.title('Total Reads Assigned to Genes by featureCounts')
plt.ylabel('Total Read Count')
plt.savefig('figures/total_read_counts.png')
plt.close()
print("Figure 5 saved as total_read_counts.png")

# --- FIGURE 2: Alignment Rate Bar Chart ---
# UPDATE THESE NUMBERS based on your actual HISAT2 summary logs
alignment_rates = [92.5, 93.1, 91.8, 94.2] 

plt.figure(figsize=(8, 6))
plt.bar(labels, alignment_rates, color=['#55A868', '#DD8452', '#55A868', '#DD8452'])
plt.ylim(0, 100)
plt.title('HISAT2 Overall Alignment Rates')
plt.ylabel('Alignment Rate (%)')
for i, v in enumerate(alignment_rates):
    plt.text(i, v + 1, str(v)+'%', ha='center')
plt.savefig('figures/alignment_rates.png')
plt.close()
print("Figure 2 saved as alignment_rates.png")
