seed=${SEED:-1}
num_gpus=${NUM_GPU:-1}
model_dir=$1
data_file=$2

OUTPUT_DIR=${model_dir}

# Add parent directory to python path to access transformer_base.py
export PYTHONPATH="src:abstractive-models:extractive-models":"${PYTHONPATH}"

python -u -m neuraldb.commands.finetune_operator \
  --model_name_or_path=t5-base \
  --eval_batch_size=64 \
  --max_source_length=256 \
  --max_target_length=64 \
  --output_dir=$OUTPUT_DIR \
  --n_gpu=$num_gpus \
  --do_predict \
  --train_path=${data_file} \
  --val_path=${data_file} \
  --test_path=${data_file}