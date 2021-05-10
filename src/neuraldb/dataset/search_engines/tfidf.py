from typing import List, Optional

import math
from drqascripts.retriever.build_tfidf_lines import OnlineTfidfDocRanker
from neuraldb.search_engine import SearchEngine


class TFIDFSearchEngine(SearchEngine):
    class RankArgs:
        def __init__(self, cache_bits):
            self.ngram = 2
            self.hash_size = int(math.pow(2, cache_bits))
            self.tokenizer = "simple"
            self.num_workers = None

    def __init__(self, filter_size: int = 5):
        super().__init__(filter_size)
        self.onlineranker_args = self.RankArgs(24)
        self.ranker: Optional[OnlineTfidfDocRanker] = None

    def find_top_k(self, query: str, k: int = 5) -> List[str]:
        assert self.ranker is not None, "Database has not yet been indexed"
        return self.ranker.closest_docs(query, k)[0]

    def reindex(self):
        self.ranker = OnlineTfidfDocRanker(self.onlineranker_args, self.updates)
