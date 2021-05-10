#!/bin/bash
# Usage: sbatch launch_distributed.sh <WRAPPER.sh>
## Usage: sbatch launch_distributed_gpu.sh
# Make sure to have run setup_env.sh first to create the environment.

#SBATCH --job-name=ndb-mips
#SBATCH --output=/checkpoint/%u/jobs/%x-%j.out
#SBATCH --error=/checkpoint/%u/jobs/%x-%j.err
#SBATCH --partition=dev
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:2
#SBATCH --constraint=volta32gb
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=24:00:00
#SBATCH --signal=USR1@600
#SBATCH --open-mode=append
#SBATCH --comment="NDB"
#SBATCH --mail-type=FAIL

echo $HOSTNAME
echo $CUDA_VISIBLE_DEVICES

export MASTER_PORT=$((12000 + RANDOM % 20000))

conda activate /private/home/jth/anaconda3/envs/neuraldb

CHECKPOINT_DIR="/checkpoint/$USER/job_staging/neuraldb_expts/"
mkdir -p $CHECKPOINT_DIR

seed=${seed:-${SLURM_ARRAY_TASK_ID:-1}}
SEED=$seed NUM_GPU=2 WORK_DIR=$CHECKPOINT_DIR bash -x ./scripts/train.t5.rec.sh $1 $2 $3 $4 $5 $6 $7
