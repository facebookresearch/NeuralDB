import logging

import json
import os
import random
from abc import ABC

from neuraldb.dataset.abstract_reader import AbstractReader
from neuraldb.dataset.answer_type import guess_answer_type
from neuraldb.dataset.database_reader import DatabaseSpecificReader
from neuraldb.dataset.instance_generator import InstanceGenerator
from neuraldb.dataset.e2e_reader.v0_2_database_reader import V2DatabaseSpecificReader
from neuraldb.dataset.e2e_generator.seq2seq_reader import Seq2SeqSpecificGenerator
from neuraldb.dataset.search_engines.tfidf import TFIDFSearchEngine

logger = logging.getLogger(__name__)


class NeuralDatabaseDatasetReader(AbstractReader):
    def __init__(
        self,
        database_reader: DatabaseSpecificReader,
        instance_generator: InstanceGenerator,
    ):
        self.database_reader = database_reader
        self.instance_generator = instance_generator

    def read(self, file_path):
        logger.info("Reading instances from {}".format(file_path))
        with open(file_path) as f:
            databases = json.load(f)

        logger.info("Dataset file contains {} databases".format(len(databases)))

        for idx, database in enumerate(databases):
            logger.info(
                "Loading updates and queries from database {} of {}".format(
                    idx, len(databases)
                )
            )
            loaded_database = self.database_reader.load_instances(database)

            yield from self.instance_generator.generate(loaded_database)

            if os.getenv("DEBUG", None) is not None and idx > 3:
                break

class NeuralDatabaseV1DatasetReader(AbstractReader):
    def __init__(
        self,
        database_reader: DatabaseSpecificReader,
        instance_generator: InstanceGenerator,
    ):
        self.database_reader = database_reader
        self.instance_generator = instance_generator

    def read(self, file_path):
        logger.info("Reading instances from {}".format(file_path))
        with open(file_path) as f:
            for idx, line in enumerate(f):
                database = json.loads(line)
                loaded_database = self.database_reader.load_instances(database)
                yield from self.instance_generator.generate(loaded_database)

                if os.getenv("DEBUG", None) is not None and idx > 3:
                    break

class NeuralDatabaseDatasetPipelineReader(AbstractReader):
    def __init__(self, instance_generator: InstanceGenerator):
        self.instance_generator = instance_generator

    def read(self, file_path):
        logger.info("Reading instances from {}".format(file_path))
        with open(file_path) as f:
            for instance in json.load(f):

                question_tokens = self.instance_generator._tokenizer.tokenize(
                    instance["question"]
                )
                contexts = [
                    a[1]
                    for a in sorted(
                        instance["context-score"], key=lambda a: a[2], reverse=True
                    )
                ]
                context_tokens = [
                    self.instance_generator._tokenizer.tokenize(context)
                    for context in contexts
                ]

                answer_preprocessed = self._preprocess_answer(
                    instance["answer"], instance["metadata"]["query_type"]
                )
                answer_type = guess_answer_type(
                    answer_preprocessed, instance["metadata"]["query_type"]
                )
                answer = self.instance_generator._preprocess_answer(
                    answer_preprocessed, answer_type
                )
                yield from self.instance_generator._generate_instances(
                    context_tokens,
                    question_tokens,
                    answer,
                    {
                        "query_type": instance["metadata"]["query_type"],
                        "output_type": answer,
                        "gold_facts": instance["gold_facts"],
                        "context_height": instance["context_height"],
                        "relation_type": instance["metadata"]["relation_type"],
                    },
                )

    @staticmethod
    def _preprocess_answer(answer, query_type=None):
        if isinstance(answer, int):
            return str(answer)
        elif isinstance(answer, str):
            if "," in answer and query_type in {"list", "set"}:
                return [a.strip() for a in answer.split(",")]
            else:
                return answer
        elif isinstance(answer, list):
            return [str(a).strip() for a in answer]

        raise ValueError(
            "Unknown answer type. Got {} for {} but expected one of: <int, str, list>".format(
                type(answer), answer
            )
        )


