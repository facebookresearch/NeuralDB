def precision(actual, predicted):
    actual_set = set(actual)
    return (
        sum(1.0 for p in predicted if p in actual_set) / float(len(predicted))
        if len(predicted)
        else 1.0
    )


def recall(actual, predicted):
    if len(actual) == 0:
        return 1.0

    actual_set = set(actual)
    return (
        sum(1.0 for p in predicted if p in actual_set) / float(len(actual))
        if len(actual)
        else 1.0
    )


def f1(actual, predicted):
    pr = precision(actual, predicted)
    rec = recall(actual, predicted)

    return 2.0 * pr * rec / (pr + rec) if (pr + rec > 0.0) else 0.0
