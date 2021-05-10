import logging
import random
from typing import Dict, List, Any

logger = logging.getLogger(__name__)


class DatabaseSpecificReader:
    def __init__(self, max_queries=None):
        self._max_queries = max_queries

    def load_instances(self, database: Dict[str, List[Any]]):
        return self._load_instances(database)

    def _load_instances(self, database: Dict[str, List[Any]]):
        raise NotImplementedError

    def _maybe_sample(self, queries: List[Any]):
        if self._max_queries is not None:
            queries = random.sample(queries, min(len(queries), self._max_queries))
        return queries
