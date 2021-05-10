import json
import logging
from neuraldb.dataset.abstract_reader import AbstractReader
from neuraldb.dataset.instance_generator import InstanceGenerator

logger = logging.getLogger(__name__)


class UnaryOperatorReader(AbstractReader):
    def __init__(self, generator: InstanceGenerator):
        self.generator: InstanceGenerator = generator

    def read(self, file_path):
        logger.info("Reading instances from {}".format(file_path))
        with open(file_path) as f:
            instances = (json.loads(line) for line in f)
            yield from self.generator.generate(instances)
