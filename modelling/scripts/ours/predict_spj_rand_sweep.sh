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

function do_predictions_ssg_spj() {
  dataset1=$1
  dataset2=$2
  model_path=$3
  generator=spj
  mkdir -pv work/${dataset2}/$model_path/
  tsp python src/neuraldb/run.py \
    --model_name_or_path work/${dataset1}/$model_path \
    --output_dir work/${dataset1}/$model_path \
    --predictions_file work/${dataset2}/$model_path/intermediate_predictions.jsonl \
    --do_predict --test_file resources/${dataset2}_ssg/test.jsonl \
    --instance_generator $generator \
    --per_device_eval_batch_size 64 \
    --predict_with_generate

  tsp python src/neuraldb/convert_spj_to_predictions.py work/${dataset2}/$model_path/intermediate_predictions.jsonl work/${dataset2}/$model_path/predictions.jsonl --actual_file resources/${dataset2}/test.jsonl
}


seed=${SEED:-1}
do_predictions_ssg_spj v2.4_25 v2.4_25 model=t5,generator=spj_rand,lr=1e-4,steps=1/seed-${seed}
do_predictions_ssg_spj v2.4_25 v2.4_50 model=t5,generator=spj_rand,lr=1e-4,steps=1/seed-${seed}
do_predictions_ssg_spj v2.4_25 v2.4_100 model=t5,generator=spj_rand,lr=1e-4,steps=1/seed-${seed}
do_predictions_ssg_spj v2.4_25 v2.4_250 model=t5,generator=spj_rand,lr=1e-4,steps=1/seed-${seed}
do_predictions_ssg_spj v2.4_25 v2.4_500 model=t5,generator=spj_rand,lr=1e-4,steps=1/seed-${seed}
do_predictions_ssg_spj v2.4_25 v2.4_1000 model=t5,generator=spj_rand,lr=1e-4,steps=1/seed-${seed}