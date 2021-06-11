from collections import defaultdict


def precision(actual, predicted):
    return (
        sum(1.0 for p in predicted if p in actual) / float(len(predicted))
        if len(predicted)
        else 1.0
    )


def recall(actual, predicted):
    return (
        sum(1.0 for p in predicted if p in actual) / float(len(actual))
        if len(actual)
        else 1.0
    )


def f1(actual, predicted):
    actual = set(actual)
    predicted = set(predicted)

    pr = precision(actual, predicted)
    rec = recall(actual, predicted)

    return compute_f1(pr, rec)


def join_decoded(decoded_labels):
    return " ".join(decoded_labels)


def exact_match(actual, predicted):
    return 1.0 if join_decoded(actual) == join_decoded(predicted) else 0.0


def exact_match_case_insensitive(actual, predicted):
    return (
        1.0 if join_decoded(actual).lower() == join_decoded(predicted).lower() else 0.0
    )


def compute_f1(pr, rec):
    return 2.0 * pr * rec / (pr + rec) if (pr + rec > 0.0) else 0.0


def average_score(all_actual, all_predicted, scoring_function):
    running_score = 0
    num_instances = 0

    for actual, predicted in zip(all_actual, all_predicted):
        num_instances += 1
        local_score = scoring_function(actual, predicted)
        assert local_score <= 1

        running_score += local_score
        assert running_score <= num_instances

    return running_score / num_instances if num_instances > 0 else 0.0


def breakdown_score(key, all_actual, all_predicted, metadata, scoring_function):
    running_score = defaultdict(int)
    num_instances = defaultdict(int)

    for actual, predicted, metadatum in zip(all_actual, all_predicted, metadata):
        num_instances[metadatum[key]] += 1
        local_score = scoring_function(actual, predicted)
        assert local_score <= 1

        running_score[metadatum[key]] += local_score
        assert running_score[metadatum[key]] <= num_instances[metadatum[key]]

    return {
        key: running_score[key] / num_instances[key] if num_instances[key] > 0 else 0.0
        for key in num_instances.keys()
    }
