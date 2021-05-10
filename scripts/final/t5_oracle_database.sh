experiment=$1
version=$2
context=$3
lr=$4
max_queries=$5

seed=${SEED:-42}

if [ -z "$max_queries" ]
then
  maxq=""
  max_queries=null
else
  maxq="--max_queries=${max_queries}"
fi

if [ -z "$FILTER_RELATION"]
then
  filt=""
  filters=null
else
  filt="--filter ${FILTER_RELATION}"
  filters=$(echo $FILTER_RELATION | tr -s ' ' '.' )
fi

OUTPUT_DIR=${WORK_DIR:-.}/experiment=${experiment}/dataset=ndb,model=t5-base,oracle=true,version=${version}/lr=${lr}/context=${context},filters=${filters},max_queries=${max_queries}/seed-${seed}

mkdir -pv $OUTPUT_DIR

# Add parent directory to python path to access transformer_base.py
export PYTHONPATH="src:abstractive-models:extractive-models":"${PYTHONPATH}"


python src/neuraldb/commands/t5train2.py \
  --model_name_or_path=t5-base \
  --learning_rate=${lr} \
  --train_batch_size=4 \
  --eval_batch_size=4 \
  --max_source_length=1024 \
  --max_target_length=256 \
  --num_train_epoch=6 \
  --output_dir=$OUTPUT_DIR \
  --n_gpu=${NUM_GPU:-1} \
  --do_train \
  --train_path=${version}/train_queries_last_${context}.json \
  --val_path=${version}/dev_queries_last_${context}.json \
  --dataset_version=${version} \
  --seed=${seed} \
  --oracle \
  ${maxq} \
  ${filt}

rm $OUTPUT_DIR/*checkpointepoch*