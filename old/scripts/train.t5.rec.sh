experiment=$1
mips=$2
lr=$3
version=$4
context=$5
scale=$6
grad=$7

seed=${SEED:-42}

if [ -z "$max_queries" ]
then
  maxq=""
  max_queries=null
else
  maxq="--max_queries=${max_queries}"
fi

if [ -z "$CNN" ]
then
  cnn_var=null
  cnn=""
else
  cnn_var=$CNN
  cnn="--cnn=${CNN}"
fi


OUTPUT_DIR=${WORK_DIR:-.}/experiment=${experiment}/dataset=ndb,model=t5-base,retrieval=mips_${mips},version=${version}/lr=${lr},scale=${scale},grad=${grad},cnn=${cnn_var}/context=${context}/seed-${seed}

mkdir -pv $OUTPUT_DIR

# Add parent directory to python path to access transformer_base.py
export PYTHONPATH="src:abstractive-models:extractive-models":"${PYTHONPATH}"


python src/neuraldb/commands/t5train2_mips_${mips}.py \
  --model_name_or_path=t5-base \
  --learning_rate=${lr} \
  --train_batch_size=8 \
  --eval_batch_size=8 \
  --max_source_length=256 \
  --max_target_length=48 \
  --num_train_epoch=20 \
  --gradient_accumulation_steps=${grad} \
  --output_dir=$OUTPUT_DIR \
  --n_gpu=${NUM_GPU:-1} \
  --do_train \
  --train_path=${version}/train_queries_last_${context}.json \
  --val_path=${version}/dev_queries_last_${context}.json \
  --dataset_version=${version} \
  --seed=${seed} \
  --scale=${scale} \
  ${cnn} ${maxq}

rm $OUTPUT_DIR/*.ckpt