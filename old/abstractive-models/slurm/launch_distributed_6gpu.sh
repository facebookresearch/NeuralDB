#!/bin/bash
# Usage: sbatch launch_distributed.sh <WRAPPER.sh>
## Usage: sbatch launch_distributed_gpu.sh <CHECKPOINT_PATH> <INSP> <BERT_NAME> <LOG_DIR>
# Make sure to have run setup_env.sh first to create the environment.

#SBATCH --job-name=ndb
#SBATCH --output=/checkpoint/%u/jobs/%x-%j.out
#SBATCH --error=/checkpoint/%u/jobs/%x-%j.err
#SBATCH --partition=learnfair
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:6
#SBATCH --constraint=volta32gb
#SBATCH --cpus-per-task=8
#SBATCH --mem=300G
#SBATCH --time=72:00:00
#SBATCH --signal=USR1@600
#SBATCH --open-mode=append
#SBATCH --comment="NDB"

CHECKPOINT_DIR="/checkpoint/$USER/shared/NDB/$SLURM_JOB_ID/"
mkdir -p $CHECKPOINT_DIR

echo "Starting distributed job $SLURM_JOB_ID on $SLURM_NNODES nodes: $SLURM_NODELIST"
BASEDIR=$PWD
WRAPPER=$1

chmod 777 "$BASEDIR/$WRAPPER"
srun --label "$BASEDIR/$WRAPPER" $CHECKPOINT_DIR
