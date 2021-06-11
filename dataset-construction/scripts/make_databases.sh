size=$1
python src/ndb_data/construction/make_database_finalize.py work/newdbs/${size}_train work/newdbs/intermediate_train_${size}.jsonl --target-size ${size}
python src/ndb_data/construction/make_database_finalize.py work/newdbs/${size}_dev work/newdbs/intermediate_dev_${size}.jsonl --target-size ${size}
python src/ndb_data/construction/make_database_finalize.py work/newdbs/${size}_test work/newdbs/intermediate_test_${size}.jsonl --target-size ${size}