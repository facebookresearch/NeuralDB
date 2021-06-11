
dataset=${1:-v2.4}

function convert(){
  size=$1

  echo "Convert ${dataset} ${size}"
  mkdir -pv resources/${dataset}_${size}_ssg
  python src/neuraldb/convert_ssg_predictions.py resources/ssg_predictions/${dataset}_${size}/test_0.8_st_ssg_sup.json resources/${dataset}_${size}_ssg/test.jsonl --master_file resources/${dataset}_${size}/test.jsonl
}

convert 25
convert 50
convert 100
convert 250
convert 500
convert 1000