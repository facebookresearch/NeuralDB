#!/bin/bash

train() {
  lr=$1
  sbatch --array=1-5 scripts/launch_distributed_rec_2gpu.sh $lr v0.2 50
  sbatch --array=1-5 scripts/launch_distributed_rec_2gpu.sh $lr v0.2 100
  sbatch --array=1-5 scripts/launch_distributed_rec_2gpu.sh $lr v0.2 300
  sbatch --array=1-5 scripts/launch_distributed_rec_2gpu.sh $lr v0.2 500
}


train 5e-3
train 2e-3
train 1e-3
train 8e-4
