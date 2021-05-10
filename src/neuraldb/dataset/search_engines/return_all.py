from typing import List

from neuraldb.search_engine import SearchEngine


class ReturnAll(SearchEngine):
    def find_top_k(self, query: str, k: int = 5) -> List[str]:
        raise NotImplementedError

    def filter(self, query):
        # If we return None, the context filter will use all items and not care about adding to a budget
        return None #list(range(len(self.updates)))

    def reindex(self):
        pass
