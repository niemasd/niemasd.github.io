---
title: "Ultra Efficient Acceleration for De Novo Genome Assembly via Near-Memory Computing"
collection: publications
pubtype: paper
permalink: /publication/2021-09-26-de-novo-dbg-assembly-acceleration
date: 2021-09-26
venue: 'International Conference on Parallel Architectures and Compilation Techniques (PACT) 2021'
paperurl: 'https://doi.org/10.1109/PACT52795.2021.00022'
citation: 'Zhou M, Wu L, Li M, <b>Moshiri N</b>, Skadron K, Rosing T (2021). "Ultra Efficient Acceleration for De Novo Genome Assembly via Near-Memory Computing." <i>International Conference on Parallel Architectures and Compilation Techniques (PACT) 2021</i>. <a href="https://doi.org/10.1109/PACT52795.2021.00022" target="_blank">doi:10.1109/PACT52795.2021.00022</a>'
---
De novo assembly of genomes for which there is no reference, is essential for novel species discovery and metagenomics. In this work, we accelerate two key performance bottlenecks of DBG-based assembly, graph construction and graph traversal, with a near-data processing (NDP) architecture based on 3D-stacking. The proposed framework distributes key operations across NDP cores to exploit a high degree of parallelism and high memory bandwidth. We propose several optimizations based on domain-specific properties to improve the performance of our design. We integrate the proposed techniques into an existing DBG assembly tool, and our simulation-based evaluation shows that the proposed NDP implementation can improve the performance of graph construction by 33× and traversal by 16× compared to the state-of-the-art.
