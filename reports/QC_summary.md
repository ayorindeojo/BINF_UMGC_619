# Quality Control Summary

## Tools
- FastQC
- MultiQC

## Samples
- SRR222175
- SRR222176
- SRR222177
- SRR222178

## Results

Quality assessment was performed using FastQC and summarized with MultiQC. All four RNA-seq samples completed the QC process successfully.

| Sample | Total Reads | GC (%) | Read Length (bp) | Duplication (%) |
|---------|------------:|-------:|-----------------:|----------------:|
| SRR222175 | 9,037,384 | 48 | 65 | 51.70 |
| SRR222176 | 8,542,144 | 56 | 65 | 39.55 |
| SRR222177 | 11,308,009 | 51 | 65 | 38.35 |
| SRR222178 | 11,461,875 | 50 | 65 | 35.72 |

The sequencing depth ranged from approximately 8.5 to 11.5 million reads per sample. All samples had a consistent read length of 65 bp. GC content ranged from 48% to 56%, while sequence duplication ranged from 35.7% to 51.7%. Although SRR222175 showed the highest duplication level, increased duplication is common in RNA-seq because highly expressed transcripts generate many identical reads.

Overall, the samples were considered suitable for downstream preprocessing and alignment. The next step is read cleaning using fastp.
