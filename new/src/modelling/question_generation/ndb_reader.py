import json
from functools import reduce

from modelling.reader import Reader


def space(_sep):
    return " " + _sep + " "


class NDBReader(Reader):

    def __init__(self,tokenizer, path):
        super().__init__()
        self.path = path
        self._sep = "[QSP]"
        self.tokenizer = tokenizer
        self.special_tokens = ["[SEP]","[QRY]"]

    def __iter__(self):
        with open(self.path) as f:
            for line in f:
                yield from self.generate_instances(json.loads(line))

    def generate_instances(self, instance):
        # fact_tokens = list(map(self.tokenizer.tokenize, instance["facts"]))

        for query in instance["queries"]:
            # query_tokens = self.tokenizer.tokenize(query["question"])

            context = instance["facts"][:query['height']]
            context = space("[SEP]").join(context)

            if query["answer"] is None or None in query["answer"] or len(query["answer"]) == 0:
                answer = "[NULL_ANSWER]"
            else:
                answer = " [SEP] ".join(str(a) for a in query['answer'])

            # answer_tokens = self.tokenizer.tokenize(answer)
            a = {
                "source": query["question"] + " [QRY] " + context,
                "target": answer,
                "instance": instance
            }

            yield a