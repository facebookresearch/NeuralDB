## Setup 

Installing: 

```
conda create -n neuraldb python=3.8
conda activate neuraldb

pip install -r requirements.txt 
```

Set Python path to include the following directories:

```
export PYTHONPATH=src:abstractive-models:extractive-models
```

(Outdated)
If torch doesn't work, use a specific build for the cuda version:

```bash
pip uninstall torch
conda install pytorch cudatoolkit=10.1 -c pytorch
```


