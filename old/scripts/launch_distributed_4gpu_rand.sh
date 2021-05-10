#!/bin/bash
# Usage: sbatch launch_distributed.sh <WRAPPER.sh>
## Usage: sbatch launch_distributed_gpu.sh
# Make sure to have run setup_env.sh first to create the environment.

#SBATCH --job-name=ndb-rand-operator
#SBATCH --output=/checkpoint/%u/jobs/%x-%A-%a.out
#SBATCH --error=/checkpoint/%u/jobs/%x-%A-%a.err
#SBATCH --partition=learnfair
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:4
#SBATCH --constraint=volta32gb
#SBATCH --cpus-per-task=8
#SBATCH --mem=500G
#SBATCH --time=72:00:00
#SBATCH --signal=USR1@600
#SBATCH --open-mode=append
#SBATCH --comment="NDB"

#source /etc/profile.d/modules.sh
#module purge
#module load anaconda3
#conda init bash

nvidia-smi
env

conda activate /private/home/jth/anaconda3/envs/neuraldb

export MASTER_PORT=$((12000 + RANDOM % 20000))
CHECKPOINT_DIR="/checkpoint/$USER/job_staging/neuraldb_expts/"
mkdir -p $CHECKPOINT_DIR
seed=${seed:-${SLURM_ARRAY_TASK_ID:-1}}
SEED=$seed NUM_GPU=4 WORK_DIR=$CHECKPOINT_DIR bash -x ./scripts/train.t5.operator.rand.sh $1 $2 $3 $4
