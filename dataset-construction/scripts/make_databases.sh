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
size=$1
python src/ndb_data/construction/make_database_finalize.py work/newdbs/${size}_train work/newdbs/intermediate_train_${size}.jsonl --target-size ${size}
python src/ndb_data/construction/make_database_finalize.py work/newdbs/${size}_dev work/newdbs/intermediate_dev_${size}.jsonl --target-size ${size}
python src/ndb_data/construction/make_database_finalize.py work/newdbs/${size}_test work/newdbs/intermediate_test_${size}.jsonl --target-size ${size}