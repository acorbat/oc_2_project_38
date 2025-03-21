<p align="center">
  <a href="https://ai4life.eurobioimaging.eu/open-calls/">
    <img src="https://github.com/ai4life-opencalls/.github/blob/main/AI4Life_banner_giraffe_nodes_OC.png?raw=true" width="70%">
  </a>
</p>


# Project #38: Neuroscan
## A 3D human motor neuron disease platform for high throughput drug screening

[![DOI](https://zenodo.org/badge/DOI/)](https://doi.org/)


---
This page was created by the [AI4Life project](https://ai4life.eurobioimaging.eu) using data provided by Katharina Hennig at [Institute of Molecular Medicine](https://imm.medicina.ulisboa.pt/) (now [Gulbenkian Institute for Molecular Medicine](https://gimm.pt/)). 
All the images demonstrated in this tutorial are provided under **CC-BY** licence.

If any of the instructions are not working, please [open an issue](https://github.com/ai4life-opencalls/oc-2-project-38/issues) or contact us at [ai4life@fht.org](ai4life@fht.org)! 

**Project challenges**: cell instance segmentation.

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Rationale](#rationale)
5. [Conclusion](#conclusion)

# Introduction

A 3D human motor neuron disease platform for high throughput drug screening.
The goal of this package is to load the 3D images acquired of neurospheres and segment nuclei and Islet1 positive nuclei from their respective channels.

## Installation

Install the [conda](https://conda.io) package, dependency and environment manager.

You can download this repository from the green `Code` button and download and zip, or through the command line with

    cd <path to any folder of choice>
    git clone https://github.com/BIIFSweden/AI4Life_OC2_2024_38.git

Then create the `neuroscan` conda environment:

    cd <path to your 'AI4Life_OC2_2024_38' directory>
    conda env create -f environment.yml

This will install all necessary project dependencies as well as the `neuroscan` companion package (editable install).

## Usage

Copy all project data to the [data](data) directory (or use symbolic links).

Then run [Jupyter Lab](https://jupyter.org) from within the `neuroscan` conda environment:

    cd <path to your 'AI4Life_OC2_2024_38' directory>
    conda activate neuroscan
    jupyter-lab

All analysis notebooks can be found in the [notebooks](notebooks) directory.

Or you can use the following command to analyze a folder.

    conda activate neuroscan
    neuroscan segment <path to folder>

This will add two TIFF labeled images containing the instance segmentation for nuclei and motor neurons in separate files.

## Rationale

Should you want to delve deeper into how the pipeline was developed, please go to the `notebooks` folder.
You can find three notebooks.
The [data_loading.ipynb](notebooks/data_loading.ipynb) describes how images are loaded.
The [nuclei_segmentation.ipynb](notebooks/nuclei_segmentation.ipynb) describes how nuclei are segmented from the nuclei channel.
The [motor_segmentation.ipynb](notebooks/motor_segmentation.ipynb) describes how motor neurons are segmented from the motor neuron channel.

## Conclusion

[AI4Life](https://ai4life.eurobioimaging.eu)  is a Horizon Europe-funded project that brings together the computational and life science communities.

AI4Life has received funding from the European Union’s Horizon Europe research and innovation programme under grant agreement number 101057970. Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Council Executive Agency. Neither the European Union nor the granting authority can be held responsible for them.

## Support

If you find a bug, please [raise an issue](https://github.com/BIIFSweden/AI4Life_OC2_2024_38/issues/new).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors

[SciLifeLab BioImage Informatics Facility (BIIF)](https://biifsweden.github.io) project lead: Agustin Corbat

Data acquisition: [Katharina Hennig](https://orcid.org/0000-0003-4655-1185), [Afonso Malheiro](https://orcid.org/0000-0001-9062-1051), [Edgar R. Gomes](https://orcid.org/0000-0002-6941-4872)

## License

[MIT](LICENSE)
