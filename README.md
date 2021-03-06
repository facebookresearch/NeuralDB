# Database Reasoning over Text

This repository contains the code for the [Database Reasoning Over Text](https://arxiv.org/pdf/2106.01074.pdf) paper, 
to appear at ACL2021. Work is performed in collaboration with James Thorne, Majid Yazdani, Marzieh Saeidi, Fabrizio Silvestri, Sebastian Riedel, and Alon Halevy.


![Overview Image](overview.png)


## Data
The completed NeuralDB datasets can be downloaded [here](https://dl.fbaipublicfiles.com/neuraldb/fb-data-WikiNLDB.zip) and are released under a [CC BY-SA 3.0 license](https://creativecommons.org/licenses/by-sa/2.0/). 

The dataset includes entity names from Wikidata which are released under a [CC BY-SA 3.0 license](https://creativecommons.org/licenses/by-sa/3.0/).
This dataset includes sentences from the KELM corpus. KELM is released under the [CC BY-SA 2.0 license](https://creativecommons.org/licenses/by-sa/2.0/)


## Repository Structure
The repository is structured in 3 sub-folders:

* Tools for mapping the KELM data to Wikidata identifiers are provided in the [dataset construction](dataset-construction/) folder ,
* The information retrieval system for the support set generator are provided in the [ssg](ssg/) folder
* The models for Neural SPJ, the baseline retrieval (TF-IDF and DPR), and evaluation scripts are provided in the [modelling folder](modelling/).

Instructions for running each component are provided in the README files in the respective sub-folders.

## Setup

All sub-folders were set up with one Python environment per folder. Requirements for each environment can be installed by
running a pip install:

```
pip install -r requirements.txt
```

In the `dataset-construction` and `modelling` folders, the `src` folder should be included in the python path.

```
export PYTHONPATH=src
```

## License

The code in this repository is released under the [Apache 2.0 license](LICENSE)
