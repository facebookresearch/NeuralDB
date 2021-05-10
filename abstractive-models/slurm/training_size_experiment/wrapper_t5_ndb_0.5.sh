#!/bin/bash

. /usr/share/modules/init/sh
eval "$(conda shell.bash hook)"
module load anaconda3/5.0.1
. /public/apps/anaconda3/5.0.1/etc/profile.d/conda.sh

module purge
module unload cuda
module load cuda
module load NCCL
module load cudnn

conda activate HF

BASEDIR=$PWD

CHECKPOINT_DIR=${1:-"/checkpoint/$USER/shared/NDB/$SLURM_JOB_ID/"}

#MASTER_ADDR="${SLURM_NODELIST//[}"
#export MASTER_ADDR="${MASTER_ADDR%%[,-]*}"
#export MASTER_PORT=29500
export WORLD_SIZE=${SLURM_NTASKS}
export RANK=${SLURM_PROCID}

echo "Running job $SLURM_JOB_ID on $SLURM_NNODES nodes: $SLURM_NODELIST"
#echo "Mode: $MODE"
#echo "Node: $SLURMD_NODENAME"
#echo "Master: $MASTER_ADDR:$MASTER_PORT"
echo "World Size: $WORLD_SIZE"
echo "Rank: $RANK"
#echo "GPUs: $CUDA_VISIBLE_DEVICES"

cd $BASEDIR
export PYTHONPATH=.

sh run_train.sh /checkpoint/myazdani/NDB/t5-base-0.5-trainset 0.5 1
