---
title: "FAST: FPGA-based Acceleration of Genomic Sequence Trimming"
collection: publications
pubtype: paper
permalink: /publication/2022-08-12-fast-fpga-trimming
excerpt: 'FAST: FPGA-based Acceleration of Genomic Sequence Trimming'
date: 2022-08-12
venue: 'IEEE Biomedical Circuits and Systems Conference (BioCAS) 2022'
citation: 'Khaleghi B, Zhang T, Shao N, Akel A, Curewitz K, Eno J, Eilert S, <b>Moshiri N</b>, Rosing T (2022). "FAST: FPGA-based Acceleration of Genomic Sequence Trimming." <i>IEEE Biomedical Circuits and Systems Conference (BioCAS) 2022</i>. <a href="https://doi.org/10.1109/BioCAS54905.2022.9948621" target="_blank">doi:10.1109/BioCAS54905.2022.9948621</a>'
---
The sheer amount of genomic sequencing data generated daily that requires time-sensitive processing for downstream analysis calls for accelerating the bioinformatics pipelines. Previous studies mainly have attempted accelerating the alignment stage, leaving the other pipeline stages as performance bottlenecks. In this work, we propose the first FPGA-based framework dubbed FAST to accelerate the stages that deal with sequence trimming, in particular adapter and primer removal. FAST supports a comprehensive set of functionalities and is convenient to use by operating on standard genomics data formats. The proposed framework is fully configurable and supports variety of runtime settings. It surpasses the state-of-the-art widely-used adapter trimmer (fastp) by 4.7x–29.4x speed-up, with 10.1x–54.9x less energy, respectively. For clipping primers, which with current existing tool (iVar) accounts for ~50% of SARS-CoV-2 analysis pipeline, FAST achieves up to 62x speed-up in trimming the virus sequences with a low FPGA resource utilization of 12%. Upon acceptance, we will make our entire framework publicly available.
