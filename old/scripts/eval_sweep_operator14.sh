#!/bin/bash


train4() {
  lr=8e-5
  FILTER_RELATION="$1" sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_filter $lr v1.4 1.0
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
train4 "P47"
train4 "P50"
train4 "P54"
train4 "P57"
train4 "P58"
train4 "P61"
train4 "P69"
train4 "P106"
train4 "P108"
train4 "P118"
train4 "P1082"
train4 "P1092"
train4 "P1110"
train4 "P1174"
train4 "P1198"
train4 "P1867"
echo "FFF"
exit 0

train5() {
  lr=$1
  sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_sweep $lr v2.3_noisy 1.0
  sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_sweep $lr v2.3 1.0
}

train5 8e-5

train6() {
  lr=$1
  sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.4 1.0
  sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.4 0.5
  sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.4 0.25
  sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.4 0.1
  sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.4 0.075
  sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.4 0.05
  sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.4 0.025
  sbatch --array=1-3 scripts/launch_distributed_4gpu.sh operator_sweep $lr v1.4 0.01
}

train6 8e-5
