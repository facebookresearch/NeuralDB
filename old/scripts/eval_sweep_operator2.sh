#!/bin/bash

train5() {
  lr=$1
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.1 1.0
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.1 0.50
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.1 0.1
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.1 0.05
}


train5 6e-6
train5 8e-6
train5 1e-5
train5 2e-5
train5 4e-5
train5 6e-5
train5 8e-5
train5 1e-4
train5 2e-4
train5 4e-4
train5 6e-4
train5 8e-4
train5 1e-3

