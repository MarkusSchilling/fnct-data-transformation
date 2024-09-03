# FNCT Data Transformation

This repository hosts a set of Python scripts developed to streamline the processing and semantic integration of Full-Notch Creep Test ([FNCT](https://www.iso.org/standard/70480.html)) data. The scripts are provided as [Jupyter Notebooks](https://jupyter.org/) (ipynb files). FNCT is a critical method used to assess the slow crack growth (SCG) and environmental stress cracking (ESC) resistance of polymers, particularly polyolefins like high-density polyethylene (PE-HD) - see [Literature](#Literature) section for more details.

## Overview

The scripts transform raw and manually entered/added FNCT data into organized data stored using a standardized vocabulary. This process leads to the creation of data aligned with the FAIR principles (Findable, Accessible, Interoperable, and Reusable) and therefore enhances data interoperability and prepares them for further automated analysis. Moreover, the conversion of raw FNCT data into semantically enriched formats, such as RDF, is facilitated. For the creation of semantic integrated FNCT data, the [OntoFNCT framework](https://github.com/MarkusSchilling/ontoFNCT) may be used. The transformation workflow includes the following key steps:

1. **Folder Setup**: Automatically organizes directories for primary data, metadata, and secondary data.
2. **Excel File Processing**: Converts raw FNCT data from Excel files into CSV format, ensuring data integrity and preventing overwrites.
3. **Secondary Data Aggregation**: Combines and processes secondary data from multiple sources into a unified CSV file, including key metrics calculations like final elongation and residual fracture surface based on available information.
4. **Metadata Integration**: Extracts and stores metadata separately, capturing essential test information for traceability.


### Example Data

Besides the scripts, some example FNCT data stemming from FNCT experiments performed at Bundesanstalt für Materialforschung und -prüfung ([BAM](https://www.bam.de/Navigation/EN/Home/home.html)), Berlin, Germany, are provided in the [example data](https://github.com/MarkusSchilling/fnct-data-transformation/blob/main/example_data) folder in this repository. This data regarded is also available in the open Zenodo repository [Dataset of comprehensive Full-notch creep tests (FNCT) of selected high-density polyethylene (PE-HD) materials](https://doi.org/10.5281/zenodo.10143352).

## Getting Started

The scripts are designed to be user-friendly, with built-in checks for folder existence and overwrite protection to safeguard data integrity. For researchers and test operators, this provides an efficient way to prepare FNCT data for further analysis or semantic integration without the need for extensive manual data handling. In particular, files that can be saved and examined step by step are created so that the overall process is traceable and not all scripts have to be executed. Depending on the requirements, only parts of the scripts can be executed (not the entire pipeline, if applicable). It is also possible and desirable to adapt the scripts to your own requirements.

## Requirements

- Python 3.x
- Libraries: `pandas`, `numpy`, `rdflib`

## License

This repository is open-source and available under the [MIT License](https://github.com/MarkusSchilling/fnct-data-transformation/blob/main/LICENSE).

## Literature

For more details on the scripts presented in this repository and when using those, please refer to 

*M. Schilling, N. Marschall, U. Niebergall, M. Böhning, TBD.*

Bibtex:
```
@article{Schilling2024,
   author = {Schilling, Markus and Marschall, Niklas and Niebergall, Ute and Boehning, Martin},
   title = {Modernizing FNCT Data Handling in Polymer Labs: Towards Efficient Management},
   journal = {Polymer},
   pages = {},
   ISSN = {},
   DOI = {},
   url = {},
   year = {2024},
   type = {Journal Article}
}
```
available open access at: [Polymer]().

A dataset comprising example FNCT data can be found in the open Zenodo repository named [Dataset of comprehensive Full-notch creep tests (FNCT) of selected high-density polyethylene (PE-HD) materials (2023)](https://doi.org/10.5281/zenodo.10143351).

For more details on digitalization efforts in the field of materials science and engineering (MSE) and the FNCT, the following literature may be considered.

### Digitalization in MSE

- [FAIR and Structured Data: A Domain Ontology Aligned with Standard-compliant Tensile Testing (2024)](https://doi.org/10.1002/adem.202400138)
- [PMD Core Ontology: Achieving semantic interoperability in materials science (2024)](https://doi.org/10.1016/j.matdes.2023.112603)
- [Semantic integration of diverse data in materials science: Assessing Orowan strengthening (2024)](https://doi.org/10.1038/s41597-024-03169-4)
- [Ontopanel: A Tool for Domain Experts Facilitating Visual Ontology Development and Mapping for FAIR Data Sharing in Materials Testing (2022)](https://doi.org/10.1007/s40192-022-00279-y)
- [A Perspective on Digital Knowledge Representation in Materials Science and Engineering (2022)](https://doi.org/10.1002/adem.202101176)


### FNCT

- [Characteristics of Environmental Stress Cracking of PE-HD induced by Biodiesel and Diesel Fuels (2024)](https://doi.org/10.1016/j.polymertesting.2024.108547)
- [Relation of craze to crack length during slow crack growth phenomena in high-density polyethylene (2024)](https://doi.org/10.1002/pen.26698)
- [A phenomenological criterion for an optical assessment of PE-HD fracture surfaces obtained from FNCT (2021)](https://doi.org/10.1016/j.polymertesting.2020.107002)
- [Crack propagation in PE-HD induced by environmental stress cracking (ESC) analyzed by several imaging techniques (2018)](https://doi.org/10.1016/j.polymertesting.2018.08.014)
- [Full notch creep test (FNCT) of PE-HD – Characterization and differentiation of brittle and ductile fracture behavior during environmental stress cracking (ESC) (2017)](http://dx.doi.org/10.1016/j.polymertesting.2017.09.043)