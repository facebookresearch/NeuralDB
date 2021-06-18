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

dataset=${1:-v2.4}

function convert(){
  size=$1

  echo "Convert ${dataset} ${size}"
  mkdir -pv resources/${dataset}_${size}_ssg
  python src/neuraldb/convert_ssg_predictions.py resources/ssg_predictions/${dataset}_${size}/test_0.8_st_ssg_sup.json resources/${dataset}_${size}_ssg/test.jsonl --master_file resources/${dataset}_${size}/test.jsonl
}

convert 25
convert 50
convert 100
convert 250
convert 500
convert 1000