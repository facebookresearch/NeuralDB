from ndb_data.wikidata_common.common_mongo import MongoDataSource


class KELMMongo(MongoDataSource):
    def __init__(self):
        super().__init__()
        self.collection = self.db["kelm"]

    def find_entity(self, entity):
        results = self.collection.find({"entities": entity})
        return results

    def find_entity_rel(self, entity, rels):
        results = self.collection.find(
            {"entities": entity, "relations": {"$in": list(rels)}}
        )
        return results
