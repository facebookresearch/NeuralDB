from typing import Dict, List, Any

import logging

from neuraldb.dataset.answer_type import guess_answer_type
from neuraldb.dataset.database_reader import DatabaseSpecificReader

logger = logging.getLogger(__name__)


class V2DatabaseSpecificReader(DatabaseSpecificReader):
    def _read_update(self, update):
        return {"text": update[1]}

    def _read_query(self, query):
        return {
            "context_height": query[0],
            "input": query[1],
            "output": query[2],
            "output_type": guess_answer_type(query[2]),
        }

    def _load_instances(self, database: Dict[str, List[Any]]):
        logger.debug("Loading updates")
        updates = map(self._read_update, database["updates"])

        logger.debug("Loading queries")
        queries = map(self._read_query, self._maybe_sample(database["queries"]))

        return {"updates": updates, "queries": queries, "metadata": {}}
