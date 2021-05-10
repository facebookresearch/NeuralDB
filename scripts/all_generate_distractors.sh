function sweep() {
  bash scripts/generate_distractors.sh $1 $2 1
  bash scripts/generate_distractors.sh $1 $2 10
  bash scripts/generate_distractors.sh $1 $2 50
  bash scripts/generate_distractors.sh $1 $2 100
  bash scripts/generate_distractors.sh $1 $2 1000
  bash scripts/generate_distractors.sh $1 $2 2500
  bash scripts/generate_distractors.sh $1 $2 5000
  bash scripts/generate_distractors.sh $1 $2 7500
  bash scripts/generate_distractors.sh $1 $2 10000
}


sweep 50 distractors
sweep 50 similar

sweep 100 distractors
sweep 100 similar

sweep 500 distractors
sweep 500 similar

sweep 1000 distractors
sweep 1000 similar

sweep 2000 distractors
sweep 2000 similar

sweep 5000 distractors
sweep 5000 similar