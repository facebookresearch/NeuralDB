size=$1
python src/ndb_data/construction/make_questions.py work/newdbs/intermediate_train_${size}.jsonl work/newdbs/final_train_${size}.jsonl
python src/ndb_data/construction/make_questions.py work/newdbs/intermediate_dev_${size}.jsonl work/newdbs/final_dev_${size}.jsonl
python src/ndb_data/construction/make_questions.py work/newdbs/intermediate_test_${size}.jsonl work/newdbs/final_test_${size}.jsonl
