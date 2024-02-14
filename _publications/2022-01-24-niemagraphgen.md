---
title: "NiemaGraphGen: A memory-efficient global-scale contact network simulation toolkit"
collection: publications
pubtype: paper
permalink: /publication/2022-01-24-niemagraphgen
date: 2022-01-24
venue: 'Gigabyte'
paperurl: 'https://doi.org/10.46471/gigabyte.37'
citation: '<b>Moshiri N</b> (2022). "NiemaGraphGen: A memory-efficient global-scale contact network simulation toolkit." <i>Gigabyte</i>. <a href="https://doi.org/10.46471/gigabyte.37" target="_blank">doi:10.46471/gigabyte.37</a>'
---
Epidemic simulations require the ability to sample contact networks from various random graph models. Existing methods can simulate city-scale or even country-scale contact networks, but they are unable to feasibly simulate global-scale contact networks due to high memory consumption. NiemaGraphGen (NGG) is a memory-efficient graph generation tool that enables the simulation of global-scale contact networks. NGG avoids storing the entire graph in memory and is instead intended to be used in a data streaming pipeline, resulting in memory consumption that is orders of magnitude smaller than existing tools. NGG provides a massively-scalable solution for simulating social contact networks, enabling global-scale epidemic simulation studies.
