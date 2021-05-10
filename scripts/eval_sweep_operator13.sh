#!/bin/bash

train5() {
  lr=$1
  sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_sweep $lr v2.2_noisy 1.0
  sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_sweep $lr v2.2 1.0
}

train5 8e-5
