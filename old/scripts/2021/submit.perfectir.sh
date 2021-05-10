seed=${SEED:-1}
num_gpus=${NUM_GPU:-1}
db=$1
lr=$2

OUTPUT_DIR=${WORK_DIR:-.}/checkpoints/experiment=perfectir/lr=${lr}/seed-${seed}
mkdir -pv $OUTPUT_DIR

# Add parent directory to python path to access transformer_base.py
export PYTHONPATH="src:abstractive-models:extractive-models":"${PYTHONPATH}"

python -u -m jobs.commands.finetune_seq2seq \
  --model_name_or_path=t5-base \
  --learning_rate=$lr \
  --train_batch_size=4 \
  --eval_batch_size=4 \
  --max_source_length=1024 \
  --max_target_length=256 \
  --num_train_epoch=6 \
  --output_dir=$OUTPUT_DIR \
  --n_gpu=$num_gpus \
  --do_train \
  --oracle \
  --dataset_version=v1.0 \
  --retriever=all \
  --train_path=resources/${db}/train.jsonl \
  --val_path=resources/${db}/dev.jsonl \
  --seed=$seed