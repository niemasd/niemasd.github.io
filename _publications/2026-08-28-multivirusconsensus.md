---
title: "MultiVirusConsensus: An accurate and efficient open-source pipeline for identification and consensus sequence generation of multiple viruses from mixed samples"
collection: publications
pubtype: paper
permalink: /publication/2026-08-28-multivirusconsensus
date: 2026-08-28
venue: 'Bioinformatics Advances'
paperurl: 'https://doi.org/10.1093/bioadv/vbag256'
citation: '<b>Moshiri N</b> (2026). "MultiVirusConsensus: An accurate and efficient open-source pipeline for identification and consensus sequence generation of multiple viruses from mixed samples." <i>Bioinformatics Advances</i>. vbag256. <a href="https://doi.org/10.1093/bioadv/vbag256" target="_blank">doi:10.1093/bioadv/vbag256</a>'
---
**Motivation:** Viral surveillance from mixed samples (e.g. wastewater) has become critical in public health efforts to track and contain pathogens. However, existing open-source bioinformatics tools for viral consensus sequence generation are optimized for individual viruses (rather than multiple potential viruses of interest).

**Results:** MultiVirusConsensus (MVC) is an accurate and efficient open-source pipeline for identification and consensus sequence generation of multiple viruses from mixed samples. It utilizes the memory-efficient ViralConsensus tool to simultaneously perform consensus sequence calling on all viruses of interest (1) completely in parallel, and (2) by piping datastreams between tools without writing/reading intermediate files (thus eliminating slowdowns related to slow disk accesses).

**Availability:** MultiVirusConsensus (MVC) is freely available as an open-source software project at: [https://github.com/niemasd/MultiVirusConsensus](https://github.com/niemasd/MultiVirusConsensus)
