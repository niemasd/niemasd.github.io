---
title: "QPL-Enabled HTSlib Library: Accelerating Sequence File Compression using Intel IAA"
collection: publications
pubtype: paper
permalink: /publication/2026-08-25-qpl-htslib
date: 2026-08-25
venue: 'Bioinformatics Advances'
paperurl: 'https://doi.org/10.1093/bioadv/vbag250'
citation: 'Laflen B, Li Z, Urbina M, Rosing T, <b>Moshiri N</b> (2026). "QPL-Enabled HTSlib Library: Accelerating Sequence File Compression using Intel IAA." <i>Bioinformatics Advances</i>. vbag250. <a href="https://doi.org/10.1093/bioadv/vbag250" target="_blank">doi:10.1093/bioadv/vbag250</a>'
---
Sequence analysis workflows require the accessibility of large datasets, which require state-of-the-art compression tools. These compression tools, such as Samtools, often rely on HTSlib as a GZip implementation, but are still limited by throughput on time-intensive compression. QPL-HTSLib offers order of magnitude speedups for the compression and decompression of the SAM and BAM file formats commonly used in genomics workflows at the cost of a slightly larger compressed file, and is a drop-in replacement for HTSlib on Intel systems.
