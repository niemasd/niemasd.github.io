---
title: "FPGA Acceleration of Protein Back-Translation and Alignment"
collection: publications
pubtype: conference
permalink: /publication/2020-10-27-fpga-protein-back-translation-ashg
excerpt: 'FPGA Acceleration of Protein Back-Translation and Alignment'
date: 2020-10-27
venue: 'American Society of Human Genetics (ASHG) 2020'
citation: 'Salamat S, Kang J, Kim Y, Imani M, <b>Moshiri N</b>, Rosing T (2020). "FPGA Acceleration of Protein Back-Translation and Alignment." <i>American Society of Human Genetics (ASHG) 2020</i>. Poster.'
---
Identifying genome functionality changes our understanding of humans and helps us in disease diagnosis; as well as drug, bio-material, and genetic engineering of plants and animals. Comparing the structure of the protein sequences, when only sequence information is available, against a database with known functionality helps us to identify and recognize the functionality of the unknown sequence. The process of predicting the possible RNA sequence that a specific protein has originated from is called back-translation. Aligning the back-translated RNA sequence against the database locates the most similar sequences, which is used to predict the functionality of the unknown protein sequence. Providing massive parallelism, FPGAs can accelerate bioinformatics applications substantially. In this paper, we propose, FabP (FabP is also the name of a family of proteins, "Fatty-Acid-Binding Proteins"), an optimized FPGA-based accelerator for aligning a back-translated protein sequence against a database of DNA/RNA sequences. FabP is deeply optimized to fully utilize the FPGA resources and the DRAM memory bandwidth to maximize the performance. FabP on a mid-range FPGA provides 8.1 % and 23.3× (24.8× and 266.8 ×) speedup and higher energy efficiency as compared to the GPU-based implementation on a high-end NVIDIA GPU (state-of-the-art CPU implementation), respectively.
