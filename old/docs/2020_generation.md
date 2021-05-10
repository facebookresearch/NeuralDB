
## NUO dataset generation

The NUO dataset can be generated from Wikidata. There's a few different versions, [described in this document](https://docs.google.com/document/d/1KD0hIi6NYfYzErldw2nj--H2skafmc_0zImcwphO-Gs/edit), [generated using these templates](https://docs.google.com/document/d/1qljPmDoYieA33UWEK3kZ4ZzS80LNalXbl7XHR4jQsck/edit)

There's several steps to generate the dataset: 

1) Build the template JSONs from the config CSV
2) Extract data from Wikidata
3) Resolve Wikidata IDs
4) Generate Negative Instances
5) Replace entities (substitute Wikidata IDs for canonical names)
6) Generate E2E-style DB from NUO and hard-sample

Commands 

Build the template JSON
```bash
export PYTHONPATH=src
python -m neuraldb.generation.build_json v1.4
```

Extract templates from Wikidata

```bash
export PYTHONPATH=src 
python -m neuraldb/generation/operator_wikidata /path/to/wikidata-latest.json.bz2 configs/generate_v1.4.json --complete
```

Resolve entity names from Wikidata (or the service if not in first 100k entities)

```bash
export PYTHONPATH=src
python -m neuraldb.generation.resolve_entities
```

Generate Negatives:

```bash
export PYTHONPATH=src
python -m neuraldb.generation.generate_negatives
```

Replace entity names:

```bash
export PYTHONPAT=src
python -m neuraldb.generation.replace_entities
```

Once these have been run, there will be several JSON files that should be moved into a folder for that dataset:

```bash
#example
mkdir v1.0
mv generated* v1.0
