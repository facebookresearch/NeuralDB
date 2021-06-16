import json


def read_NDB(data_file):
    with open(data_file) as file:
        dataset = []

        for line in file:
            db = json.loads(line)

            facts = db["facts"]
            queries = db["queries"]
            dataset.append([facts, queries])
        return dataset


def create_dataset(db):
    dataset = []
    eos = "<eos>"
    for d in db:

        questions = d[1]
        ctx = d[0]

        for q in questions:

            t = q["height"]
            gold_facts = q["facts"]
            context = ctx[: t + 1]
            flat_facts = [item for sublist in gold_facts for item in sublist]

            # all facts in flat facts can be positive
            state = [q["query"]]
            pos_act = [context[g] for g in flat_facts]
            # everything else is negative
            neg_act = [x for i, x in enumerate(context) if i not in flat_facts]

            dataset.append([state, eos, 0])
            dataset.extend([[state, n, 0] for n in neg_act])
            pos_set = [[state, p, 1] for p in pos_act]

            dataset.extend(pos_set)

            for g in gold_facts:
                if len(g) <= 1:
                    state = [q["query"], context[g[0]]]

                    pos_act = eos
                    neg_act = context
                    item = [state, pos_act, 1]
                    dataset.append(item)
                    dataset.extend([[state, n, 0] for n in neg_act])
                else:
                    g_0 = g[0]
                    g_1 = g[1]

                    state = [q["query"], context[g_0]]
                    pos_act = context[g_1]
                    neg_act = [x for i, x in enumerate(context) if i != g_1]
                    item = [state, pos_act, 1]
                    dataset.append(item)
                    dataset.extend([[state, n, 0] for n in neg_act])

                    state = [q["query"], context[g_1]]
                    pos_act = context[g_0]
                    neg_act = [x for i, x in enumerate(context) if i != g_0]
                    item = [state, pos_act, 1]
                    dataset.append(item)
                    dataset.extend([[state, n, 0] for n in neg_act])

                    state = [q["query"], context[g_0], context[g_1]]
                    pos_act = eos
                    neg_act = context
                    item = [state, pos_act, 1]
                    dataset.append(item)
                    dataset.extend([[state, n, 0] for n in neg_act])

    return dataset


def prepare_tokenizer(tokenizer):
    special_tokens = []
    special_tokens.extend(["<sep>", "<SEP>", "<eos>", "[SEP]"])
    tokenizer.add_special_tokens({"additional_special_tokens": special_tokens})
