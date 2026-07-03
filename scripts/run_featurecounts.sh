#!/bin/bash

mkdir -p results/featurecounts

featureCounts \
    -a reference/Homo_sapiens.GRCh38.115.gtf \
    -o results/featurecounts/gene_counts.txt \
    -T 4 \
    results/bam/SRR222175.sam \
    results/bam/SRR222176.sam \
    results/bam/SRR222177.sam \
    results/bam/SRR222178.sam

echo "featureCounts complete!"
