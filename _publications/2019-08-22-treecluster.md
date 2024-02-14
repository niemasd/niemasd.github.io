---
title: "TreeCluster: Clustering biological sequences using phylogenetic trees"
collection: publications
pubtype: paper
permalink: /publication/2019-08-22-treecluster
date: 2019-08-22
venue: 'PLoS ONE'
paperurl: 'https://doi.org/10.1371/journal.pone.0221068'
citation: 'Balaban M, <b>Moshiri N</b>, Mai U, Jia X, Mirarab S (2019). "TreeCluster: Clustering biological sequences using phylogenetic trees." <i>PLoS ONE</i>. 14(8):e0221068. <a href="https://doi.org/10.1371/journal.pone.0221068" target="_blank">doi:10.1371/journal.pone.0221068</a>'
---
Clustering homologous sequences based on their similarity is a problem that appears in many bioinformatics applications. The fact that sequences cluster is ultimately the result of their phylogenetic relationships. Despite this observation and the natural ways in which a tree can define clusters, most applications of sequence clustering do not use a phylogenetic tree and instead operate on pairwise sequence distances. Due to advances in large-scale phylogenetic inference, we argue that tree-based clustering is under-utilized. We define a family of optimization problems that, given an arbitrary tree, return the minimum number of clusters such that all clusters adhere to constraints on their heterogeneity. We study three specific constraints, limiting (1) the diameter of each cluster, (2) the sum of its branch lengths, or (3) chains of pairwise distances. These three problems can be solved in time that increases linearly with the size of the tree, and for two of the three criteria, the algorithms have been known in the theoretical computer scientist literature. We implement these algorithms in a tool called TreeCluster, which we test on three applications: OTU clustering for microbiome data, HIV transmission clustering, and divide-and-conquer multiple sequence alignment. We show that, by using tree-based distances, TreeCluster generates more internally consistent clusters than alternatives and improves the effectiveness of downstream applications. TreeCluster is available at [https://github.com/niemasd/TreeCluster](https://github.com/niemasd/TreeCluster).
