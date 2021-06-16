import argparse
import os

from sentence_transformers import SentencesDataset, InputExample, SentenceTransformer
from sentence_transformers.evaluation import BinaryClassificationEvaluator
from sentence_transformers.losses import ContrastiveLoss
from torch.utils.data import DataLoader
from torch.utils.data.sampler import WeightedRandomSampler

from ssg_utils import read_NDB, create_dataset


def is_valid_folder(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="training ssg")
    parser.add_argument(
        "-i",
        dest="folder",
        required=True,
        help="input data folder",
        type=lambda x: is_valid_folder(parser, x),
    )
    parser.add_argument("-b", dest="batch_size", type=int, help="batch size", default=100)

    parser.add_argument("-e", dest="epochs", type=int, help="number of epochs", default=10)

    parser.add_argument("-o", dest="output", required=True, help="output address")
    parser.add_argument("-d", dest="device", default="cuda:0", help="output address")

    args = parser.parse_args()

    folder = args.folder
    batch_size = args.batch_size
    epochs = args.epochs
    output = args.output
    device = args.device

    # Define the model. Either from scratch of by loading a pre-trained model
    model = SentenceTransformer("distilbert-base-nli-mean-tokens", device=device)

    # read the train data
    name = "train"
    data_file = folder + "/" + name + ".jsonl"
    db = read_NDB(data_file)
    dataset = create_dataset(db)

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

    # read the dev data
    name = "dev"
    data_file = folder + "/" + name + ".jsonl"
    db = read_NDB(data_file)
    dataset = create_dataset(db)

    dev_examples = []
    for d in dataset:
        texts = ["[SEP]".join(d[0]), "".join(d[1])]
        label = d[2]
        dev_examples.append(InputExample(texts=texts, label=label))

    train_loss = ContrastiveLoss(model)

    # Define your train dataset, the dataloader and the train loss
    train_dataset = SentencesDataset(train_examples, model)
    sampler = WeightedRandomSampler(weights=weights, num_samples=len(train_examples))
    train_dataloader = DataLoader(
        train_dataset, sampler=sampler, shuffle=False, batch_size=batch_size
    )

    evaluator = BinaryClassificationEvaluator.from_input_examples(
        dev_examples, batch_size=batch_size
    )

    model.fit(
        train_objectives=[(train_dataloader, train_loss)],
        epochs=epochs,
        warmup_steps=100,
        evaluator=evaluator,
        output_path=output,
        evaluation_steps=100,
    )
