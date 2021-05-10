from typing import List


class SearchEngine:
    def __init__(self, filter_size: int = None):
        self.updates = []
        self.filter_size = filter_size

    def set_document_database(self, updates: List[str]):
        self.updates = updates

    def add_update(self, update: str):
        self.updates.append(update)

    def clear_updates(self):
        self.updates = []

    def find_top_k(self, query: str, k: int = 5) -> List[str]:
        raise NotImplementedError()

    def filter(self, query):
        return self.find_top_k(query, self.filter_size)

    def reindex(self):
        raise NotImplementedError()
