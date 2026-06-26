# BIFS 619 RNA-Seq Group Project

## Team Members
- Ayorinde Ojo
- Granados Sandra
- McKee Liber

## Project Objective
Perform a human RNA-seq analysis using publicly available sequencing data from the NCBI Sequence Read Archive (SRA). The workflow includes quality control, read cleaning, alignment, quantification, and biological interpretation.

## Dataset

**BioProject:** PRJNA141411

Samples:

| Run | Sample | Condition |
|-----|--------|-----------|
| SRR222175 | RNA_seq_P1N | Normal |
| SRR222176 | RNA_seq_P1T | Tumor |
| SRR222177 | RNA_seq_P2N | Normal |
| SRR222178 | RNA_seq_P2T | Tumor |

## Software

- FastQC
- MultiQC
- fastp
- HISAT2
- featureCounts

## Workflow

1. Download sequencing data
2. Quality control (FastQC)
3. Aggregate QC (MultiQC)
4. Read trimming (fastp)
5. Alignment (HISAT2)
6. Gene quantification (featureCounts)
7. Differential expression analysis
8. Biological interpretation

## Repository Structure

```
data/
figures/
notes/
reports/
results/
scripts/
templates/
```

## Notes

Raw FASTQ files are excluded from Git using `.gitignore` because of their large size. They can be downloaded using:

```bash
./scripts/download_data.sh
```
