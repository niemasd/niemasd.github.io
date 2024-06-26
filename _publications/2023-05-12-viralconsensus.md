---
title: "ViralConsensus: A fast and memory-efficient tool for calling viral consensus genome sequences directly from read alignment data"
collection: publications
pubtype: paper
permalink: /publication/2023-05-12-viralconsensus
date: 2023-05-12
venue: 'Bioinformatics'
paperurl: 'https://doi.org/10.1093/bioinformatics/btad317'
citation: '<b>Moshiri N</b> (2023). "ViralConsensus: A fast and memory-efficient tool for calling viral consensus genome sequences directly from read alignment data." <i>Bioinformatics</i>. 39(5):btad317. <a href="https://doi.org/10.1093/bioinformatics/btad317" target="_blank">doi:10.1093/bioinformatics/btad317</a>'
---
### Motivation
In viral molecular epidemiology, reconstruction of consensus genomes from sequence data is critical for tracking mutations and variants of concern. However, as the number of samples that are sequenced grows rapidly, compute resources needed to reconstruct consensus genomes can become prohibitively large.

### Results
ViralConsensus is a fast and memory-efficient tool for calling viral consensus genome sequences directly from read alignment data. ViralConsensus is orders of magnitude faster and more memory-efficient than existing methods. Further, unlike existing methods, ViralConsensus can pipe data directly from a read mapper via standard input and performs viral consensus calling on-the-fly, making it an ideal tool for viral sequencing pipelines.

### Availability
ViralConsensus is freely available at [https://github.com/niemasd/ViralConsensus](https://github.com/niemasd/ViralConsensus) as an open-source software project.
