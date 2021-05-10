#!/bin/bash
# Usage: sbatch launch_distributed.sh <WRAPPER.sh>
## Usage: sbatch launch_distributed_gpu.sh
# Make sure to have run setup_env.sh first to create the environment.

#SBATCH --job-name=ndb-sweep
#SBATCH --output=/checkpoint/%u/jobs/%x-%A-%a.out
#SBATCH --error=/checkpoint/%u/jobs/%x-%A-%a.err
#SBATCH --partition=learnfair
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:1
#SBATCH --constraint=volta32gb
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=18:00:00
#SBATCH --signal=USR1@600
#SBATCH --open-mode=append
#SBATCH --comment="NDB"
#SBATCH --mail-type=FAIL

export MASTER_PORT=$((12000 + RANDOM % 20000))

echo $HOSTNAME
echo $MASTER_PORT
echo $CUDA_VISIBLE_DEVICES

#export NCCL_DEBUG=INFO
#export NCCL_DEBUG_SUBSYS=COLL
nvidia-smi

#conda activate /private/home/jth/anaconda3/envs/neuraldb

CHECKPOINT_DIR="/checkpoint/$USER/job_staging/neuraldb_expts/"
mkdir -p $CHECKPOINT_DIR



job=${SLURM_ARRAY_TASK_ID:-1}
cmd=$(sed -n "${job}p" < scripts/$1.sh)
NUM_GPU=1 WORK_DIR=$CHECKPOINT_DIR eval "$cmd"