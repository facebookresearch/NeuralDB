sbatch --array=1-5 scripts/launch_distributed_2gpu_fusion_oracle.sh oracle_fusion v0.5 50 0.00008 12
sbatch --array=1-5 scripts/launch_distributed_2gpu_fusion_oracle.sh oracle_fusion v0.5 50 0.0005 12

sbatch --array=1-5 scripts/launch_distributed_2gpu_fusion_oracle.sh oracle_fusion v0.5 100 0.00008 12
sbatch --array=1-5 scripts/launch_distributed_2gpu_fusion_oracle.sh oracle_fusion v0.5 100 0.0005 12
sbatch --array=1-5 scripts/launch_distributed_2gpu_oracle.sh oracle_concat v0.5 50 0.0008
sbatch --array=1-5 scripts/launch_distributed_2gpu_oracle.sh oracle_concat v0.5 50 0.0005
sbatch --array=1-5 scripts/launch_distributed_2gpu_oracle.sh oracle_concat v0.5 100 0.0008
sbatch --array=1-5 scripts/launch_distributed_2gpu_oracle.sh oracle_concat v0.5 100 0.0005
