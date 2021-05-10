bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.1 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 4 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 1.0 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 10 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.1 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 2 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 2 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 1.0 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.1 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.1 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 2 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 2 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 1.0 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 8 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.1 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 5 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 2 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 8 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 1.0 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 12 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.5 8 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 0.1 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 10 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 8 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 10 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 10 2 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 8 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.1 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.5 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 1 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 0.5 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 2 12 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 0.5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 12 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 2 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 2 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 2 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 1.0 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 1.0 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 2 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 10 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 1.0 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 0.5 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 2 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 2 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.1 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.5 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 6 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 1.0 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 2 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 4 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 2 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 0.1 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.1 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 4 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.5 12 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 8 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 0.1 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 0.5 12 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 8 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 2 1 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 10 1 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 1.0 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 10 4 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.5 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 5 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 1.0 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 5 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.01 v0.2 50 5 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 5 4 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 1.0 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 12 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0002 v0.2 50 10 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.005 v0.2 50 0.5 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 1.0 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 12 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 1 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 0.5 6 16
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 10 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 4 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 10 4 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 1 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 4 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.5 12 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 10 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 6 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 5 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 2 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 0.1 12 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 6 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0008 v0.2 50 10 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 10 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 0.5 8 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 0.5 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 2 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 2 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 10 8 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.1 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 1.0 6 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 2 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 1 4
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.1 2 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.002 v0.2 50 2 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 0.1 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 6 16
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 4 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 1.0 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 1.0 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 5 6 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 2 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 1.0 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0005 v0.2 50 5 1 32
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.001 v0.2 50 0.1 6 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.01 v0.2 50 0.1 6 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0002 v0.2 50 0.1 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 5 12 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.008 v0.2 50 10 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0001 v0.2 50 2 2 64
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0001 v0.2 50 1.0 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 2 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 2 2 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.002 v0.2 50 10 4 8
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 10 1 32
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.008 v0.2 50 5 1 8
bash -x scripts/train.t5.rec.sh mips_sweep bert 0.0005 v0.2 50 0.5 1 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.005 v0.2 50 0.5 8 64
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.001 v0.2 50 1.0 6 4
CNN=16 bash -x scripts/train.t5.rec.sh mips_sweep t5 0.0008 v0.2 50 10 2 16