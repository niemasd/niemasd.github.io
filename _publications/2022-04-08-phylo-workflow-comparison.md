---
title: "An Evaluation of Phylogenetic Workflows in Viral Molecular Epidemiology"
collection: publications
pubtype: paper
permalink: /publication/2022-04-08-phylo-workflow-comparison
date: 2022-04-08
venue: 'Viruses'
paperurl: 'https://doi.org/10.3390/v14040774'
citation: 'Young C, Meng S, <b>Moshiri N</b> (2022). "An Evaluation of Phylogenetic Workflows in Viral Molecular Epidemiology." <i>Viruses</i>. 14(4):774. <a href="https://doi.org/10.3390/v14040774" target="_blank">doi:10.3390/v14040774</a>'
---
The use of viral sequence data to inform public health intervention has become increasingly common in the realm of epidemiology. Such methods typically utilize multiple sequence alignments and phylogenies estimated from the sequence data. Like all estimation techniques, they are error prone, yet the impacts of such imperfections on downstream epidemiological inferences are poorly understood. To address this, we executed multiple commonly used viral phylogenetic analysis workflows on simulated viral sequence data, modeling Human Immunodeficiency Virus (HIV), Hepatitis C Virus (HCV), and Ebolavirus, and we computed multiple methods of accuracy, motivated by transmission-clustering techniques. For multiple sequence alignment, MAFFT consistently outperformed MUSCLE and Clustal Omega, in both accuracy and runtime. For phylogenetic inference, FastTree 2, IQ-TREE, RAxML-NG, and PhyML had similar topological accuracies, but branch lengths and pairwise distances were consistently most accurate in phylogenies inferred by RAxML-NG. However, FastTree 2 was the fastest, by orders of magnitude, and when the other tools were used to optimize branch lengths along a fixed FastTree 2 topology, the resulting phylogenies had accuracies that were indistinguishable from their original counterparts, but with a fraction of the runtime.
