from ndb_data.wikidata_common.common_mongo import MongoDataSource


class Wikipedia(MongoDataSource):
    def __init__(self):
        super().__init__()
        self.collection = self.db["wiki_redirects"]

    def resolve_redirect(self, names):
        results = self.collection.find({"title": {"$in": names}})
        new_search = []
        for res in results:
            new_search.append(res["target"])
        return new_search
