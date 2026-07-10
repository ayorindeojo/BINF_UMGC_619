#!/bin/bash

set -euo pipefail

REFERENCE_DIR="reference"
INDEX_DIR="${REFERENCE_DIR}/index"

FASTA_GZ="Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz"
FASTA="Homo_sapiens.GRCh38.dna.primary_assembly.fa"

GTF_GZ="Homo_sapiens.GRCh38.115.gtf.gz"
GTF="Homo_sapiens.GRCh38.115.gtf"

FASTA_URL="https://ftp.ensembl.org/pub/release-115/fasta/homo_sapiens/dna/${FASTA_GZ}"
GTF_URL="https://ftp.ensembl.org/pub/release-115/gtf/homo_sapiens/${GTF_GZ}"

mkdir -p "${REFERENCE_DIR}" "${INDEX_DIR}"

cd "${REFERENCE_DIR}"

if [ ! -f "${FASTA}" ]; then
    echo "Downloading GRCh38 reference genome..."
    wget -c "${FASTA_URL}"

    echo "Decompressing reference genome..."
    gunzip -f "${FASTA_GZ}"
else
    echo "Reference genome already exists. Skipping download."
fi

if [ ! -f "${GTF}" ]; then
    echo "Downloading Ensembl release 115 GTF..."
    wget -c "${GTF_URL}"

    echo "Decompressing GTF..."
    gunzip -f "${GTF_GZ}"
else
    echo "GTF already exists. Skipping download."
fi

if [ ! -f "index/grch38.1.ht2" ]; then
    echo "Building HISAT2 GRCh38 index..."

    hisat2-build \
        "${FASTA}" \
        "index/grch38"
else
    echo "HISAT2 index already exists. Skipping index build."
fi

echo "Reference setup complete."
