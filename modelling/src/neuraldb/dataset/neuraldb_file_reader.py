import json
import logging
import os

from neuraldb.dataset.instance_generator.instance_generator import InstanceGenerator
from neuraldb.dataset.neuraldb_parser import NeuralDBParser

logger = logging.getLogger(__name__)


class NeuralDBFileReader:
    def __init__(self, instance_generator: InstanceGenerator):
        self.database_reader = NeuralDBParser()
        self.instance_generator = instance_generator

    def read(self, file_path):
        logger.info("Reading instances from {}".format(file_path))

        database_count = 0
        with open(file_path) as f:
            for idx, line in enumerate(f):
                database_count += 1
                database = json.loads(line)

                loaded_database = self.database_reader.load_instances(database)
                yield from self.instance_generator.generate(
                    loaded_database, database_idx=idx
                )

                if os.getenv("DEBUG", None) is not None and idx > 3:
                    break

        logger.info("Dataset file contains {} databases".format(database_count))
