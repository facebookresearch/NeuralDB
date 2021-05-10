from typing import Dict, List, Any

import logging

from neuraldb.dataset.answer_type import guess_answer_type, AnswerType
from neuraldb.dataset.database_reader import DatabaseSpecificReader

logger = logging.getLogger(__name__)


class V4DatabaseSpecificReader(DatabaseSpecificReader):
    def __init__(self, filter_types=None, max_queries=None, max_list_len=10):
        super().__init__(max_queries)
        self.filter_types = filter_types if filter_types is not None else {}
        self.max_list_len = max_list_len

    @staticmethod
    def _read_update(update):
        return {"text": update[2], "relation_type": update[1]}

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
        processed_ans = self._process_answer(query[4], query[2])
        answer_type = guess_answer_type(processed_ans, query[2])

        if query[1] in self.filter_types or query[2] in self.filter_types:
            return None

        if answer_type == AnswerType.LIST_ANSWER and (
            self.max_list_len is not None and len(processed_ans) > self.max_list_len
        ):
            logger.error(
                "Could not include query because it would return a very long list. \nQuery: {}\nAnswer ({}): {}".format(
                    query[3], len(processed_ans), query[4]
                )
            )
            return None

        return {
            "context_height": query[0],
            "input": query[3],
            "output": processed_ans,
            "output_type": answer_type,
            "metadata": {
                "relation_type": query[1],
                "query_type": query[2],
                "output_type": answer_type,
            },
        }

    def _load_instances(self, database: Dict[str, List[Any]]):
        logger.debug("Loading updates")
        updates = map(self._read_update, database["updates"])

        logger.debug("Loading queries")
        queries = filter(
            lambda query: query is not None,
            map(self._read_query, self._maybe_sample(database["queries"])),
        )

        return {"updates": updates, "queries": queries, "metadata": {}}
