from ndb_data.wikidata_common.common_mongo import MongoDataSource


class Wikidata(MongoDataSource):
    def __init__(self):
        super().__init__()
        self.collection = self.db["wiki_graph"]

    def get_by_id_or_uri(self, unit_uri):
        return self.collection.find_one(
            {"wikidata_id": unit_uri.replace("http://www.wikidata.org/entity/", "")}
        )

    def find_custom(self, search_key, search_toks):
        return self.collection.find({search_key: {"$in": search_toks}})

    def find_matching_relation(self, relation):
        return self.collection.find({"propery_types": relation})
