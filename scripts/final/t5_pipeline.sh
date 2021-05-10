experiment=$1
lr=$2
version=$3
context=$4
retriever=$5
pipeline=$6
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

OUTPUT_DIR=${WORK_DIR:-.}/final=true/experiment=${experiment}/dataset=ndb,model=t5-base,version=${version},pipeline=${pipeline}/lr=${lr}/context=${context},filters=${filters},max_queries=${max_queries}/seed-${seed}

mkdir -pv $OUTPUT_DIR

# Add parent directory to python path to access transformer_base.py
export PYTHONPATH="src:abstractive-models:extractive-models":"${PYTHONPATH}"

which python
python src/neuraldb/commands/t5train2.py \
  --retriever=$retriever \
  --model_name_or_path=t5-base \
  --learning_rate=${lr} \
  --train_batch_size=50 \
  --eval_batch_size=50 \
  --max_source_length=256 \
  --max_target_length=48 \
  --num_train_epoch=6 \
  --output_dir=$OUTPUT_DIR \
  --n_gpu=${NUM_GPU:-1} \
  --do_train \
  --train_path=${version}_${pipeline}/train_queries_last_${context}_${pipeline}.json \
  --val_path=${version}_${pipeline}/dev_queries_last_${context}_${pipeline}.json \
  --dataset_version=${version} \
  --seed=${seed} \
  ${maxq} \
  ${filt}

rm $OUTPUT_DIR/*checkpointepoch*