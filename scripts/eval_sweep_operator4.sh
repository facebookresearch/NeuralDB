#!/bin/bash

train5() {
  lr=$1
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.1.2 1.0
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.1.3 1.0
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.1.4 1.0
}

train5 8e-6
train5 4e-5