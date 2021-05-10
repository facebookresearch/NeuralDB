#!/bin/bash
# Usage: sbatch launch_distributed.sh <WRAPPER.sh>
## Usage: sbatch launch_distributed_gpu.sh
# Make sure to have run setup_env.sh first to create the environment.

#SBATCH --job-name=ndb-final-t5
#SBATCH --output=/checkpoint/%u/jobs/%x-%A-%a.out
#SBATCH --error=/checkpoint/%u/jobs/%x-%A-%a.err
#SBATCH --partition=dev
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:3
#SBATCH --constraint=volta32gb
#SBATCH --cpus-per-task=8
#SBATCH --mem=100G
#SBATCH --time=12:00:00
#SBATCH --signal=USR1@600
#SBATCH --open-mode=append
#SBATCH --comment="NDB"
#SBATCH --mail-type=FAIL

export MASTER_PORT=$((12000 + RANDOM % 20000))
conda activate /private/home/jth/anaconda3/envs/neuraldb

export PYTHONPATH="src:abstractive-models:extractive-models":"${PYTHONPATH}"

job=${SLURM_ARRAY_TASK_ID:-1}
cmd=$(sed -n "${job}p" < $1)
export NUM_GPU=3

nvidia-smi
eval "$cmd"