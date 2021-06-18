##
## Copyright (c) 2021 Facebook, Inc. and its affiliates.
##
## This file is part of NeuralDB.
## See https://github.com/facebookresearch/NeuralDB for further info.
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##     http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
##
mkdir -pv work/newdbs

python src/ndb_data/construction/make_database_initial.py work/kelm_cache/ work/newdbs/25 --num_dbs_to_make 1000 --sample_rels 1 --sample_per_rel 16 --sample_extra 2
python src/ndb_data/construction/make_database_finalize.py work/newdbs/25_train work/newdbs/intermediate_train_25.jsonl --target-size 25
python src/ndb_data/construction/make_database_finalize.py work/newdbs/25_dev work/newdbs/intermediate_dev_25.jsonl --target-size 25
python src/ndb_data/construction/make_database_finalize.py work/newdbs/25_test work/newdbs/intermediate_test_25.jsonl --target-size 25


python src/ndb_data/construction/make_database_initial.py work/kelm_cache/ work/newdbs/50 --num_dbs_to_make 500 --sample_rels 1 --sample_per_rel 16 --sample_extra 2
python src/ndb_data/construction/make_database_finalize.py work/newdbs/50_train work/newdbs/intermediate_train_50.jsonl --target-size 50
python src/ndb_data/construction/make_database_finalize.py work/newdbs/50_dev work/newdbs/intermediate_dev_50.jsonl --target-size 50
python src/ndb_data/construction/make_database_finalize.py work/newdbs/50_test work/newdbs/intermediate_test_50.jsonl --target-size 50


python src/ndb_data/construction/make_database_initial.py work/kelm_cache/ work/newdbs/100 --num_dbs_to_make 250 --sample_rels 2 --sample_per_rel 16 --sample_extra 2
python src/ndb_data/construction/make_database_finalize.py work/newdbs/50_train work/newdbs/intermediate_train_100.jsonl --target-size 100
python src/ndb_data/construction/make_database_finalize.py work/newdbs/50_dev work/newdbs/intermediate_dev_100.jsonl --target-size 100
python src/ndb_data/construction/make_database_finalize.py work/newdbs/50_test work/newdbs/intermediate_test_100.jsonl --target-size 100

python src/ndb_data/construction/make_database_initial.py work/kelm_cache/ work/newdbs/250 --num_dbs_to_make 100 --sample_rels 2 --sample_per_rel 32 --sample_extra 3
python src/ndb_data/construction/make_database_finalize.py work/newdbs/50_train work/newdbs/intermediate_train_250.jsonl --target-size 250
python src/ndb_data/construction/make_database_finalize.py work/newdbs/50_dev work/newdbs/intermediate_dev_250.jsonl --target-size 250
python src/ndb_data/construction/make_database_finalize.py work/newdbs/50_test work/newdbs/intermediate_test_250.jsonl --target-size 250

python src/ndb_data/construction/make_database_initial.py work/kelm_cache/ work/newdbs/500 --num_dbs_to_make 50 --sample_rels 3 --sample_per_rel 40 --sample_extra 4
python src/ndb_data/construction/make_database_finalize.py work/newdbs/50_train work/newdbs/intermediate_train_250.jsonl --target-size 500
python src/ndb_data/construction/make_database_finalize.py work/newdbs/50_dev work/newdbs/intermediate_dev_250.jsonl --target-size 500
python src/ndb_data/construction/make_database_finalize.py work/newdbs/50_test work/newdbs/intermediate_test_250.jsonl --target-size 500

python src/ndb_data/construction/make_database_initial.py work/kelm_cache/ work/newdbs/1000 --num_dbs_to_make 25 --sample_rels 3 --sample_per_rel 50 --sample_extra 4
python src/ndb_data/construction/make_database_finalize.py work/newdbs/50_train work/newdbs/intermediate_train_250.jsonl --target-size 1000
python src/ndb_data/construction/make_database_finalize.py work/newdbs/50_dev work/newdbs/intermediate_dev_250.jsonl --target-size 1000
python src/ndb_data/construction/make_database_finalize.py work/newdbs/50_test work/newdbs/intermediate_test_250.jsonl --target-size 1000



bash scripts/make_databases.sh 50;
bash scripts/make_databases.sh 100;
bash scripts/make_databases.sh 250;
bash scripts/make_databases.sh 500;
bash scripts/make_databases.sh 1000;

bash scripts/make_questions.sh 50;
bash scripts/make_questions.sh 100;
bash scripts/make_questions.sh 250;
bash scripts/make_questions.sh 500;
bash scripts/make_questions.sh 1000;