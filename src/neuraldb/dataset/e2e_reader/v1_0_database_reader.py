import random
from typing import Dict, List, Any

import logging

from neuraldb.dataset.answer_type import guess_answer_type, AnswerType
from neuraldb.dataset.database_reader import DatabaseSpecificReader
from neuraldb.dataset.e2e_reader.v0_4_database_reader import V4DatabaseSpecificReader

logger = logging.getLogger(__name__)

def new_guess_answer_type(answer):
    if isinstance(answer, bool) and answer in {"Yes", "No", "TRUE","True","False","FALSE"}:
        return AnswerType.BOOL_ANSWER
    elif answer == "None" or answer is None:
        return AnswerType.NULL_ANSWER
    elif isinstance(answer, str):
        return AnswerType.EXTRACTIVE_ANSWER
    elif isinstance(answer, int):
        return AnswerType.NUMERIC_ANSWER
    elif isinstance(answer, list):
        if len(answer):
            return AnswerType.LIST_ANSWER
        else:
            return AnswerType.EMPTY_LIST_ANSWER

    raise ValueError("Unable to determine answer type from: {}".format(answer))

class V10DatabaseSpecificReader(DatabaseSpecificReader):

    def __init__(self, filter_types=None, max_queries=None, max_list_len=10):
        super().__init__(max_queries)
        self.filter_types = filter_types if filter_types is not None else {}
        self.max_list_len = max_list_len

    @staticmethod
    def _process_answer(answer, query_type=None):
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

    def _read_query(self, query):
        # generated["qs"].append({
        #     "question": question,
        #     "answer": answer,
        #     "type": qtype,
        #     "facts": fact,
        #     "deriations": derivation,
        #     "height": height
        # })

        answer_type = new_guess_answer_type(query["answer"])
        output = query["answer"]
        return {
            "context_height": query["height"],
            "input": query["question"] if "question" in query else query["query"],
            "output": output,
            "output_type": answer_type,
            "gold_facts": query["facts"],
            "metadata": {
                "relation_type": "unknown",
                "query_type": query["type"],
                "output_type": answer_type,
            },
        }

    @staticmethod
    def _read_update(update):
        return {"text": update, "relation_type": "unknown"}

    def _load_instances(self, database: Dict[str, List[Any]]):
        logger.debug("Loading updates")
        updates = map(self._read_update, database["facts"])

        logger.debug("Loading queries")
        queries = filter(
            lambda query: query is not None,
            map(self._read_query, self._maybe_sample(database["queries"])),
        )

        return {"updates": updates, "queries": queries, "metadata": {}}
