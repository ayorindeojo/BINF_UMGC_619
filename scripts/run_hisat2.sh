#!/bin/bash

mkdir -p results/hisat2
mkdir -p results/bam

for SAMPLE in SRR222175 SRR222176 SRR222177 SRR222178
do
    echo "Aligning ${SAMPLE}..."

    hisat2 \
        -x reference/index/grch38 \
        -U data/cleaned/${SAMPLE}_cleaned.fastq.gz \
        -S results/bam/${SAMPLE}.sam \
        --summary-file results/hisat2/${SAMPLE}_summary.txt \
        -p 4

done

echo "Alignment complete!"
