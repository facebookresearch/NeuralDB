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
function do_predictions() {
  model_path=$1
  generator=$2
  predictions_path=$3
  tsp python src/neuraldb/run.py \
    --model_name_or_path $model_path \
    --output_dir $model_path \
    --predictions_file $model_path/predictions.jsonl \
    --do_predict --test_file resources/${predictions_path}/test.jsonl \
    --instance_generator $generator \
    --per_device_eval_batch_size 4 \
    --predict_with_generate

}

dataset=${1:-v2.4_25}
export seed=${SEED:-1}

SEED=${seed} tsp bash scripts/baselines/train_t5.sh $dataset perfectir 1e-4
SEED=${seed} tsp bash scripts/baselines/train_t5.sh $dataset wholedb 1e-4

do_predictions work/${dataset}/model=t5,generator=perfectir,lr=1e-4,steps=1/seed-${seed} perfectir ${dataset}
do_predictions work/${dataset}/model=t5,generator=wholedb,lr=1e-4,steps=1/seed-${seed} wholedb ${dataset}

SEED=${seed} tsp bash scripts/baselines/train_longformer.sh $dataset perfectir 1e-4
SEED=${seed} tsp bash scripts/baselines/train_longformer.sh $dataset wholedb 1e-4

do_predictions work/${dataset}/model=longformer,generator=perfectir,lr=1e-4,steps=1/seed-${seed} perfectir ${dataset}
do_predictions work/${dataset}/model=longformer,generator=wholedb,lr=1e-4,steps=1/seed-${seed} wholedb ${dataset}

SEED=${seed} tsp bash scripts/baselines/train_t5_retriever.sh $dataset externalir dpr 1e-4
SEED=${seed} tsp bash scripts/baselines/train_t5_retriever.sh $dataset externalir tfidf 1e-4

do_predictions work/${dataset}/model=t5,generator=externalir,retriever=dpr,lr=1e-4,steps=1/seed-${seed} externalir ${dataset}_dpr
do_predictions work/${dataset}/model=t5,generator=externalir,retriever=tfidf,lr=1e-4,steps=1/seed-${seed} externalir ${dataset}_tfidf
