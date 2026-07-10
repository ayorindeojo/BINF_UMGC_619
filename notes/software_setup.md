# RNA-seq Software Setup

Date: June 2026

## Software installed in the VM

- FastQC
- MultiQC v1.12 (default)
- fastp 0.20.1
- HISAT2 2.2.1
- featureCounts 2.0.3

Environment:
UMGC Virtual Machine

## Software verified

- FastQC
- MultiQC
- fastp
- HISAT2
- featureCounts

## QC software used

- FastQC
- MultiQC v1.35

## MultiQC Version Note

The UMGC VM includes MultiQC v1.12 by default. During quality control, the report generated with v1.12 failed to render interactive plots because it attempted to load external Highcharts JavaScript libraries that returned HTTP 403 errors.

To resolve this issue, a separate Conda environment (multiqc_new) was created with MultiQC v1.35. The QC report was regenerated successfully using v1.35, and all interactive plots rendered correctly.


## Reference Genome and Annotation

Reference genome:
GRCh38 (Homo sapiens primary assembly)

Genome FASTA:
Homo_sapiens.GRCh38.dna.primary_assembly.fa

Gene annotation:
Homo_sapiens.GRCh38.115.gtf

Alignment:
Reads were aligned using HISAT2 v2.2.1.

HISAT2 index:
The HISAT2 index was built locally from the GRCh38 primary assembly FASTA using the `hisat2-build` command.

The reference FASTA, GTF file, and HISAT2 index are stored locally in the project reference directory but were not committed to GitHub because of their large size.
