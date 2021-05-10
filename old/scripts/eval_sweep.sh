#!/bin/bash

train() {
  lr=$1
  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh $lr v0.2 50
  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh $lr v0.2 100
  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh $lr v0.2 300
  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh $lr v0.2 500

  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh $lr v0.4 50
  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh $lr v0.4 100
  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh $lr v0.4 500
  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh $lr v0.4 1000
  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh $lr v0.4 2000
  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh $lr v0.4 5000
  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh $lr v0.4 7000
  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh $lr v0.4 10000
}

train 1e-2
train 8e-3
train 5e-3
train 2e-3
train 1e-3
train 8e-4
train 5e-4
train 3e-4
train 1e-4
