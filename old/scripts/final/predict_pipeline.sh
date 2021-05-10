python -m neuraldb.commands.t5train2 --output_dir /checkpoint/jth/neuraldb/final=true/experiment=pipeline/dataset=ndb,model=t5-base,version=v0.5,pipeline=dpr/lr=5e-4/context=50,filters=null,max_queries=null/seed-1/ --model_name_or_path t5-base --do_predict --train_batch_size 50 --eval_batch_size 50 --n_gpu 3 --train_path=v0.5_dpr/train_queries_last_50_dpr.json --val_path=v0.5_dpr/dev_queries_last_50.json --test_path=v0.5_dpr/dev_queries_last_50_dpr.json --retriever pipeline   --dataset_version=v0.5
python -m neuraldb.commands.t5train2 --output_dir /checkpoint/jth/neuraldb/final=true/experiment=pipeline/dataset=ndb,model=t5-base,version=v0.5,pipeline=dpr/lr=5e-4/context=50,filters=null,max_queries=null/seed-2/ --model_name_or_path t5-base --do_predict --train_batch_size 50 --eval_batch_size 50 --n_gpu 3 --train_path=v0.5_dpr/train_queries_last_50_dpr.json --val_path=v0.5_dpr/dev_queries_last_50.json --test_path=v0.5_dpr/dev_queries_last_50_dpr.json --retriever pipeline   --dataset_version=v0.5
python -m neuraldb.commands.t5train2 --output_dir /checkpoint/jth/neuraldb/final=true/experiment=pipeline/dataset=ndb,model=t5-base,version=v0.5,pipeline=dpr/lr=5e-4/context=50,filters=null,max_queries=null/seed-3/ --model_name_or_path t5-base --do_predict --train_batch_size 50 --eval_batch_size 50 --n_gpu 3 --train_path=v0.5_dpr/train_queries_last_50_dpr.json --val_path=v0.5_dpr/dev_queries_last_50.json --test_path=v0.5_dpr/dev_queries_last_50_dpr.json --retriever pipeline   --dataset_version=v0.5
python -m neuraldb.commands.t5train2 --output_dir /checkpoint/jth/neuraldb/final=true/experiment=pipeline/dataset=ndb,model=t5-base,version=v0.5,pipeline=dpr/lr=5e-4/context=50,filters=null,max_queries=null/seed-4/ --model_name_or_path t5-base --do_predict --train_batch_size 50 --eval_batch_size 50 --n_gpu 3 --train_path=v0.5_dpr/train_queries_last_50_dpr.json --val_path=v0.5_dpr/dev_queries_last_50.json --test_path=v0.5_dpr/dev_queries_last_50_dpr.json --retriever pipeline   --dataset_version=v0.5
python -m neuraldb.commands.t5train2 --output_dir /checkpoint/jth/neuraldb/final=true/experiment=pipeline/dataset=ndb,model=t5-base,version=v0.5,pipeline=dpr/lr=5e-4/context=50,filters=null,max_queries=null/seed-5/ --model_name_or_path t5-base --do_predict --train_batch_size 50 --eval_batch_size 50 --n_gpu 3 --train_path=v0.5_dpr/train_queries_last_50_dpr.json --val_path=v0.5_dpr/dev_queries_last_50.json --test_path=v0.5_dpr/dev_queries_last_50_dpr.json --retriever pipeline   --dataset_version=v0.5

