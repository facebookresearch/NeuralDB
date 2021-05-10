#!/bin/bash

train5() {
  lr=1e-4
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_reprn $lr v1.0.1 0.50
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_reprn $lr v1.0.1 1.0

}

train5
