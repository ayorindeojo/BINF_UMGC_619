#!/bin/bash

mkdir -p results/fastp
mkdir -p data/cleaned

for SAMPLE in SRR222175 SRR222176 SRR222177 SRR222178
do
    echo "Cleaning $SAMPLE..."

    fastp \
        -i data/${SAMPLE}.fastq.gz \
        -o data/cleaned/${SAMPLE}_cleaned.fastq.gz \
        --html results/fastp/${SAMPLE}_fastp.html \
        --json results/fastp/${SAMPLE}_fastp.json \
        --thread 4
done

echo "Read cleaning complete!"
