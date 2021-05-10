export OUTPUT_DIR=../experiments/t5-small-0.05-trainset-v01
#export CURRENT_DIR=${PWD}
#export OUTPUT_DIR=${CURRENT_DIR}/${OUTPUT_DIR_NAME}

# Make output directory if it doesn't exist
mkdir -p $OUTPUT_DIR

# Add parent directory to python path to access transformer_base.py
export PYTHONPATH="../../":"${PYTHONPATH}"

python finetune.py \
  --data_dir=../data/gen/v0.1 \
  --model_name_or_path=t5-small \
  --output_dir=$OUTPUT_DIR \
  --eval_batch_size=50 \
  --max_source_length=512 \
  --max_target_length=8 \
  --n_gpu=4 \
  --do_predict
