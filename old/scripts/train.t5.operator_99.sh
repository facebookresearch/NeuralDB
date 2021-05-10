experiment=$1
lr=$2
method=$3
seed=${SEED:-42}

OUTPUT_DIR=${WORK_DIR:-.}/experiment=${experiment}/dataset=d1_99,model=t5-base,method=${method}/lr=${lr}/seed-${seed}
mkdir -pv $OUTPUT_DIR

# Add parent directory to python path to access transformer_base.py
export PYTHONPATH="src:abstractive-models:extractive-models":"${PYTHONPATH}"

python src/neuraldb/commands/t5train2_operator99.py \
  --model_name_or_path=t5-base \
  --learning_rate=${lr} \
  --train_batch_size=64 \
  --eval_batch_size=64 \
  --num_train_epoch=4 \
  --output_dir=$OUTPUT_DIR \
  --n_gpu=${NUM_GPU:-1} \
  --do_train \
  --train_path=v0.5_newssg_${method}/train.jsonl \
  --val_path=v0.5_newssg_${method}/dev.jsonl \
  --test_name=metrics_test.jsonl \
  --val_check_interval=1.0 \
  --seed=${seed}

retVal=$?
if [ $retVal -eq 1 ]; then
    echo "JOB FAILED"
    nvidia-smi
    env
fi

rm $OUTPUT_DIR/*checkpointepoch*