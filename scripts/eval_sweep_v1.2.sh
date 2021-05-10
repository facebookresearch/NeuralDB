#!/bin/bash

train5() {
  lr=$1
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator $lr v1.2_resolv_100k 0.1
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator $lr v1.2_resolv_100k 0.1
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator $lr v1.2_resolv_100k 0.5
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator $lr v1.2_resolv_100k 0.5
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator $lr v1.2_resolv_100k 1.0
  sbatch --array=1-5 scripts/launch_distributed_4gpu.sh operator $lr v1.2_resolv_100k 1.0

}

train5 8e-3
train5 8e-4
