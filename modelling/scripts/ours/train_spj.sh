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
export PYTHONPATH=src
export TRANSFORMERS_CACHE=/local/scratch/jt719/.cache

dataset=$1
generator=$2
lr=$3
steps=${4:-1}
seed=${SEED:-1}

work_dir=work/${dataset}/model=t5,generator=${generator},lr=${lr},steps=${steps}/seed-${seed}
data_dir=resources/${dataset}

python src/neuraldb/run.py \
  --model_name_or_path t5-base \
  --learning_rate ${lr} \
  --gradient_accumulation_steps ${steps} \
  --output_dir ${work_dir} \
  --train_file ${data_dir}/train.jsonl \
  --validation_file ${data_dir}/dev.jsonl \
  --instance_generator ${generator} \
  --do_train \
  --do_eval \
  --num_train_epochs 3 \
  --evaluation_strategy epoch \
  --per_device_train_batch_size 8 \
  --per_device_eval_batch_size 8 \
  --predict_with_generate \
  --save_total_limit 2 \
  --seed ${seed} \
  --save_steps 10000

rm -rfv ${work_dir}/checkpoint-*