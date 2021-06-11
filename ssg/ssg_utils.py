import json



def read_NDB_v2(data_file):
    with open(data_file) as file:
        counter = 0
        dataset = []

        for line in file:
            db = json.loads(line)

            facts = db['facts']
            queries = db['queries']
            dataset.append([facts, queries])
        return dataset

def create_dataset_ds_v2(db):
    dataset = []
    eos = "<eos>"
    for d in db:

        questions = d[1]
        ctx = d[0]

        for q in questions:

            t = q['height']
            if q['predicted_evidence']:
                gold_facts = q['predicted_evidence'][0]
            else:
                gold_facts =[]
            query_type = q['type']
            context = ctx[0:t+1]

            if 'join' in query_type or len(gold_facts) <= 1:

                state = [q['question']]
                pos_act = None

                if not gold_facts:
                    neg_act = [x for i, x in enumerate(context) if i not in gold_facts]
                    dataset.append([state, eos, 1])
                    dataset.extend([[state, n, 0] for n in neg_act])

                for g in gold_facts:
                    pos_act = None
                    if g < t:
                        pos_act = context[g]

                    neg_act = [x for i, x in enumerate(context) if i not in gold_facts]
                    if pos_act is not None:
                        item = [state, pos_act, 1]

                        dataset.append(item)

                    dataset.append([state, eos, 0])

                    dataset.extend([[state, n, 0] for n in neg_act])
                    if pos_act is None:
                        break
                    state = state.copy()
                    state.append(pos_act)

                if pos_act is not None:
                    pos_act = eos
                    neg_act = context
                    item = [state, pos_act, 1]
                    dataset.append(item)

                    dataset.extend([[state, n, 0] for n in neg_act])
            else:

                state = [q['question']]

                pos_act = [context[g] for g in gold_facts]

                neg_act = [x for i, x in enumerate(context) if i not in gold_facts]

                dataset.append([state, eos, 0])
                dataset.extend([[state, n, 0] for n in neg_act])
                pos_set = [[state, p, 1] for p in pos_act]

                dataset.extend(pos_set)

                for g in gold_facts:
                    state = [q['question'], context[g]]

                    pos_act = eos
                    neg_act = context
                    item = [state, pos_act, 1]
                    dataset.append(item)

                    dataset.extend([[state, n, 0] for n in neg_act])
    return dataset

def create_dataset_v3(db):
    dataset = []
    eos = "<eos>"
    for d in db:

        questions = d[1]
        ctx = d[0]

        for q in questions:

            t = q['height']
            gold_facts = q['facts']
            query_type = q['type']
            context = ctx[0:t+1]
            flat_facts = [item for sublist in gold_facts for item in sublist]
            #print(flat_facts)
            # all facts in flat facts can be positive
            state = [q['question']]

            pos_act = [context[g] for g in flat_facts]
            neg_act = [x for i, x in enumerate(context) if i not in flat_facts]

            dataset.append([state, eos, 0])
            dataset.extend([[state, n, 0] for n in neg_act])
            pos_set = [[state, p, 1] for p in pos_act]

            dataset.extend(pos_set)

            for g in gold_facts:
                if len(g) <= 1:
                    state = [q['question'], context[g[0]]]

                    pos_act = eos
                    neg_act = context
                    item = [state, pos_act, 1]
                    dataset.append(item)
                    dataset.extend([[state, n, 0] for n in neg_act])
                else:
                    g_0 = g[0]
                    g_1 = g[1]

                    state = [q['question'], context[g_0]]
                    pos_act = context[g_1]
                    neg_act = [x for i, x in enumerate(context) if i != g_1]
                    item = [state, pos_act, 1]
                    dataset.append(item)
                    dataset.extend([[state, n, 0] for n in neg_act])

                    state = [q['question'], context[g_1]]
                    pos_act = context[g_0]
                    neg_act = [x for i, x in enumerate(context) if i != g_0]
                    item = [state, pos_act, 1]
                    dataset.append(item)
                    dataset.extend([[state, n, 0] for n in neg_act])

                    state = [q['question'], context[g_0], context[g_1]]
                    pos_act = eos
                    neg_act = context
                    item = [state, pos_act, 1]
                    dataset.append(item)
                    dataset.extend([[state, n, 0] for n in neg_act])

    return dataset


