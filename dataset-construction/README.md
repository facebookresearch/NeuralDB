# Neural Database Training Dataset Generation from KELM

This repository generates training instances for the NDB training dataset from templates over facts mapped from KELM. 

In some scripts, the KELM mappings and Wikidata graph are used. These assume that they have been loaded into a MongoDB database.
Set the following environment variables to point the scripts to the appropriate the database:


```
MONGO_USER=
MONGO_PASSWORD=
MONGO_HOST=
MONGO_PORT=
MONGO_DB=
```

## 1. Load data into database


_The method for restoring the mapping between facts in the KELM and Wikidata IDs should now be considered as deprecated as the authors of KELM have now released the original mapping data._


### 1.1 Wikidata
Wikidata can be imported to the MongoDB using the `wikidata_index.py` script, however this takes a few days to unzip, import and index.
The easiest option is to restore a dump of the mongo database instead. The dump can be downloaded from [Google Drive](https://drive.google.com/file/d/1A3pwl3ZGR2QT-5IzMp_fV4g1Qlvbmtc7/view?usp=sharing) and is released under a CC BY-SA 3.0 license.

```
mongorestore --archive --gzip < mongo_wikidata_dump.gz
```

All indexes should be generated on restoring the DB. But failing this, the following indexes should be created for the wiki_graph collection:
`wikidata_id, english_name, english_wiki, sitelinks.title ` and the following indexes for wiki_redirect collection `title`

### 1.2 KELM
Importing the mappings from KELM is quite fast and is done through running the `kelm_data.py` script

```
python -m ndb_data.data_import.kelm_data <path_to_mapped_kelm>.jsonl
```

After importing, the following indexes should be created: `entities, relations, (entities, relations)`


## 2. Dataset construction

Question and answer generation is done in a few stages using the data from KELM For the ACL experiments. The data has been checkpointed and released with the version identified `v2.4` for the ACL paper.

The exact choices used for the ACL paper are stored in bash scripts in the `scripts/` folder.

### 2.1 Build Initial Database
Sample the initial set of facts for the databases. The first half of this is slow as it needs to cache all the subjects and entities in KELM.
This could be done faster with splitting KELM into smaller chunks and aggregating the results.

Firstly, we need to cache the subjects/entities/relations as indexing these takes a while and these can be re-used:

```
python -m ndb_data.construction.make_database_initial_cache kelm_file.jsonl
```

With all the subjects objects and relations, this file generates a split of the subjects into train dev and test and outputs 3 files. One for each split.

```
python -m ndb_data.construction.make_database_initial kelm_file.jsonl out_file_prefix
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
python -m ndb_data.construction.make_database_finalize [out_file_prefix]_train second_phase_train.jsonl
python -m ndb_data.construction.make_database_finalize [out_file_prefix]_dev second_phase_dev.jsonl
python -m ndb_data.construction.make_database_finalize [out_file_prefix]_test second_phase_test.jsonl
``` 

### 2.3 Generate Questions
This takes the facts in the database and generates questions accordingly. This will also generate complex questions.

```
python -m ndb_data.construction.make_questions second_phase_train.jsonl questions_train.jsonl
python -m ndb_data.construction.make_questions second_phase_dev.jsonl questions_dev.jsonl
python -m ndb_data.construction.make_questions second_phase_test.jsonl questions_test.jsonl
``` 

### 2.4 Stratified Sample Queries
The question generation script will generate all questions for every query which is heavily imbalanced. This balancing performs a multi-variate stratified sample over binned support sets and tries to get a uniform distribution over support set size. 
```
python -m ndb_data.sample_questions questions_train.jsonl balanced_train.jsonl
python -m ndb_data.sample_questions questions_dev.jsonl balanced_dev.jsonl
python -m ndb_data.sample_questions questions_test.jsonl balanced_test.jsonl
``` 

### v2.5 [extra step for small databases]: Filter databases of more than 900 tokens

For the baseline experiments, we filter out databases containing more than 900 tokens to evaluate databases that can be encoded within a standard transformer model under the 1024 token limit.

```
python -m ndb_data.generation.fiter_db_facts in_folder/ out_folder/
```
