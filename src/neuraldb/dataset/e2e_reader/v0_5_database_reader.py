import random
from typing import Dict, List, Any

import logging

from neuraldb.dataset.answer_type import guess_answer_type, AnswerType
from neuraldb.dataset.database_reader import DatabaseSpecificReader
from neuraldb.dataset.e2e_reader.v0_4_database_reader import V4DatabaseSpecificReader

logger = logging.getLogger(__name__)


class V5DatabaseSpecificReader(V4DatabaseSpecificReader):
    def _read_query(self, query):
        processed_ans = self._process_answer(query[5], query[3])
        answer_type = guess_answer_type(processed_ans, query[3])

        if query[2] in self.filter_types or query[3] in self.filter_types:
            return None

        if answer_type == AnswerType.LIST_ANSWER and (
            self.max_list_len is not None and len(processed_ans) > self.max_list_len
        ):
            logger.error(
                "Could not include query because it would return a very long list. \nQuery: {}\nAnswer ({}): {}".format(
                    query[4], len(processed_ans), query[5]
                )
            )
            return None

        return {
            "context_height": query[0],
            "input": query[4],
            "output": processed_ans,
            "output_type": answer_type,
            "gold_facts": query[1],
            "metadata": {
                "relation_type": query[2],
                "query_type": query[3],
                "output_type": answer_type,
            },
        }


class V5D2DatabaseSpecificReader(V5DatabaseSpecificReader):
    def _read_query(self, query):

        if len(query[6]) == 0:
            query[5] = str(query[5]).replace("/dep", "")
            processed_ans = self._process_answer(query[5], query[3])
            answer_type = guess_answer_type(processed_ans, query[3])

            inp = query[1]

            if answer_type == AnswerType.NULL_ANSWER:

                if len(query[1]) and query[1][0] > 1:
                    fid = random.uniform(-1, query[1][0] - 1)
                    fid = int(fid)

                    if fid >= 0:
                        inp = [fid]
                    else:
                        inp = []

                else:
                    inp = []

            yield {
                "context_height": query[0],
                "input": query[4],
                "output": processed_ans,
                "output_type": answer_type,
                "gold_facts": inp,
                "metadata": {
                    "relation_type": query[2],
                    "query_type": query[3],
                    "output_type": answer_type,
                },
            }

        else:

            assert len(query[1]) == len(query[6])
            for fact, output in zip(query[1], query[6]):
                processed_ans = self._process_answer(output, None)
                answer_type = guess_answer_type(processed_ans, query[3])

                yield {
                    "context_height": query[0],
                    "input": query[4],
                    "output": processed_ans,
                    "output_type": answer_type,
                    "gold_facts": [fact],
                    "metadata": {
                        "relation_type": query[2],
                        "query_type": query[3],
                        "output_type": answer_type,
                    },
                }

    def _load_instances(self, database: Dict[str, List[Any]]):
        logger.debug("Loading updates")
        updates = map(self._read_update, database["updates"])

        logger.debug("Loading queries")
        queries = []
        for query in database["queries"]:
            xgen = self._read_query(query)
            if xgen is None:
                continue
            for inst in xgen:
                if inst is not None:
                    queries.append(inst)

        return {"updates": updates, "queries": queries, "metadata": {}}
