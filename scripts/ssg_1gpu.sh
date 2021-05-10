#!/bin/bash
# Usage: sbatch launch_distributed.sh <WRAPPER.sh>
## Usage: sbatch launch_distributed_gpu.sh
# Make sure to have run setup_env.sh first to create the environment.

#SBATCH --job-name=ssg
#SBATCH --output=/checkpoint/%u/jobs/%A-%a.out
#SBATCH --error=/checkpoint/%u/jobs/%A-%a.err
#SBATCH --partition=learnfair
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:1

#SBATCH --constraint=volta32gb
#SBATCH --cpus-per-task=8
#SBATCH --mem=64G
#SBATCH --time=4:00:00
#SBATCH --signal=USR1@600
#SBATCH --open-mode=append
#SBATCH --comment="NDB"
#SBATCH --mail-type=FAIL

export MASTER_PORT=$((12000 + RANDOM % 20000))
conda activate /private/home/jth/anaconda3/envs/neuraldb

export PYTHONPATH="src:abstractive-models:extractive-models":"${PYTHONPATH}"
python src/neuraldb/models/predict_ssg.py --surrogate /checkpoint/jth/neuraldb/final=true/experiment=entire_database/dataset=ndb,model=t5-base,version=v0.5/lr=5e-4/context=50,filters=null,max_queries=null/seed-$2 --db ${SLURM_ARRAY_TASK_ID} --file $1 --out $3/${SLURM_ARRAY_TASK_ID}_$2_$(basename $1)