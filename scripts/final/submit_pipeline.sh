NUM_GPU=$NUM_GPU SEED=1 bash -x scripts/final/t5_pipeline.sh pipeline 5e-4 v0.5 50 pipeline dpr
NUM_GPU=$NUM_GPU SEED=2 bash -x scripts/final/t5_pipeline.sh pipeline 5e-4 v0.5 50 pipeline dpr
NUM_GPU=$NUM_GPU SEED=3 bash -x scripts/final/t5_pipeline.sh pipeline 5e-4 v0.5 50 pipeline dpr
NUM_GPU=$NUM_GPU SEED=4 bash -x scripts/final/t5_pipeline.sh pipeline 5e-4 v0.5 50 pipeline dpr
NUM_GPU=$NUM_GPU SEED=5 bash -x scripts/final/t5_pipeline.sh pipeline 5e-4 v0.5 50 pipeline dpr

NUM_GPU=$NUM_GPU SEED=1 bash -x scripts/final/t5_big_pipeline.sh pipeline 5e-4 v0.5 50 pipeline dpr
NUM_GPU=$NUM_GPU SEED=2 bash -x scripts/final/t5_big_pipeline.sh pipeline 5e-4 v0.5 50 pipeline dpr
NUM_GPU=$NUM_GPU SEED=3 bash -x scripts/final/t5_big_pipeline.sh pipeline 5e-4 v0.5 50 pipeline dpr
NUM_GPU=$NUM_GPU SEED=4 bash -x scripts/final/t5_big_pipeline.sh pipeline 5e-4 v0.5 50 pipeline dpr
NUM_GPU=$NUM_GPU SEED=5 bash -x scripts/final/t5_big_pipeline.sh pipeline 5e-4 v0.5 50 pipeline dpr