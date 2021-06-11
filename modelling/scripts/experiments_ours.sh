dataset=${1:-v2.4_25}
export seed=${SEED:-1}

SEED=${seed} tsp bash scripts/ours/train_spj.sh $dataset spj_rand 1e-4
SEED=${seed} tsp bash scripts/ours/train_spj.sh $dataset spj 1e-4