def create_dataset_v2(db):
    dataset = []
    eos = "<eos>"
    for d in db:

        questions = d[1]
        ctx = d[0]

        for q in questions:

            t = q['height']
            gold_facts = q['facts']
            query_type = q['type']
            context = ctx[0:t+1]

            if 'join' in query_type or len(gold_facts) <= 1:

                state = [q['question']]
                pos_act = None

                if not gold_facts:
                    neg_act = [x for i, x in enumerate(context) if i not in gold_facts]
                    dataset.append([state, eos, 1])
                    dataset.extend([[state, n, 0] for n in neg_act])

                for g in gold_facts:
                    pos_act = None
                    if g < t:
                        pos_act = context[g]

                    neg_act = [x for i, x in enumerate(context) if i not in gold_facts]
                    if pos_act is not None:
                        item = [state, pos_act, 1]

                        dataset.append(item)

                    dataset.append([state, eos, 0])

                    dataset.extend([[state, n, 0] for n in neg_act])
                    if pos_act is None:
                        break
                    state = state.copy()
                    state.append(pos_act)

                if pos_act is not None:
                    pos_act = eos
                    neg_act = context
                    item = [state, pos_act, 1]
                    dataset.append(item)

                    dataset.extend([[state, n, 0] for n in neg_act])
            else:

                state = [q['question']]

                pos_act = [context[g] for g in gold_facts]

                neg_act = [x for i, x in enumerate(context) if i not in gold_facts]

                dataset.append([state, eos, 0])
                dataset.extend([[state, n, 0] for n in neg_act])
                pos_set = [[state, p, 1] for p in pos_act]

                dataset.extend(pos_set)

                for g in gold_facts:
                    state = [q['question'], context[g]]

                    pos_act = eos
                    neg_act = context
                    item = [state, pos_act, 1]
                    dataset.append(item)

                    dataset.extend([[state, n, 0] for n in neg_act])
    return dataset


def read_NDB(data_file):
    with open(data_file) as json_file:
        data = json.load(json_file)

    counter = 0
    dataset = []
    for d in data:
        counter = counter + 1
        updates = [[u[0], u[2]] for u in d['updates']]
        questions = d['queries']
        dataset.append([updates, questions])
    return dataset


def read_james_NDB(data_file):
    with open(data_file) as json_file:
        data = json.load(json_file)

    counter = 0
    dataset = []
    for d in data:
        counter = counter + 1
        updates = [[u[0], u[2]] for u in d['updates']]
        questions = d['queries']
        dataset.append([updates, questions])
    return dataset


def create_james_dataset(db):
    dataset = []
    eos = "<eos>"
    for d in db:
        updates = d[0]
        questions = d[1]
        ctx = [c[1] for c in updates]

        for q in questions:

            t = q[0]
            gold_facts = q[6]
            query_type = q[3]
            context = ctx[0:t]

            if 'join' in query_type or 'atomic' in query_type:
                # print(t)
                # print(gold_facts)
                # print(q[4])
                state = [q[4]]
                pos_act = None

                if not gold_facts:
                    neg_act = [x for i, x in enumerate(context) if i not in gold_facts]
                    dataset.append([state, eos, 1])
                    dataset.extend([[state, n, 0] for n in neg_act])

                for g in gold_facts:
                    pos_act = None
                    if g < t:
                        pos_act = context[g]

                    neg_act = [x for i, x in enumerate(context) if i not in gold_facts]
                    if pos_act is not None:
                        item = [state, pos_act, 1]

                        dataset.append(item)

                    dataset.append([state, eos, 0])

                    dataset.extend([[state, n, 0] for n in neg_act])
                    if pos_act is None:
                        break
                    state = state.copy()
                    state.append(pos_act)

                if pos_act is not None:
                    pos_act = eos
                    neg_act = context
                    item = [state, pos_act, 1]
                    dataset.append(item)

                    dataset.extend([[state, n, 0] for n in neg_act])
    return dataset


def create_james_dataset_with_aggr(db):
    dataset = []
    eos = "<eos>"
    for d in db:
        updates = d[0]
        questions = d[1]
        ctx = [c[1] for c in updates]

        for q in questions:

            t = q[0]
            gold_facts = q[6]
            query_type = q[3]
            context = ctx[0:t]

            if 'join' in query_type or 'atomic' in query_type:
                # print(t)
                # print(gold_facts)
                # print(q[4])
                state = [q[4]]
                pos_act = None

                if not gold_facts:
                    neg_act = [x for i, x in enumerate(context) if i not in gold_facts]
                    dataset.append([state, eos, 1])
                    dataset.extend([[state, n, 0] for n in neg_act])

                for g in gold_facts:
                    pos_act = None
                    if g < t:
                        pos_act = context[g]

                    neg_act = [x for i, x in enumerate(context) if i not in gold_facts]
                    if pos_act is not None:
                        item = [state, pos_act, 1]

                        dataset.append(item)

                    dataset.append([state, eos, 0])

                    dataset.extend([[state, n, 0] for n in neg_act])
                    if pos_act is None:
                        break
                    state = state.copy()
                    state.append(pos_act)

                if pos_act is not None:
                    pos_act = eos
                    neg_act = context
                    item = [state, pos_act, 1]
                    dataset.append(item)

                    dataset.extend([[state, n, 0] for n in neg_act])
            else:

                state = [q[4]]

                pos_act = [context[g] for g in gold_facts]

                neg_act = [x for i, x in enumerate(context) if i not in gold_facts]

                dataset.append([state, eos, 0])
                dataset.extend([[state, n, 0] for n in neg_act])
                pos_set = [[state, p, 1] for p in pos_act]

                dataset.extend(pos_set)

                for g in gold_facts:
                    state = [q[4], context[g]]

                    pos_act = eos
                    neg_act = context
                    item = [state, pos_act, 1]
                    dataset.append(item)

                    dataset.extend([[state, n, 0] for n in neg_act])
    return dataset


