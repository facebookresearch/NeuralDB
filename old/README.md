# NeuralDB retrieval based models

Docs
* [Installation and Setup](docs/install.md)
* [Baseline data (VLDB 2020 D1)](docs/baseline_data.md)
* [Training baseline models](docs/baseline_models.md)
* [Generating data from Wikidata (VLDB 2020 D2)](docs/2020_generation.md)
* [2020: VLDB paper experiments - NeuralDB model](docs/2020_models.md)
* [Generating data from Wikidata (ACL 2021)](docs/generation.md)
* [2021: ACL paper experiments - NeuralDB model](docs/2021_models.md)

## Key Concepts

* **Generator** takes an instance, tokenizes and pads it and prepares it as input for the model (e.g. sequence to sequence vs sequence classification)
* **Reader** Reads a database.json file and generates instances from it. From v0.2-v0.5 the formatting of the JSON file is evolving. The reader provides a common interface to the model 
* **E2E** end-to-end model with multiple facts input and a single answer output
* **NUO** neural unary operator (now neural SPJ) - performs a query based derivation of a single fact
* **Search Engines** for E2E model, these are TF-IDF, BM25 and MIPS to filter the facts in the database before inputting into the model
* **Oracle Model** for E2E, only the correct facts are input
* **FID / Fusion in Decoder Model** A baseline for E2E using fusion in decoder (Gauthier Izacard's paper)

## Package Structure

```
src/
    neuraldb/                # Python package containing NeuralDB project
        commands/            # Entry points to run fine-tuning/testing
        dataset/             # Components pertaining to loading the dataset
            e2e_generator
            e2e_reader
            nuo_generator  
            search_engines 
        demo/                # Web based demonstration
        generation/          # For constructing the NUO (D2) dataset
        models/              # HuggingFace model files (mostly extending T5)
        scoring/             # Helper functions for scoring and evaluation
```


```