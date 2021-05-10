experiment=$1
lr=$2
version=$3
train_percentage=$4
epochs=$5
model=$6
seed=${SEED:-42}

if [ -z "$train_percentage" ]
then
  maxq=""
  train_percentage=null
else
  maxq="--train_percentage=${train_percentage}"
fi

if [ -z "$FILTER_RELATION"]
then
  filt=""
  filters=null
else
  filt="--filter ${FILTER_RELATION}"
  filters=$(echo $FILTER_RELATION | tr -s ' ' '.' )
fi

OUTPUT_DIR=${WORK_DIR:-.}/experiment=${experiment}/dataset=operator,model=t5-base,version=${version}/ft_lr=${lr},ft_epochs=${epochs}/filters=${filters},train_percentage=${train_percentage}/seed-${seed}

mkdir -pv $OUTPUT_DIR

# Add parent directory to python path to access transformer_base.py
export PYTHONPATH="src:abstractive-models:extractive-models":"${PYTHONPATH}"

python src/neuraldb/commands/t5train2_operator.py \
  --model_name_or_path=t5-base \
  --learning_rate=${lr} \
  --train_batch_size=64 \
  --eval_batch_size=64 \
  --ft_weights=${model}/seed-${seed} \
  --num_train_epoch=${epochs} \
  --output_dir=$OUTPUT_DIR \
  --n_gpu=${NUM_GPU:-1} \
  --do_train \
  --train_path=${version}/generated_clean_train.jsonl \
  --val_path=${version}/generated_clean_val.jsonl \
  --test_name=metrics_test.jsonl \
  --val_check_interval=1.0 \
  --seed=${seed} \
  ${filt} ${maxq}

retVal=$?
if [ $retVal -eq 1 ]; then
    echo "JOB FAILED"
    nvidia-smi
    env
fi

rm $OUTPUT_DIR/*checkpointepoch*