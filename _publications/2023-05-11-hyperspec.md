---
title: "HyperSpec: Ultrafast Mass Spectra Clustering in Hyperdimensional Space"
collection: publications
pubtype: paper
permalink: /publication/2023-05-11-hyperspec
excerpt: 'HyperSpec: Ultrafast Mass Spectra Clustering in Hyperdimensional Space'
date: 2023-05-11
venue: 'Journal of Proteome Research'
paperurl: 'https://doi.org/10.1021/acs.jproteome.2c00612'
citation: 'Xu W, Kang J, Bittremieux W, <b>Moshiri N</b>, Rosing T (2023). "HyperSpec: Ultrafast Mass Spectra Clustering in Hyperdimensional Space." <i>Journal of Proteome Research</i>. 22(6):1639–1648. <a href="https://doi.org/10.1021/acs.jproteome.2c00612" target="_blank">doi:10.1021/acs.jproteome.2c00612</a>'
---
As current shotgun proteomics experiments can produce gigabytes of mass spectrometry data per hour, processing these massive data volumes has become progressively more challenging. Spectral clustering is an effective approach to speed up downstream data processing by merging highly similar spectra to minimize data redundancy. However, because state-of-the-art spectral clustering tools fail to achieve optimal runtimes, this simply moves the processing bottleneck. In this work, we present a fast spectral clustering tool, HyperSpec, based on hyperdimensional computing (HDC). HDC shows promising clustering capability while only requiring lightweight binary operations with high parallelism that can be optimized using low-level hardware architectures, making it possible to run HyperSpec on graphics processing units to achieve extremely efficient spectral clustering performance. Additionally, HyperSpec includes optimized data preprocessing modules to reduce the spectrum preprocessing time, which is a critical bottleneck during spectral clustering. Based on experiments using various mass spectrometry data sets, HyperSpec produces results with comparable clustering quality as state-of-the-art spectral clustering tools while achieving speedups by orders of magnitude, shortening the clustering runtime of over 21 million spectra from 4 h to only 24 min.
