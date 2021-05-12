
import json
import logging
import os

logger = logging.getLogger(__name__)

class Reader():

    def read(self, path):
        logger.info("reading instances from {}".format(path))

        with open(path) as f:
            for idx, line in enumerate(f):
                instance = json.loads(line)
                yield from self.generate_instances(instance)

                if os.getenv("DEBUG") is not None and idx > 10:
                    break


    def generate_instances(self, instance):
        raise NotImplementedError()