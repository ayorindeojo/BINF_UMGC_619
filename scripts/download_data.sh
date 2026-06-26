#!/bin/bash

# Download Human RNA-seq dataset
prefetch SRR222175
prefetch SRR222176
prefetch SRR222177
prefetch SRR222178

fasterq-dump SRR222175 -O data/
fasterq-dump SRR222176 -O data/
fasterq-dump SRR222177 -O data/
fasterq-dump SRR222178 -O data/

gzip data/*.fastq