python -m neuraldb.commands.t5train2 --output_dir /checkpoint/jth/neuraldb/final=true/experiment=pipeline/dataset=ndb,model=t5-base,version=v0.5,pipeline=dpr/lr=5e-4/context=50,filters=null,max_queries=null/seed-1/ --model_name_or_path t5-base --do_predict --train_batch_size 50 --eval_batch_size 50 --n_gpu 3 --train_path=v0.5_dpr/train_queries_last_50_dpr.json --val_path=v0.5_dpr/dev_queries_last_50.json --test_path=v0.5_dpr/dev_queries_last_50_dpr.json --retriever pipeline   --dataset_version=v0.5
python -m neuraldb.commands.t5train2 --output_dir /checkpoint/jth/neuraldb/final=true/experiment=pipeline/dataset=ndb,model=t5-base,version=v0.5,pipeline=dpr/lr=5e-4/context=50,filters=null,max_queries=null/seed-2/ --model_name_or_path t5-base --do_predict --train_batch_size 50 --eval_batch_size 50 --n_gpu 3 --train_path=v0.5_dpr/train_queries_last_50_dpr.json --val_path=v0.5_dpr/dev_queries_last_50.json --test_path=v0.5_dpr/dev_queries_last_50_dpr.json --retriever pipeline   --dataset_version=v0.5
python -m neuraldb.commands.t5train2 --output_dir /checkpoint/jth/neuraldb/final=true/experiment=pipeline/dataset=ndb,model=t5-base,version=v0.5,pipeline=dpr/lr=5e-4/context=50,filters=null,max_queries=null/seed-3/ --model_name_or_path t5-base --do_predict --train_batch_size 50 --eval_batch_size 50 --n_gpu 3 --train_path=v0.5_dpr/train_queries_last_50_dpr.json --val_path=v0.5_dpr/dev_queries_last_50.json --test_path=v0.5_dpr/dev_queries_last_50_dpr.json --retriever pipeline   --dataset_version=v0.5
python -m neuraldb.commands.t5train2 --output_dir /checkpoint/jth/neuraldb/final=true/experiment=pipeline/dataset=ndb,model=t5-base,version=v0.5,pipeline=dpr/lr=5e-4/context=50,filters=null,max_queries=null/seed-4/ --model_name_or_path t5-base --do_predict --train_batch_size 50 --eval_batch_size 50 --n_gpu 3 --train_path=v0.5_dpr/train_queries_last_50_dpr.json --val_path=v0.5_dpr/dev_queries_last_50.json --test_path=v0.5_dpr/dev_queries_last_50_dpr.json --retriever pipeline   --dataset_version=v0.5
python -m neuraldb.commands.t5train2 --output_dir /checkpoint/jth/neuraldb/final=true/experiment=pipeline/dataset=ndb,model=t5-base,version=v0.5,pipeline=dpr/lr=5e-4/context=50,filters=null,max_queries=null/seed-5/ --model_name_or_path t5-base --do_predict --train_batch_size 50 --eval_batch_size 50 --n_gpu 3 --train_path=v0.5_dpr/train_queries_last_50_dpr.json --val_path=v0.5_dpr/dev_queries_last_50.json --test_path=v0.5_dpr/dev_queries_last_50_dpr.json --retriever pipeline   --dataset_version=v0.5

python -m neuraldb.commands.t5train2 --output_dir /checkpoint/jth/neuraldb/final=true/experiment=pipeline/dataset=ndb,model=t5-base,version=v0.5,pipeline=big_dpr/lr=5e-4/context=50,filters=null,max_queries=null/seed-2 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 3 --train_path=v0.5_dpr/train_queries_last_50_dpr.json --val_path=v0.5_dpr/dev_queries_last_50_dpr.json --test_path=v0.5_dpr/dev_queries_last_50_dpr.json --retriever pipeline   --dataset_version=v0.5
python -m neuraldb.commands.t5train2 --output_dir /checkpoint/jth/neuraldb/final=true/experiment=pipeline/dataset=ndb,model=t5-base,version=v0.5,pipeline=big_dpr/lr=5e-4/context=50,filters=null,max_queries=null/seed-4 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 3 --train_path=v0.5_dpr/train_queries_last_50_dpr.json --val_path=v0.5_dpr/dev_queries_last_50_dpr.json --test_path=v0.5_dpr/dev_queries_last_50_dpr.json --retriever pipeline   --dataset_version=v0.5
python -m neuraldb.commands.t5train2 --output_dir /checkpoint/jth/neuraldb/final=true/experiment=pipeline/dataset=ndb,model=t5-base,version=v0.5,pipeline=big_dpr/lr=5e-4/context=50,filters=null,max_queries=null/seed-5 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 3 --train_path=v0.5_dpr/train_queries_last_50_dpr.json --val_path=v0.5_dpr/dev_queries_last_50_dpr.json --test_path=v0.5_dpr/dev_queries_last_50_dpr.json --retriever pipeline   --dataset_version=v0.5
python -m neuraldb.commands.t5train2 --output_dir /checkpoint/jth/neuraldb/final=true/experiment=pipeline/dataset=ndb,model=t5-base,version=v0.5,pipeline=big_dpr/lr=5e-4/context=50,filters=null,max_queries=null/seed-1 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 3 --train_path=v0.5_dpr/train_queries_last_50_dpr.json --val_path=v0.5_dpr/dev_queries_last_50_dpr.json --test_path=v0.5_dpr/dev_queries_last_50_dpr.json --retriever pipeline   --dataset_version=v0.5
python -m neuraldb.commands.t5train2 --output_dir /checkpoint/jth/neuraldb/final=true/experiment=pipeline/dataset=ndb,model=t5-base,version=v0.5,pipeline=big_dpr/lr=5e-4/context=50,filters=null,max_queries=null/seed-3 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 3 --train_path=v0.5_dpr/train_queries_last_50_dpr.json --val_path=v0.5_dpr/dev_queries_last_50_dpr.json --test_path=v0.5_dpr/dev_queries_last_50_dpr.json --retriever pipeline   --dataset_version=v0.5

