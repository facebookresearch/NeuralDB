#!/bin/bash

train() {
  lr=$1

  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh lr_sweep $lr v0.5 50
  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh lr_sweep $lr v0.5 100
  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh lr_sweep $lr v0.5 500
  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh lr_sweep $lr v0.5 1000
  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh lr_sweep $lr v0.5 2000
  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh lr_sweep $lr v0.5 5000
  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh lr_sweep $lr v0.5 7000
  sbatch --array=1-5 scripts/launch_distributed_2gpu.sh lr_sweep $lr v0.5 10000
}

train 1e-3

