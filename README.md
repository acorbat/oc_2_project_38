# AI4Life_OC2_2024_38 NeuroScan

A 3D human motor neuron disease platform for high throughput drug screening

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

## Support

If you find a bug, please [raise an issue](https://github.com/BIIFSweden/AI4Life_OC2_2024_38/issues/new).

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Authors

[SciLifeLab BioImage Informatics Facility (BIIF)](https://biifsweden.github.io) project lead: Agustin Corbat

## License

[MIT](LICENSE)
