NUM_GPU=$NUM_GPU SEED=1 bash -x scripts/final/t5_entire_database.sh search_database_large 5e-4 v0.5 50 tfidf
NUM_GPU=$NUM_GPU SEED=2 bash -x scripts/final/t5_entire_database.sh search_database_large 5e-4 v0.5 50 tfidf
NUM_GPU=$NUM_GPU SEED=3 bash -x scripts/final/t5_entire_database.sh search_database_large 5e-4 v0.5 50 tfidf
NUM_GPU=$NUM_GPU SEED=4 bash -x scripts/final/t5_entire_database.sh search_database_large 5e-4 v0.5 50 tfidf
NUM_GPU=$NUM_GPU SEED=5 bash -x scripts/final/t5_entire_database.sh search_database_large 5e-4 v0.5 50 tfidf
NUM_GPU=$NUM_GPU SEED=1 bash -x scripts/final/t5_oracle_database.sh oracle_large v0.5 50 5e-4
NUM_GPU=$NUM_GPU SEED=2 bash -x scripts/final/t5_oracle_database.sh oracle_large v0.5 50 5e-4
NUM_GPU=$NUM_GPU SEED=3 bash -x scripts/final/t5_oracle_database.sh oracle_large v0.5 50 5e-4
NUM_GPU=$NUM_GPU SEED=4 bash -x scripts/final/t5_oracle_database.sh oracle_large v0.5 50 5e-4
NUM_GPU=$NUM_GPU SEED=5 bash -x scripts/final/t5_oracle_database.sh oracle_large v0.5 10 5e-4
