# Neural Database Training Dataset Generation from KELM

This repository generates training instances for the NDB training dataset from templates over facts mapped from KELM.


## 1. KELM Mapping

**Deprecation warning** The `map_kelm.py` script in this repo is deprecated and has been moved into the `kelm-wikidata` model. 
In this repo, only the first reference fact is used. This can be used to replicate the ACL2021 submissions.

For these scripts, set the following environment variables to point the database containing the Wikidata facts 
(see the `kelm-wikidata` repo for the instructions on how to set up Mongo)

```
MONGO_USER=
MONGO_PASSWORD=
MONGO_HOST=
MONGO_PORT=
MONGO_DB=
```

The [KELM-wikidata repo](https://github.com/fairinternal/kelm-wikidata) maps the KELM data from this [GitHub repo](https://github.com/google-research-datasets/KELM-corpus) to a
snapshot from Wikidata. About 90% of sentences from KELM are grounded with Wikidata identifiers.
KELM uses a seq2seq model to _verbalize_ knowledge graph triples as sentences.

* [Use this repo to map from KELM: https://github.com/fairinternal/kelm-wikidata](https://github.com/fairinternal/kelm-wikidata) 


There are two steps here:
1. Generate all hypotheses input `kelm_file.jsonl` output file `hypothesis_file.jsonl`.
   It would beneficial to split the kelm file into chunks of about 100000 instances or so and run lots of these in parallel. 
   
   This script maps entity names to all matching entity IDs. Where there are multiple matching IDs, they will be resolved at a later stage. 
   This doesn't consider any of the relations present in the entity.
    
    ```
    python src/dataset_generation/generation/map_kelm.py kelm_file.jsonl hypothesis_file.jsonl error_file.jsonl
    ```
2. Finalize the hypotheses, for each generated hypothesis, build S,R,O triples.
   For each of the S,R,O triples, this will check if it exists in the mongoDB. if not it will drop it.
   
   ```
   python src/dataset_generation/generation/finalize_kelm.py hypothesis_file.jsonl out.jsonl
   ``` 



 
## 2. Question Generation

Question generation is done in a few stages. For the ACL experiments, the data has been checkpointed as `v1.8` in Google Drive. 
The generated questions are asked over KELM data. For experiments since ACL, the dataset is checkpointed as v2. V1 datasets use the old (deprecated) KELM mapping that only considers the first tuple in the reference sentence. In contrast v2 considers all.

The question generation in V2 uses a different sampling method to V1 (tagged as `acl-submission`).

### 2.1 Build Initial Database
Sample the initial set of facts for the databases. The first half of this is slow as it needs to cache all the subjects and entities in KELM.
This could be done faster with splitting KELM into smaller chunks and aggregatign the results.

With all the subjects objects and relations, this file generates a split of the subjects into train dev and test and outputs 3 files. One for each split.

```
python src/dataset_creation/v2/make_database_initial.py kelm_file.jsonl out_file_prefix
```

This picks a random relation, then picks facts participating in this relation to add to the database. 

Other args:
```
    --num_dbs_to_make # How many databases to make (50,000). 
    --sample_rels # How many relations to sample per database (2)
    --sample_per_rel # How many entities to sample per relation (10)
    --sample_extra # How many to randomly sample
```

### 2.2 Finalize Database
This step then adds relations one-hop away from the facts in the database. This requires importing KELM and Wikidata into MongoDB (use the `dataset_creation/extraction/kelm_data.py` script).

This queries the KELM dataset to find facts which share entities and with what's in the DB.

This step will also normalize the facts in the database as KELM can often butcher the names of entities which break the scoring.

This will drop facts if there are too many, this file can be used to set the size of the database.

```
python src/dataset_creation/v2/make_database_finalize.py [out_file_prefix]_train second_phase_train.jsonl
python src/dataset_creation/v2/make_database_finalize.py [out_file_prefix]_dev second_phase_dev.jsonl
python src/dataset_creation/v2/make_database_finalize.py [out_file_prefix]_test second_phase_test.jsonl
``` 

### 2.3 Generate Questions
This takes the facts in the database and generates questions accordingly. This will also generate complex questions.

```
python src/dataset_creation/v2/make_questions.py second_phase_train.jsonl questions_train.jsonl
python src/dataset_creation/v2/make_questions.py second_phase_dev.jsonl questions_dev.jsonl
python src/dataset_creation/v2/make_questions.py second_phase_test.jsonl questions_test.jsonl
``` 

### 2.4 Stratified Sample Queries
The quesiton generation script will generate all questions for every query which is heavily imbalanced. This balancing performs a multi-variate stratified sample over binned support sets and tries to get a uniform distribution over support set size. 
```
python src/dataset_creation/v2/make_questions.py questions_train.jsonl balanced_train.jsonl
python src/dataset_creation/v2/make_questions.py questions_dev.jsonl balanced_dev.jsonl
python src/dataset_creation/v2/make_questions.py questions_test.jsonl balanced_test.jsonl
``` 

### 2.5 Subsample Databases
The above dataset can take a long time to train (12 hours per epoch on 8 GPUs) and may take a couple of hours to load the dataset.

To speed up training, we used 10% and 25% of the dataset, just by taking the first N databases.

```
head -n 5000 balanced_train.jsonl > train_10.jsonl
head -n 500 balanced_dev.jsonl > dev_10.jsonl
head -n 500 balanced_test.jsonl > test_10.jsonl
```