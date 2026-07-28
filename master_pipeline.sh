#!/bin/bash

# ==============================================================================
# BIFS 619 - Group Project Master Pipeline
# This script automates the full RNA-Seq workflow from raw data to visualization
# ==============================================================================

# Exit immediately if a command exits with a non-zero status
set -e

echo "========================================"
echo " Starting Master RNA-Seq Pipeline"
echo "========================================"

# Step 1: Download Data
echo ""
echo "[1/7] Downloading raw RNA-Seq data..."
bash download_data.sh

# Step 2: Quality Control & Trimming
echo ""
echo "[2/7] Running FastP for quality control..."
bash run_fastp.sh

# Step 3: Setup Reference Genome
echo ""
echo "[3/7] Setting up HISAT2 reference genome..."
bash setup_hisat2_reference.sh

# Step 4: Alignment
echo ""
echo "[4/7] Aligning reads to the reference with HISAT2..."
bash run_hisat2.sh

# Step 5: Quantification
echo ""
echo "[5/7] Quantifying gene expression with featureCounts..."
bash run_featurecounts.sh

# Step 6: Data Wrangling
echo ""
echo "[6/7] Merging gene symbols into the count data..."
python3 add_gene_symbols.py

# Step 7: Data Visualization
echo ""
echo "[7/7] Generating the top 20 expression heatmap..."
python3 create_expression_heatmap.py

echo ""
echo "========================================"
echo " Pipeline Complete! Check the /figures directory for your outputs."
echo "========================================"