experiment=$1
lr=$2

seed=${SEED:-42}

OUTPUT_DIR=${WORK_DIR:-.}/experiment=${experiment}/dataset=ndb,model=t5-base,oracle=true/lr=${lr}/seed-${seed}
mkdir -pv $OUTPUT_DIR

# Add parent directory to python path to access transformer_base.py
export PYTHONPATH="src:abstractive-models:extractive-models"

python src/neuraldb/commands/t5train2_operator2.py \
  --output_dir=$OUTPUT_DIR \
  --model_name_or_path t5-base \
  --do_train \
  --train_batch_size 50 \
  --eval_batch_size 50 \
  --n_gpu=${NUM_GPU:-1} \
  --train_path=v0.5_intermediates2/train_queries_last_50.json \
  --val_path=v0.5_intermediates2/dev_queries_last_50.json \
  --max_target_length=48 \
  --max_source_length=256 \
  --model_name_or_path=t5-base \
  --learning_rate=${lr} \
  --seed=${seed}


rm $OUTPUT_DIR/*checkpointepoch*