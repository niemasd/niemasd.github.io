---
title: "An Evaluation of Phylogenetic Workflows in Viral Molecular Epidemiology"
collection: publications
pubtype: conference
permalink: /publication/2021-05-05-phylo-workflow-comparison-dynamics
date: 2021-05-05
venue: '28th International Dynamics & Evolution of Human Viruses'
citation: 'Young C, Meng S, <b>Moshiri N</b> (2021). "An Evaluation of Phylogenetic Workflows in Viral Molecular Epidemiology." <i>28th International Dynamics & Evolution of Human Viruses</i>. Poster.'
---
The use of viral sequence data to inform public health intervention has become increasingly common in the realm of epidemiology. Such methods typically utilize multiple sequence alignments and phylogenies estimated from the sequence data. Like all estimation techniques, they are error prone, yet the impacts of such imperfections on downstream epidemiological inferences are poorly understood. To address this, we executed multiple commonly used viral phylogenetic analysis workflows on simulated viral sequence data, modeling Human Immunodeficiency Virus (HIV), Hepatitis C Virus (HCV), and Ebolavirus, and we computed multiple methods of accuracy, motivated by transmission-clustering techniques. For multiple sequence alignment, MAFFT consistently outperformed MUSCLE and Clustal Omega, in both accuracy and runtime. For phylogenetic inference, FastTree 2, IQ-TREE, RAxML-NG, and PhyML had similar topological accuracies, but branch lengths and pairwise distances were consistently most accurate in phylogenies inferred by RAxML-NG. However, FastTree 2 was the fastest, by orders of magnitude, and when the other tools were used to optimize branch lengths along a fixed FastTree 2 topology, the resulting phylogenies had accuracies that were indistinguishable from their original counterparts, but with a fraction of the runtime.
