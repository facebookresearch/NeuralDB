context=$1
distractors=$2
num=$3

for i in $(seq 1 10);
do
  python -m neuraldb.generation.mix_distractors \
    --in-file v0.4/dev_queries_last_${context}.json \
    --out-file generate_distrators_v0.4/dev_${context}_${distractors}_${num}_${i}.json \
    --num ${num} \
    --distractor-file notebooks/$2.txt;
done;
