import json

from modelling.reader import Reader


def space(_sep):
    return " " + _sep + " "


class QGReader(Reader):

    def __init__(self,path):
        super().__init__()
        self.path = path
        self._sep = "[QSP]"
        self.special_tokens = [self._sep]

    def __iter__(self):
        with open(self.path) as f:
            for line in f:
                yield from self.generate_instances(json.loads(line))

    def generate_instances(self, instance):

        a = {
            "source": space(self._sep).join(str(i) for i in instance["input"]),
            "target": space(self._sep).join(str(o) for o in instance["output"]),
            "instance": instance
        }

        yield a