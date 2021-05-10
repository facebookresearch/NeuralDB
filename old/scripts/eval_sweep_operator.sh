#!/bin/bash

train5() {
  lr=1e-4
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.0.1 1.0
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.0.1 0.75
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.0.1 0.50
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.0.1 0.25
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.0.1 0.1
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.0.1 0.05
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.0.1 0.01
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.0.1 0.05
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.0.1 0.001
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.0.1 0.005
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.0.1 0.0005
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.0.1 0.0001
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.0.1 0.00005
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.0.1 0.00001
}

train5

train4() {
  lr=1e-4
  FILTER_RELATION="$1" sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator_filter $lr v1.0.1
}

train4 "P6"
train4 "P19"
train4 "P20"
train4 "P19 P20"
train4 "P21"
train4 "P22"
train4 "P23"
train4 "P22 P23"
train4 "P38"
train4 "P54"
train4 "P1831"
train4 "P1867"
train4 "P1831 P1867"