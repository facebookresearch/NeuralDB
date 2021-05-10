#!/bin/bash

train5() {
  lr=$1
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.1.1 1.0
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.1.1 0.50
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.1.1 0.1
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.1.1 0.05
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.1.1 0.01
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.1.1 0.005
}

train5 8e-6
train5 1e-5
train5 2e-5
train5 4e-5
train5 8e-5

train4() {
  lr=1e-4
  FILTER_RELATION="$1" sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_filter $lr v1.1.1
}

train4 "P6"
train4 "P19"
train4 "P20"
train4 "P19 P20"
train4 "P21"
train4 "P22"
train4 "P23"
train4 "P22 P23"
train4 "P26"
train4 "P27"
train4 "P35"
train4 "P38"
train4 "P38"
train4 "P47"
train4 "P50"
train4 "P54"
train4 "P57"
