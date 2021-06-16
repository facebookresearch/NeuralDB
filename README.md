# Database Reasoning over Text

This repository contains the code for the [Database Reasoning Over Text](https://arxiv.org/pdf/2106.01074.pdf) paper, 
to appear at ACL2021. Work is performed in collaboration with James Thorne, Majid Yazdani, Marzieh Saeidi, Fabrizio Silvestri, Sebastian Riedel, and Alon Halevy.


![Overview Image](overview.png)


## Data
Where to download the data from the following URL:

The KELM data are released under Creative Commons Share Alike v2.0 license (CC-BY-SA 2.0)


## Repository Structure
The repository is structured in 3 sub-folders:

* Tools for mapping the KELM data to Wikidata identifiers are provided in the  [dataset construction](dataset-construction/) folder ,
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