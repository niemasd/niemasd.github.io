---
title: "ViralMSA: massively scalable reference-guided multiple sequence alignment of viral genomes"
collection: publications
pubtype: conference
permalink: /publication/2020-11-04-viralmsa-cshl-bio-data-science
date: 2020-11-04
venue: 'Cold Spring Harbor Laboratory (CSHL) Biological Data Science Meeting 2020'
paperurl: 'https://meetings.cshl.edu/posters/data20/data2020_AbstractBookVirtual.pdf'
citation: '<b>Moshiri N</b> (2020). "ViralMSA: massively scalable reference-guided multiple sequence alignment of viral genomes." <i>Cold Spring Harbor Laboratory (CSHL) Biological Data Science Meeting 2020</i>. <a href="https://meetings.cshl.edu/posters/data20/data2020_AbstractBookVirtual.pdf" target="_blank">Poster</a>.'
---
### Motivation
In molecular epidemiology, the identification of clusters of transmissions typically requires the alignment of viral genomic sequence data. However, existing methods of multiple sequence alignment (MSA) scale poorly with respect to the number of sequences.

### Results
ViralMSA is a user-friendly reference-guided MSA tool that leverages the algorithmic techniques of read mappers to enable the MSA of ultra-large viral genome datasets. It scales linearly with the number of sequences, and it is able to align tens of thousands of full viral genomes in seconds. However, alignments produced by ViralMSA omit insertions with respect to the reference genome.

### Availability and implementation
ViralMSA is freely available at [https://github.com/niemasd/ViralMSA](https://github.com/niemasd/ViralMSA) as an open-source software project.
