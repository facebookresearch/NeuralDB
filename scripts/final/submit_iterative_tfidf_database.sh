NUM_GPU=$NUM_GPU SEED=$SEED bash -x scripts/final/t5_iterate_database.sh iterate_database 5e-4 v0.5 50 tfidf
NUM_GPU=$NUM_GPU SEED=$SEED bash -x scripts/final/t5_iterate_database.sh iterate_database 5e-4 v0.5 100 tfidf
NUM_GPU=$NUM_GPU SEED=$SEED bash -x scripts/final/t5_iterate_database.sh iterate_database 5e-4 v0.5 500 tfidf
NUM_GPU=$NUM_GPU SEED=$SEED bash -x scripts/final/t5_iterate_database.sh iterate_database 5e-4 v0.5 1000 tfidf
NUM_GPU=$NUM_GPU SEED=$SEED bash -x scripts/final/t5_iterate_database.sh iterate_database 5e-4 v0.5 2000 tfidf
NUM_GPU=$NUM_GPU SEED=$SEED bash -x scripts/final/t5_iterate_database.sh iterate_database 5e-4 v0.5 5000 tfidf
NUM_GPU=$NUM_GPU SEED=$SEED bash -x scripts/final/t5_iterate_database.sh iterate_database 5e-4 v0.5 7000 tfidf
NUM_GPU=$NUM_GPU SEED=$SEED bash -x scripts/final/t5_iterate_database.sh iterate_database 5e-4 v0.5 10000 tfidf
