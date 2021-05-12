python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0005,filter_size=8/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 8 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0001,filter_size=16/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 16 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0002,filter_size=24/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 24 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=8e-05,filter_size=24/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 24 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0001,filter_size=8/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 8 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0002,filter_size=8/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 8 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0008,filter_size=4/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 4 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.001,filter_size=8/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 8 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0008,filter_size=6/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 6 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.001,filter_size=6/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 6 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.001,filter_size=1/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 1 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0002,filter_size=2/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 2 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0002,filter_size=6/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 6 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0002,filter_size=1/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 1 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=8e-05,filter_size=1/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 1 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=8e-05,filter_size=12/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 12 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.002,filter_size=8/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 8 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=8e-05,filter_size=16/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 16 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0001,filter_size=12/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 12 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0002,filter_size=32/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 32 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=6e-05,filter_size=2/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 2 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=8e-05,filter_size=8/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 8 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0005,filter_size=32/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 32 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.002,filter_size=2/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 2 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=8e-05,filter_size=32/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 32 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0008,filter_size=2/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 2 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0001,filter_size=6/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 6 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0001,filter_size=2/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 2 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=6e-05,filter_size=16/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 16 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=8e-05,filter_size=6/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 6 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.002,filter_size=6/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 6 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0001,filter_size=24/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 24 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0002,filter_size=4/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 4 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0002,filter_size=16/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 16 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=6e-05,filter_size=6/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 6 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0008,filter_size=32/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 32 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0008,filter_size=16/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 16 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=6e-05,filter_size=1/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 1 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.002,filter_size=32/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 32 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.001,filter_size=32/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 32 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.001,filter_size=12/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 12 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0008,filter_size=8/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 8 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0002,filter_size=12/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 12 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0005,filter_size=16/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 16 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.001,filter_size=16/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 16 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.002,filter_size=24/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 24 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.001,filter_size=24/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 24 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=6e-05,filter_size=8/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 8 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=6e-05,filter_size=12/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 12 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0005,filter_size=6/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 6 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0001,filter_size=1/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 1 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.002,filter_size=16/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 16 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0008,filter_size=12/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 12 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0005,filter_size=12/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 12 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0008,filter_size=1/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 1 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=8e-05,filter_size=4/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 4 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=8e-05,filter_size=2/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 2 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=6e-05,filter_size=4/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 4 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.002,filter_size=12/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 12 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.001,filter_size=2/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 2 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0005,filter_size=2/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 2 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.002,filter_size=4/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 4 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.002,filter_size=1/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 1 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0005,filter_size=1/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 1 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0005,filter_size=4/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 4 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0005,filter_size=24/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 24 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.001,filter_size=4/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 4 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=6e-05,filter_size=24/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 24 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=6e-05,filter_size=32/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 32 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0008,filter_size=24/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 24 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0001,filter_size=4/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 4 --dataset_version=v0.4
python -m neuraldb.commands.t5train2_fusion --output_dir /checkpoint/jth/job_staging/neuraldb_expts/experiment=tfidf_fusion/dataset=ndb,model=t5-base,retrieval=tfidf,version=v0.4/lr=0.0001,filter_size=32/context=100/seed-42 --model_name_or_path t5-base --do_predict --train_batch_size 4 --eval_batch_size 4 --n_gpu 1 --train_path=v0.4/train_queries_last_100.json --val_path=v0.4/dev_queries_last_100.json --test_path=v0.4/dev_queries_last_100.json --filter_size 32 --dataset_version=v0.4