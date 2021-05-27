from random import sample

from sentence_transformers import SentencesDataset, InputExample
from sentence_transformers.evaluation import BinaryClassificationEvaluator
from sentence_transformers.losses import *
from torch.utils.data import DataLoader
from torch.utils.data.sampler import WeightedRandomSampler

from ssg_utils import read_NDB_v2, create_dataset_v2,  create_dataset_v3

folder = '../v2.3_25'

# Define the model. Either from scratch of by loading a pre-trained model
model = SentenceTransformer('distilbert-base-nli-mean-tokens', device='cuda:3')

name = 'train'  # 'test_queries_last_',
size = 200
data_file = folder + "/" + name + ".jsonl"
db = read_NDB_v2(data_file)
dataset = create_dataset_v3(db)

train_examples = []
weights = []
for d in dataset:
    texts = ["[SEP]".join(d[0]), "".join(d[1])]
    label = d[2]
    if label == 1:
        weights.append(10)
    else:
        weights.append(1)
    train_examples.append(InputExample(texts=texts, label=label))

name = 'dev'  # 'test_queries_last_',
size = 50
data_file = folder + "/" + name +".jsonl"
db = read_NDB_v2(data_file)
dataset = create_dataset_v3(db)

dev_examples = []
for d in dataset:
    texts = ["[SEP]".join(d[0]), "".join(d[1])]
    label = d[2]
    dev_examples.append(InputExample(texts=texts, label=label))

batch_size = 120
print(len(train_examples))
train_loss = ContrastiveLoss(model)
# Tune the model
#onlypos_train_examples = list(filter(lambda p: p.label == 1, train_examples))
#onlyneg_train_examples = list(filter(lambda p: p.label == 0, train_examples))
#sampled = sample(onlyneg_train_examples, len(onlypos_train_examples) * 5)
#sampled.extend(onlypos_train_examples)

# Define your train dataset, the dataloader and the train loss
train_dataset = SentencesDataset(train_examples, model)
sampler = WeightedRandomSampler(weights=weights, num_samples=len(train_examples))
train_dataloader = DataLoader(train_dataset, sampler=sampler, shuffle=False, batch_size=batch_size)

# evaluator = ClassificationEvaluator.from_input_examples(dev_examples, batch_size=batch_size)
evaluator = BinaryClassificationEvaluator.from_input_examples(dev_examples, batch_size=batch_size)

model.fit(train_objectives=[(train_dataloader, train_loss)], epochs=10, warmup_steps=100, evaluator=evaluator,
          output_path="ssg-sentencetransformer-alldata-weighted-2.3-x10", evaluation_steps=5000)
