NUM_GPU=$NUM_GPU SEED=$SEED bash -x scripts/final/t5_entire_database.sh entire_database 1e-3 v0.5 50 all
NUM_GPU=$NUM_GPU SEED=$SEED bash -x scripts/final/t5_entire_database.sh entire_database 5e-4 v0.5 50 all
NUM_GPU=$NUM_GPU SEED=$SEED bash -x scripts/final/t5_entire_database.sh entire_database 1e-4 v0.5 50 all
NUM_GPU=$NUM_GPU SEED=$SEED bash -x scripts/final/t5_entire_database.sh entire_database 5e-5 v0.5 50 all
NUM_GPU=$NUM_GPU SEED=$SEED bash -x scripts/final/t5_entire_database.sh entire_database 1e-5 v0.5 50 all