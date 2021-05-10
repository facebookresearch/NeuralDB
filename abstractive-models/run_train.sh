OUTPUT_DIR=$1
#export CURRENT_DIR=${PWD}
#export OUTPUT_DIR=${CURRENT_DIR}/${OUTPUT_DIR_NAME}

# Make output directory if it doesn't exist
mkdir -p $OUTPUT_DIR

# Add parent directory to python path to access transformer_base.py
export PYTHONPATH="../../":"${PYTHONPATH}"

python finetune.py \
  --data_dir=../data/gen/v0.1 \
  --model_name_or_path=t5-base \
  --learning_rate=1e-3 \
  --train_batch_size=50 \
  --eval_batch_size=50 \
  --max_source_length=512 \
  --max_target_length=8 \
  --num_train_epoch=300 \
  --output_dir=$OUTPUT_DIR \
  --n_gpu=4 \
  --train_percentage=$2 \
  --dev_percentage=$3 \
  --do_train
