experiment=$1
version=$2
context=$3
lr=$4
filter_size=$5

seed=${SEED:-42}



OUTPUT_DIR=${WORK_DIR:-.}/experiment=${experiment}/dataset=ndb,model=t5-base,retrieval=oracle,version=${version}/lr=${lr},filter_size=${filter_size}/context=${context}/seed-${seed}

mkdir -pv $OUTPUT_DIR

# Add parent directory to python path to access transformer_base.py
export PYTHONPATH="src:abstractive-models:extractive-models":"${PYTHONPATH}"


python -u src/neuraldb/commands/t5train2_fusion.py \
  --model_name_or_path=t5-base \
  --learning_rate=${lr} \
  --train_batch_size=4 \
  --eval_batch_size=4 \
  --max_source_length=128 \
  --max_target_length=48 \
  --num_train_epoch=20 \
  --output_dir=$OUTPUT_DIR \
  --n_gpu=${NUM_GPU:-1} \
  --do_train \
  --train_path=${version}/train_queries_last_${context}.json \
  --val_path=${version}/dev_queries_last_${context}.json \
  --dataset_version=${version} \
  --seed=${seed} \
  --filter_size=${filter_size} \
  --oracle

rm $OUTPUT_DIR/*epoch*.ckpt