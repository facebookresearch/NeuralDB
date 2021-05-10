#!/bin/bash
# Usage: sbatch launch_distributed.sh <WRAPPER.sh>
## Usage: sbatch launch_distributed_gpu.sh
# Make sure to have run setup_env.sh first to create the environment.

#SBATCH --job-name=ndb-score
#SBATCH --output=/checkpoint/%u/jobs/%x-%j.out
#SBATCH --error=/checkpoint/%u/jobs/%x-%j.err
#SBATCH --partition=learnfair
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:2
#SBATCH --constraint=volta32gb
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=1:00:00
#SBATCH --signal=USR1@600
#SBATCH --open-mode=append
#SBATCH --comment="NDB"
#SBATCH --mail-type=FAIL

export MASTER_PORT=$((12000 + RANDOM % 20000))
conda activate /private/home/jth/anaconda3/envs/neuraldb

export PYTHONPATH="src:abstractive-models:extractive-models":"${PYTHONPATH}"

job=${SLURM_ARRAY_TASK_ID:-1}
cmd=$(sed -n "${job}p" < scripts/$1.sh)
eval "$cmd"