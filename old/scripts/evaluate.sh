sbatch scripts/dev_4gpu.sh scripts/2021/predict.spj.sh checkpoint/experiment\=spj/db\=v2.1_25_filtered_quarter\,lr\=1e-4/seed-1 resources/v2.1_25_filtered_quarter/dev.jsonl
sbatch scripts/dev_4gpu.sh scripts/2021/predict.spj.sh checkpoint/experiment\=spj/db\=v2.1_25_filtered_quarter\,lr\=1e-4/seed-2 resources/v2.1_25_filtered_quarter/dev.jsonl
sbatch scripts/dev_4gpu.sh scripts/2021/predict.spj.sh checkpoint/experiment\=spj/db\=v2.1_25_filtered_quarter\,lr\=1e-4/seed-3 resources/v2.1_25_filtered_quarter/dev.jsonl

sbatch scripts/dev_4gpu.sh scripts/2021/predict.spj.sh checkpoint/experiment\=spj/db\=v2.1_25_filtered_tenth\,lr\=1e-4/seed-1 resources/v2.1_25_filtered_tenth/dev.jsonl
sbatch scripts/dev_4gpu.sh scripts/2021/predict.spj.sh checkpoint/experiment\=spj/db\=v2.1_25_filtered_tenth\,lr\=1e-4/seed-2 resources/v2.1_25_filtered_tenth/dev.jsonl
sbatch scripts/dev_4gpu.sh scripts/2021/predict.spj.sh checkpoint/experiment\=spj/db\=v2.1_25_filtered_tenth\,lr\=1e-4/seed-3 resources/v2.1_25_filtered_tenth/dev.jsonl

sbatch scripts/dev_4gpu.sh scripts/2021/predict.spj.sh checkpoint/experiment\=spj_random/db\=v2.1_25_filtered_quarter\,lr\=1e-4/seed-1 resources/v2.1_25_filtered_quarter/dev.jsonl
sbatch scripts/dev_4gpu.sh scripts/2021/predict.spj.sh checkpoint/experiment\=spj_random/db\=v2.1_25_filtered_quarter\,lr\=1e-4/seed-2 resources/v2.1_25_filtered_quarter/dev.jsonl
sbatch scripts/dev_4gpu.sh scripts/2021/predict.spj.sh checkpoint/experiment\=spj_random/db\=v2.1_25_filtered_quarter\,lr\=1e-4/seed-3 resources/v2.1_25_filtered_quarter/dev.jsonl

sbatch scripts/dev_4gpu.sh scripts/2021/predict.spj.sh checkpoint/experiment\=spj_random/db\=v2.1_25_filtered_tenth\,lr\=1e-4/seed-1 resources/v2.1_25_filtered_tenth/dev.jsonl
sbatch scripts/dev_4gpu.sh scripts/2021/predict.spj.sh checkpoint/experiment\=spj_random/db\=v2.1_25_filtered_tenth\,lr\=1e-4/seed-2 resources/v2.1_25_filtered_tenth/dev.jsonl
sbatch scripts/dev_4gpu.sh scripts/2021/predict.spj.sh checkpoint/experiment\=spj_random/db\=v2.1_25_filtered_tenth\,lr\=1e-4/seed-3 resources/v2.1_25_filtered_tenth/dev.jsonl




sbatch scripts/dev_4gpu.sh scripts/2021/predict.e2e.sh checkpoint/experiment\=perfectir/db\=v2.1_25_filtered_quarter\,lr\=1e-4/seed-1 resources/v2.1_25_filtered_quarter/dev.jsonl
sbatch scripts/dev_4gpu.sh scripts/2021/predict.e2e.sh checkpoint/experiment\=perfectir/db\=v2.1_25_filtered_quarter\,lr\=1e-4/seed-2 resources/v2.1_25_filtered_quarter/dev.jsonl
sbatch scripts/dev_4gpu.sh scripts/2021/predict.e2e.sh checkpoint/experiment\=perfectir/db\=v2.1_25_filtered_quarter\,lr\=1e-4/seed-3 resources/v2.1_25_filtered_quarter/dev.jsonl

sbatch scripts/dev_4gpu.sh scripts/2021/predict.e2e.sh checkpoint/experiment\=perfectir/db\=v2.1_25_filtered_tenth\,lr\=1e-4/seed-1 resources/v2.1_25_filtered_tenth/dev.jsonl
sbatch scripts/dev_4gpu.sh scripts/2021/predict.e2e.sh checkpoint/experiment\=perfectir/db\=v2.1_25_filtered_tenth\,lr\=1e-4/seed-2 resources/v2.1_25_filtered_tenth/dev.jsonl
sbatch scripts/dev_4gpu.sh scripts/2021/predict.e2e.sh checkpoint/experiment\=perfectir/db\=v2.1_25_filtered_tenth\,lr\=1e-4/seed-3 resources/v2.1_25_filtered_tenth/dev.jsonl

sbatch scripts/dev_4gpu.sh scripts/2021/predict.e2e.sh checkpoint/experiment\=wholedb/db\=v2.1_25_filtered_quarter\,lr\=1e-4/seed-1 resources/v2.1_25_filtered_quarter/dev.jsonl
sbatch scripts/dev_4gpu.sh scripts/2021/predict.e2e.sh checkpoint/experiment\=wholedb/db\=v2.1_25_filtered_quarter\,lr\=1e-4/seed-2 resources/v2.1_25_filtered_quarter/dev.jsonl
sbatch scripts/dev_4gpu.sh scripts/2021/predict.e2e.sh checkpoint/experiment\=wholedb/db\=v2.1_25_filtered_quarter\,lr\=1e-4/seed-3 resources/v2.1_25_filtered_quarter/dev.jsonl

sbatch scripts/dev_4gpu.sh scripts/2021/predict.e2e.sh checkpoint/experiment\=wholedb/db\=v2.1_25_filtered_tenth\,lr\=1e-4/seed-1 resources/v2.1_25_filtered_tenth/dev.jsonl
sbatch scripts/dev_4gpu.sh scripts/2021/predict.e2e.sh checkpoint/experiment\=wholedb/db\=v2.1_25_filtered_tenth\,lr\=1e-4/seed-2 resources/v2.1_25_filtered_tenth/dev.jsonl
sbatch scripts/dev_4gpu.sh scripts/2021/predict.e2e.sh checkpoint/experiment\=wholedb/db\=v2.1_25_filtered_tenth\,lr\=1e-4/seed-3 resources/v2.1_25_filtered_tenth/dev.jsonl

