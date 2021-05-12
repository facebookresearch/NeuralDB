import os
from abc import ABC

import pymongo


class MongoDataSource(ABC):
    def __init__(self):
        user = os.getenv("MONGO_USER", "")
        password = os.getenv("MONGO_PASSWORD", "")
        host = os.getenv("MONGO_HOST", "localhost")
        port = os.getenv("MONGO_PORT", "27017")
        db = os.getenv("MONGO_DB","wikidata")

        client = pymongo.MongoClient(f"mongodb://{user}:{password}@{host}:{port}")

        self.db = client[db]