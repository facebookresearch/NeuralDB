#!/bin/bash

train5() {
  lr=$1
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.3_balanced_100k 0.25
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.3_balanced_100k 0.125
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.3_balanced_100k 0.1
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.3_balanced_100k 0.075
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.3_balanced_100k 0.05
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.3_balanced_100k 0.025
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.3_balanced_100k 0.01
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.3_balanced_100k 0.005
}

train5 6e-5
train5 8e-5
train5 1e-6
