#!/bin/bash

train4() {
  lr=1e-3
  FILTER_RELATION="$1" sbatch --array=1-5 scripts/launch_distributed_2gpu.sh filter_relations $lr v0.4 50
  FILTER_RELATION="$1" sbatch --array=1-5 scripts/launch_distributed_2gpu.sh filter_relations $lr v0.4 100
  FILTER_RELATION="$1" sbatch --array=1-5 scripts/launch_distributed_2gpu.sh filter_relations $lr v0.4 500
}

train4 "is_a_at"
train4 "is_a"
train4 "is_a_at is_a"
train4 "born_in"
train4 "educated_at"
train4 "lives_where_with"
train4 "lives_where_with spouse"
train4 "sex"
train4 "continent_location"
train4 "country_location"
train4 "inv_rel"
train4 "spouse"
train4 "lang"
train4 "has_baby"
train4 "sport"
train4 "spouse has_baby"