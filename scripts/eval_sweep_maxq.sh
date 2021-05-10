#!/bin/bash

train2() {
  lr=1e-3
  xcont=$1
  xmax=$2
  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh data_ablation $lr v0.2 $xcont $xmax
}
train4() {
  lr=1e-3
  xcont=$1
  xmax=$2
  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh data_ablation $lr v0.4 $xcont $xmax
}

train24() {
  train2 $1 $2;
  train4 $1 $2;
}

train24 50 2
train24 50 5
train24 50 10
train24 50 25
train24 50 50

train24 100 2
train24 100 5
train24 100 10
train24 100 25
train24 100 50
train24 100 75

train2 300 2
train2 300 5
train2 300 10
train2 300 25
train2 300 50
train2 300 75
train2 300 100
train2 300 150
train2 300 200
train2 300 250
train2 300 300

train24 500 2
train24 500 5
train24 500 10
train24 500 25
train24 500 50
train24 500 75
train24 500 100
train24 500 150
train24 500 200
train24 500 250
train24 500 300
train24 500 350
train24 500 400
train24 500 450
train24 500 500

train4 1000 50
train4 1000 100
train4 1000 250
train4 1000 500
train4 1000 750
train4 1000 1000

train4 2000 50
train4 2000 100
train4 2000 250
train4 2000 500
train4 2000 750
train4 2000 1000
train4 2000 1500
train4 2000 2000

train4 5000 50
train4 5000 100
train4 5000 250
train4 5000 500
train4 5000 750
train4 5000 1000
train4 5000 1500
train4 5000 2000
train4 5000 2500
train4 5000 3000
train4 5000 4000
train4 5000 5000

