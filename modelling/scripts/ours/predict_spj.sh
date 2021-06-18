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
dataset=v2.4_25

function do_predictions_spj() {
  model_path=$1
  generator=spj
  tsp python src/neuraldb/run.py \
    --model_name_or_path $model_path \
    --output_dir $model_path \
    --predictions_file $model_path/intermediate_predictions.jsonl \
    --do_predict --test_file resources/${dataset}/test.jsonl \
    --instance_generator $generator \
    --per_device_eval_batch_size 64 \
    --predict_with_generate

  tsp python src/neuraldb/convert_spj_to_predictions.py $model_path/intermediate_predictions.jsonl $model_path/predictions.jsonl
}

function do_predictions_ssg_spj() {
  model_path=$1
  out_path=$2
  generator=spj

  mkdir -pv $out_path
  tsp python src/neuraldb/run.py \
    --model_name_or_path $model_path \
    --output_dir $model_path \
    --predictions_file $out_path/intermediate_predictions.jsonl \
    --do_predict \
    --test_file resources/${dataset}_ssg/test.jsonl \
    --instance_generator $generator \
    --per_device_eval_batch_size 64 \
    --predict_with_generate

  tsp python src/neuraldb/convert_spj_to_predictions.py $out_path/intermediate_predictions.jsonl $out_path/predictions.jsonl --actual_file resources/${dataset}/test.jsonl
}

seed=${SEED:-1}
do_predictions_spj work/${dataset}/model=t5,generator=spj,lr=1e-4,steps=1/seed-${seed}
