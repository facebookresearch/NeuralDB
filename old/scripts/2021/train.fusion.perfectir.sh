seed=${SEED:-1}
num_gpus=${NUM_GPU:-1}
db=$1
lr=$2

OUTPUT_DIR=${WORK_DIR:-.}/checkpoint/experiment=perfectir_fusion/db=${db},lr=${lr}/seed-${seed}
mkdir -pv $OUTPUT_DIR

# Add parent directory to python path to access transformer_base.py
export PYTHONPATH="src:abstractive-models:extractive-models":"${PYTHONPATH}"

python -u -m neuraldb.commands.finetune_end2end_fusion \
  --model_name_or_path=t5-base \
  --learning_rate=$lr \
  --train_batch_size=8 \
  --eval_batch_size=8 \
  --max_source_length=256 \
  --max_target_length=256 \
  --num_train_epoch=3 \
  --output_dir=$OUTPUT_DIR \
  --n_gpu=$num_gpus \
  --do_train \
  --oracle \
  --dataset_version=${db} \
  --retriever=all \
  --train_path=resources/${db}/train.jsonl \
  --val_path=resources/${db}/dev.jsonl \
  --seed=$seed

python -u -m neuraldb.commands.finetune_end2end_fusion \
  --model_name_or_path=t5-base \
  --eval_batch_size=8 \
  --max_source_length=256 \
  --max_target_length=256 \
  --output_dir=$OUTPUT_DIR \
  --n_gpu=$num_gpus \
  --do_predict \
  --dataset_version=${db} \
  --retriever=all \
  --train_path=resources/${db}/train.jsonl \
  --val_path=resources/${db}/dev.jsonl \
  --test_path=resources/${db}/dev.jsonl \
  --seed=$seed \
  --oracle