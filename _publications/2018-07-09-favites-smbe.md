---
title: "FAVITES: simultaneous simulation of transmission networks, phylogenetic trees and sequences"
collection: publications
pubtype: conference
permalink: /publication/2018-07-09-favites-smbe
excerpt: 'FAVITES: simultaneous simulation of transmission networks, phylogenetic trees and sequences'
date: 2018-07-09
venue: 'Society for Molecular Biology and Evolution (SMBE) 2018'
citation: '<b>Moshiri N</b>, Ragonnet-Cronin M, Wertheim JO, Mirarab S (2018). "FAVITES: simultaneous simulation of transmission networks, phylogenetic trees and sequences." <i>Society for Molecular Biology and Evolution (SMBE) 2018</i>. Poster.'
---
### Motivation
The ability to simulate epidemics as a function of model parameters allows insights that are unobtainable from real datasets. Further, reconstructing transmission networks for fast-evolving viruses like Human Immunodeficiency Virus (HIV) may have the potential to greatly enhance epidemic intervention, but transmission network reconstruction methods have been inadequately studied, largely because it is difficult to obtain ‘truth’ sets on which to test them and properly measure their performance.

### Results
We introduce FrAmework for VIral Transmission and Evolution Simulation (FAVITES), a robust framework for simulating realistic datasets for epidemics that are caused by fast-evolving pathogens like HIV. FAVITES creates a generative model to produce contact networks, transmission networks, phylogenetic trees and sequence datasets, and to add error to the data. FAVITES is designed to be extensible by dividing the generative model into modules, each of which is expressed as a fixed API that can be implemented using various models. We use FAVITES to simulate HIV datasets and study the realism of the simulated datasets. We then use the simulated data to study the impact of the increased treatment efforts on epidemiological outcomes. We also study two transmission network reconstruction methods and their effectiveness in detecting fast-growing clusters.

### Availability and implementation
FAVITES is available at [https://github.com/niemasd/FAVITES](https://github.com/niemasd/FAVITES), and a Docker image can be found on DockerHub ([https://hub.docker.com/r/niemasd/favites](https://hub.docker.com/r/niemasd/favites)).
