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
python src/ndb_data/construction/make_database_initial.py work/kelm_cache/ work/newdbs/25 --num_dbs_to_make 10000 --sample_rels 1 --sample_per_rel 16 --sample_extra 1
python src/ndb_data/construction/make_database_initial.py work/kelm_cache/ work/newdbs/50 --num_dbs_to_make 5000 --sample_rels 1 --sample_per_rel 16 --sample_extra 2
python src/ndb_data/construction/make_database_initial.py work/kelm_cache/ work/newdbs/100 --num_dbs_to_make 2500 --sample_rels 2 --sample_per_rel 16 --sample_extra 2
python src/ndb_data/construction/make_database_initial.py work/kelm_cache/ work/newdbs/250 --num_dbs_to_make 1000 --sample_rels 2 --sample_per_rel 32 --sample_extra 3
python src/ndb_data/construction/make_database_initial.py work/kelm_cache/ work/newdbs/500 --num_dbs_to_make 500 --sample_rels 2 --sample_per_rel 64 --sample_extra 4
python src/ndb_data/construction/make_database_initial.py work/kelm_cache/ work/newdbs/1000 --num_dbs_to_make 250 --sample_rels 2 --sample_per_rel 128 --sample_extra 4
