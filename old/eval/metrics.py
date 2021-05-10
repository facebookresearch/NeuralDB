import argparse
import json
import re
from collections import Counter


def intersection_score(gold, pred):
    gold = gold.split()
    pred = pred.split()
    counts = Counter(pred)
    common_count = 0
    for g in gold:
        c = counts.get(g, 0)
        if c > 0:
            counts[g] = counts[g] - 1
            common_count += 1

    return common_count / len(gold)


def exact_match(gold, pred):
    return 1 if gold == pred else 0


def split_words(seq):
    words = re.split("[, \-!?:.]+", seq)
    non_empty_words = [w for w in words if w != '']
    return non_empty_words


def flatten_answers(golds, preds):
    gold_answers = []
    pred_answers = preds['queries']

    for i in range(len(golds)):
        db_golds = [g[2] for g in golds[i]['queries']]

        gold_answers.extend(db_golds)
    if len(gold_answers) != len(pred_answers):
        raise Exception(
            "The length of gold and predicted data does not match: gold {}, pred {}".format(len(gold_answers),
                                                                                            len(pred_answers)))
    return gold_answers, pred_answers


def calculate_scores(golds, preds):
    """
    given a list of flatten gold and prediction answers,
    it returns two metrics:
    1. accuracy: for the classification task (none, no, yes, span)
    2. Average of common words ratio (how many words in gold has also occurred in pred:
        e.g. gold = 'Facebook Applied AI Research', pred = 'Ads in Facebook' -> score = 1/4=2.5
    2. Percentage of the times we have an exact match. Exact match ignores punctuations.
    :param golds: gold data
    :param preds: prediction data
    :return: a dictionary with one score for each metric
    """

    correct_cls = []
    int_scores = []
    exact_scores = []
    for i in range(len(golds)):
        gold_answer_i = golds[i].lower()
        pred_answer_i = preds[i].lower()

        if gold_answer_i not in ['yes', 'no', 'none']:
            if pred_answer_i in ['yes', 'no', 'none']:
                int_scores.append(0)
                exact_scores.append(0)
                correct_cls.append(0)
            else:
                correct_cls.append(1)
                gold_answer_i_words = ' '.join(split_words(gold_answer_i))
                pred_answer_i_words = ' '.join(split_words(pred_answer_i))
                int_scores.append(intersection_score(gold_answer_i_words, pred_answer_i_words))
                exact_scores.append(exact_match(gold_answer_i_words, pred_answer_i_words))

        else:
            if gold_answer_i == pred_answer_i:
                correct_cls.append(1)
            else:
                correct_cls.append(0)

    scores_dict = {
        "classification": sum(correct_cls) / len(correct_cls),
        "intersection": (sum(int_scores) / len(int_scores)) if len(int_scores) > 0 else None,
        "exact": (sum(exact_scores) / len(exact_scores)) if len(exact_scores) > 0 else None
    }
    return scores_dict


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-gold', type=str, help='path to the gold answers file')
    parser.add_argument('-pred', type=str, help='path to the predicted answers file')

    args = parser.parse_args()
    gold_path = args.gold
    pred_path = args.pred
    gold_data = json.load(open(gold_path))
    pred_data = json.load(open(pred_path))
    gold_answers, pred_answers = flatten_answers(gold_data, pred_data)
    print(calculate_scores(gold_answers, pred_answers))