def create_dataset(db):
    dataset = []
    eos = "<eos>"
    for d in db:
        updates = d[0]
        questions = d[1]
        ctx = [c[1] for c in updates]

        for q in questions:

            t = q[0]
            gold_facts = q[1]
            query_type = q[3]
            context = ctx[0:t]

            if 'join' in query_type or len(gold_facts) <= 1:

                state = [q[4]]
                pos_act = None

                if not gold_facts:
                    neg_act = [x for i, x in enumerate(context) if i not in gold_facts]
                    dataset.append([state, eos, 1])
                    dataset.extend([[state, n, 0] for n in neg_act])

                for g in gold_facts:
                    pos_act = None
                    if g < t:
                        pos_act = context[g]

                    neg_act = [x for i, x in enumerate(context) if i not in gold_facts]
                    if pos_act is not None:
                        item = [state, pos_act, 1]

                        dataset.append(item)

                    dataset.append([state, eos, 0])

                    dataset.extend([[state, n, 0] for n in neg_act])
                    if pos_act is None:
                        break
                    state = state.copy()
                    state.append(pos_act)

                if pos_act is not None:
                    pos_act = eos
                    neg_act = context
                    item = [state, pos_act, 1]
                    dataset.append(item)

                    dataset.extend([[state, n, 0] for n in neg_act])
            else:

                state = [q[4]]

                pos_act = [context[g] for g in gold_facts]

                neg_act = [x for i, x in enumerate(context) if i not in gold_facts]

                dataset.append([state, eos, 0])
                dataset.extend([[state, n, 0] for n in neg_act])
                pos_set = [[state, p, 1] for p in pos_act]

                dataset.extend(pos_set)

                for g in gold_facts:
                    state = [q[4], context[g]]

                    pos_act = eos
                    neg_act = context
                    item = [state, pos_act, 1]
                    dataset.append(item)

                    dataset.extend([[state, n, 0] for n in neg_act])
    return dataset


def create_cross_dataset(db):
    dataset = []
    eos = "<eos>"
    for d in db:
        updates = d[0]
        questions = d[1]
        ctx = [c[1] for c in updates]

        for q in questions:

            t = q[0]
            gold_facts = q[1]
            query_type = q[3]
            context = ctx[0:t]

            if 'join' in query_type or len(gold_facts) <= 1:
                state = [q[4]]
                for g in gold_facts:
                    acts = []
                    labels = []
                    if g < t:
                        pos_act = context[g]
                    else:
                        pos_act = eos
                    neg_act = [x for i, x in enumerate(context) if i not in gold_facts]
                    acts.append(pos_act)
                    labels.append(1)

                    if pos_act is not eos:
                        acts.append(eos)
                        labels.append(0)

                    acts.extend(neg_act)
                    labels.extend([0] * len(neg_act))
                    dataset.append([state, acts, labels])
                    if pos_act is eos:
                        break
                    state.append(pos_act)

                if pos_act is not eos:
                    acts = [eos]
                    labels = [1]
                    neg_act = context
                    acts.extend(neg_act)
                    labels.extend([0] * len(neg_act))
                    dataset.append([state, acts, labels])

            else:

                state = [q[4]]

                pos_act = [context[g] or g in gold_facts]

                neg_act = [x for i, x in enumerate(context) if i not in gold_facts]
                acts = [pos_act]
                labels = [1] * len(pos_act)
                acts.append(eos)
                labels.append(0)
                acts.extend(neg_act)
                labels.extend([0] * len(neg_act))
                dataset.append([state, acts, labels])

                for g in gold_facts:
                    state = [q[4], context[g]]

                    acts = [eos]
                    labels = [1]

                    neg_act = context
                    acts.extend(neg_act)
                    labels.extend([0] * len(neg_act))
                    dataset.append([state, acts, labels])

    return dataset


def prepare_tokenizer(tokenizer):
    special_tokens = []
    special_tokens.extend(['<sep>', '<SEP>', '<eos>', '[SEP]'])
    tokenizer.add_special_tokens(
        {'additional_special_tokens': special_tokens})
