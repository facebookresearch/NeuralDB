#!/bin/bash

train5() {
  lr=$1
  sbatch --array=1-5 scripts/launch_distributed_4gpu_rand.sh operator_sweep $lr v1.1.1 1.0
  sbatch --array=1-5 scripts/launch_distributed_4gpu_rand.sh operator_sweep $lr v1.1.1 0.50
  sbatch --array=1-5 scripts/launch_distributed_4gpu_rand.sh operator_sweep $lr v1.1.1 0.1
  sbatch --array=1-5 scripts/launch_distributed_4gpu_rand.sh operator_sweep $lr v1.1.1 0.05

  sbatch --array=1-5 scripts/launch_distributed_4gpu_rand.sh operator_sweep $lr v1.1.4 1.0
  sbatch --array=1-5 scripts/launch_distributed_4gpu_rand.sh operator_sweep $lr v1.1.4 0.50
  sbatch --array=1-5 scripts/launch_distributed_4gpu_rand.sh operator_sweep $lr v1.1.4 0.1
  sbatch --array=1-5 scripts/launch_distributed_4gpu_rand.sh operator_sweep $lr v1.1.4 0.05
}

train5 8e-6
train5 8e-5
train5 8e-4