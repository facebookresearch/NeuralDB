#!/bin/bash
# Usage: sbatch launch_distributed.sh <WRAPPER.sh>
## Usage: sbatch launch_distributed_gpu.sh
# Make sure to have run setup_env.sh first to create the environment.

#SBATCH --job-name=ndb
#SBATCH --output=/checkpoint/%u/jobs/%x-%A-%a.out
#SBATCH --error=/checkpoint/%u/jobs/%x-%A-%a.err
#SBATCH --partition=dev
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:1
#SBATCH --constraint=volta32gb
#SBATCH --cpus-per-task=8
#SBATCH --mem=256G
#SBATCH --time=24:00:00
#SBATCH --signal=USR1@600
#SBATCH --open-mode=append
#SBATCH --comment="NDB - ACL abstract deadline 1/25"

#source /etc/profile.d/modules.sh
#module purge
#module load anaconda3
#conda init bash

nvidia-smi
env

conda activate /private/home/jth/anaconda3/envs/neuraldb

bash predict_surrogate.sh $1 $SLURM_ARRAY_TASK_ID