import csv
import logging
import os
from typing import List

import numpy as np
from sentence_transformers import InputExample
from sentence_transformers.evaluation import SentenceEvaluator


class ClassificationEvaluator(SentenceEvaluator):
    """
    Evaluate a model based on the similarity of the embeddings by calculating the Spearman and Pearson rank correlation
    in comparison to the gold standard labels.
    The metrics are the cosine similarity as well as euclidean and Manhattan distance
    The returned score is the Spearman correlation with a specified metric.

    The results are written in a CSV. If a CSV already exists, then values are appended.
    """

    def __init__(self, sentences1: List[str], sentences2: List[str], scores: List[float], batch_size: int = 16,
                 name: str = '', show_progress_bar: bool = False):
        """
        Constructs an evaluator based for the dataset

        The labels need to indicate the similarity between the sentences.

        :param sentences1:
            List with the first sentence in a pair
        :param sentences2:
            List with the second sentence in a pair
        :param scores:
            Similarity score between sentences1[i] and sentences2[i]

        """
        self.sentences1 = sentences1
        self.sentences2 = sentences2
        self.scores = scores

        assert len(self.sentences1) == len(self.sentences2)
        assert len(self.sentences1) == len(self.scores)

        self.name = name

        self.batch_size = batch_size
        if show_progress_bar is None:
            show_progress_bar = (
                    logging.getLogger().getEffectiveLevel() == logging.INFO or logging.getLogger().getEffectiveLevel() == logging.DEBUG)
        self.show_progress_bar = show_progress_bar

        self.csv_file = "similarity_evaluation" + ("_" + name if name else '') + "_results.csv"
        self.csv_headers = ["epoch", "steps", "cosine_pearson", "cosine_spearman", "euclidean_pearson",
                            "euclidean_spearman", "manhattan_pearson", "manhattan_spearman", "dot_pearson",
                            "dot_spearman"]

    @classmethod
    def from_input_examples(cls, examples: List[InputExample], **kwargs):
        sentences1 = []
        sentences2 = []
        scores = []

        for example in examples:
            sentences1.append(example.texts[0])
            sentences2.append(example.texts[1])
            scores.append(example.label)
        return cls(sentences1, sentences2, scores, **kwargs)

    def __call__(self, model, output_path: str = None, epoch: int = -1, steps: int = -1) -> float:
        if epoch != -1:
            if steps == -1:
                out_txt = " after epoch {}:".format(epoch)
            else:
                out_txt = " in epoch {} after {} steps:".format(epoch, steps)
        else:
            out_txt = ":"

        logging.info("Evaluation the model on " + self.name + " dataset" + out_txt)

        embeddings1 = model.encode(self.sentences1, batch_size=self.batch_size,
                                   show_progress_bar=self.show_progress_bar, convert_to_numpy=True)
        embeddings2 = model.encode(self.sentences2, batch_size=self.batch_size,
                                   show_progress_bar=self.show_progress_bar, convert_to_numpy=True)
        labels = np.array(self.scores)
        sigmoid_fun = lambda x: 1 / (1 + np.exp(-x))
        dot_products = np.array([sigmoid_fun(np.dot(emb1, emb2)) for emb1, emb2 in zip(embeddings1, embeddings2)])

        ind = np.nonzero(dot_products > 0.5)[0]
        denominator = len(ind)
        if denominator == 0:
            denominator = 1

        p = sum([x for i, x in enumerate(labels) if i in ind]) / denominator

        pos_labels = np.nonzero(labels == 1)[0].size

        r = sum([x for i, x in enumerate(labels) if i in ind]) / pos_labels

        eval_dot = 2 * (p * r) / (p + r)

        logging.info("F: {:.4f}".format(
            eval_dot))

        if output_path is not None:
            csv_path = os.path.join(output_path, self.csv_file)
            output_file_exists = os.path.isfile(csv_path)
            with open(csv_path, mode="a" if output_file_exists else 'w', encoding="utf-8") as f:
                writer = csv.writer(f)
                if not output_file_exists:
                    writer.writerow(self.csv_headers)

                writer.writerow([epoch, steps, eval_dot])

        return eval_dot
