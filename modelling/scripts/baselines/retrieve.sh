dataset=$1
retriever=$2

export PYTHONPATH=src
mkdir -pv resources/${dataset}_${retriever}
python src/neuraldb/retriever/${retriever}.py resources/${dataset}/train.jsonl resources/${dataset}_${retriever}/train.jsonl
python src/neuraldb/retriever/${retriever}.py resources/${dataset}/dev.jsonl resources/${dataset}_${retriever}/dev.jsonl
python src/neuraldb/retriever/${retriever}.py resources/${dataset}/test.jsonl resources/${dataset}_${retriever}/test.jsonl