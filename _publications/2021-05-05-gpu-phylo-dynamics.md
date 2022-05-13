---
title: "A GPU-Powered Phylogenetic Analysis for Large-scale Genomic Sequences"
collection: publications
pubtype: conference
permalink: /publication/2021-05-05-gpu-phylo-dynamics
excerpt: 'A GPU-Powered Phylogenetic Analysis for Large-scale Genomic Sequences'
date: 2021-05-05
venue: '28th International Dynamics & Evolution of Human Viruses'
citation: 'Kang J, Young C, Morris J, Akel A, Eilert S, Eno J, Curewitz K, <b>Moshiri N</b>, Rosing T (2021). "A GPU-Powered Phylogenetic Analysis for Large-scale Genomic Sequences." <i>28th International Dynamics & Evolution of Human Viruses</i>. Poster.'
---
Phylogenetic inference is a standard procedure in many viral molecular epidemiological workflows. Currently, the state-of-the-art phylogenetic inference methods highly rely on CPU-based tools, and while these tools are able to run in reasonable amounts of time on smaller viral datasets of the past, the massive global sequencing efforts of the SARS-CoV-2 pandemic have yielded ultra-large datasets that yield real-time phylogenetic inference infeasible using existing CPU-based tools. In this work, we propose a maximum likelihood (ML)-based phylogenetics analysis acceleration strategy using graphics processing units (GPU). Based on our analysis of IQ-TREE 2, we offload and parallelize the ML scoring function to the GPU, which is shown to be the main bottleneck of the analysis. The proposed tool converts and handles the tree topology and sequences in a GPU-friendly manner, which maximizes memory coalescing. Through the parallelization of the bottom-up tree reconstruction and scoring per site, the proposed solution leads to significant speedup of the scoring function. Our evaluation results show that the tree scoring function can be run 32x faster on the GPU, as compared to the CPU-based implementation. Further, on a benchmarking experiment measuring overall phylogenetic inference runtime on simulated data modeling SARS-CoV-2 whole genome sequences, we show over an order of magnitude of speedup in our GPU-scoring IQ-TREE 2 implementation compared to the official CPU-based implementation, and the speedup widens as the number of sequences grows.