class NeuralDatabaseDatasetPipelineSSGReader(AbstractReader):
    def __init__(self, instance_generator: InstanceGenerator):
        self.instance_generator = instance_generator

    def read(self, file_path):
        logger.info("Reading instances from {}".format(file_path))
        with open(file_path) as f:
            for idx, instance in enumerate(json.load(f)):

                for group in instance["ssg_output"]:
                    question_tokens = self.instance_generator._tokenizer.tokenize(
                        instance["question"]
                    )
                    contexts = [a[1] for a in group]

                    if len(contexts) == 0:
                        answer_preprocessed = self._preprocess_answer(
                            "None", instance["metadata"]["query_type"]
                        )
                    else:
                        answer_preprocessed = self._preprocess_answer(
                            instance["answer"], instance["metadata"]["query_type"]
                        )

                    context_tokens = [
                        self.instance_generator._tokenizer.tokenize(context)
                        for context in contexts
                    ]
                    answer_type = guess_answer_type(
                        answer_preprocessed, instance["metadata"]["query_type"]
                    )

                    answer = self.instance_generator._preprocess_answer(
                        answer_preprocessed, answer_type
                    )
                    yield from self.instance_generator._generate_instances(
                        context_tokens,
                        question_tokens,
                        answer,
                        {
                            "query_type": instance["metadata"]["query_type"],
                            "output_type": answer,
                            "gold_facts": instance["gold_facts"],
                            "context_height": instance["context_height"],
                            "relation_type": instance["metadata"]["relation_type"],
                            "qnum": idx,
                        },
                    )

    @staticmethod
    def _preprocess_answer(answer, query_type=None):
        if isinstance(answer, int):
            return str(answer)
        elif isinstance(answer, str):
            if "," in answer and query_type in {"list", "set"}:
                return [a.strip() for a in answer.split(",")]
            else:
                return answer
        elif isinstance(answer, list):
            return [str(a).strip() for a in answer]

        raise ValueError(
            "Unknown answer type. Got {} for {} but expected one of: <int, str, list>".format(
                type(answer), answer
            )
        )


class NeuralDatabaseDatasetShuffleReader(NeuralDatabaseDatasetReader):
    def read(self, file_path):
        logger.info("Reading instances from {}".format(file_path))
        with open(file_path) as f:
            databases = json.load(f)

        logger.info("Dataset file contains {} databases".format(len(databases)))

        iterators = []
        for idx, database in enumerate(databases):
            logger.info(
                "Loading updates and queries from database {} of {}".format(
                    idx, len(databases)
                )
            )
            loaded_database = self.database_reader.load_instances(database)
            iterators.append(self.instance_generator.generate(loaded_database))
            if os.getenv("DEBUG", None) is not None and idx > 3:
                break

        while len(iterators):
            it = random.choice(iterators)
            try:
                nxt = next(it)
                yield from nxt
            except StopIteration:
                iterators.remove(it)


class NeuralDatabaseDatasetSingleReader(NeuralDatabaseDatasetReader):
    def __init__(
        self,
        database_reader: DatabaseSpecificReader,
        instance_generator: InstanceGenerator,
        db_id,
    ):

        super().__init__(database_reader, instance_generator)
        self.db_id = db_id

    def read(self, file_path):
        logger.info("Reading instances from {}".format(file_path))
        with open(file_path) as f:
            # databases = json.load(f)
            for idx,  line in enumerate(f):
                # loaded_database = self.database_reader.load_instances(databases[self.db_id])
                if idx == self.db_id:
                    loaded_database = json.loads(line)
                    yield from self.instance_generator.generate(loaded_database)


        # logger.info("Dataset file contains {} databases".format(len(databases)))
        #
        # logger.info(
        #     "Loading updates and queries from database {} of {}".format(
        #         self.db_id, len(databases)
        #     )
        # )



if __name__ == "__main__":

    from log_helper import setup_logging
    from transformers import AutoTokenizer

    setup_logging()
    tokenizer = AutoTokenizer.from_pretrained("t5-base")

    v2 = V2DatabaseSpecificReader()
    seq2seq = Seq2SeqSpecificGenerator(tokenizer, update_search=TFIDFSearchEngine())
    reader = NeuralDatabaseDatasetReader(v2, seq2seq)

    for instance in reader.read("v0.2/dev_queries_last_50.json"):
        print(instance.label_toks, instance.label_ids)
        print(seq2seq.pad(instance).decoder_input_ids)
