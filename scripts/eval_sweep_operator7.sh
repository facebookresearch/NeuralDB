#!/bin/bash

train5() {
  lr=$1
  sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.3.1 1.0
  sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.3.1 0.5
  sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.3.1 0.25
  sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.3.1 0.1
  sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.3.1 0.075
  sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.3.1 0.05
  sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.3.1 0.025
  sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.3.1 0.01
}

train5 4e-5
train5 6e-5
train5 8e-5
train5 1e-6
