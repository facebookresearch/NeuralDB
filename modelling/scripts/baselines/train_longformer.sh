export PYTHONPATH=src
export TRANSFORMERS_CACHE=/local/scratch/jt719/.cache

data=$1
generator=$2
lr=$3
steps=${4:-1}
seed=${SEED:-1}

work_dir=work/${data}/model=longformer,generator=${generator},lr=${lr},steps=${steps}/seed-${seed}
data_dir=resources/${data}

python src/neuraldb/run.py \
  --model_name_or_path allenai/led-base-16384 \
  --learning_rate ${lr} \
  --gradient_accumulation_steps ${steps} \
  --output_dir ${work_dir} \
  --train_file ${data_dir}/train.jsonl \
  --validation_file ${data_dir}/dev.jsonl \
  --instance_generator ${generator} \
  --do_train \
  --do_eval \
  --num_train_epochs 3 \
  --evaluation_strategy epoch \
  --per_device_train_batch_size 8 \
  --per_device_eval_batch_size 8 \
  --predict_with_generate \
  --save_total_limit 2 \
  --seed ${seed} \
  --save_steps 10000
#--overwrite_output_dir \

rm -rfv ${work_dir}/checkpoint-*