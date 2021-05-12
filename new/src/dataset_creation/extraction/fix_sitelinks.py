import pymongo
from pymongo import UpdateOne
from tqdm import tqdm


def write_updates(batch_update):
    bulks = []
    for k,v in batch_update:
        bulks.append(UpdateOne(k,v))

    collection.bulk_write(bulks)


if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://jt:jt@localhost:27017")
    db = client["wikidata"]
    collection = db["wiki_graph"]

    batch_update = []

    num_ops = 0
    tqdm_iter = tqdm(collection.find({},{"_id":1,"sitelinks" : 1}), total=collection.estimated_document_count())
    for i in tqdm_iter:
        if type(i["sitelinks"]) == dict:
            batch_update.append(({"_id":i["_id"]}, {"$set": {"sitelinks":list(i["sitelinks"].values())}}))

        if len(batch_update) > 10000:
            write_updates(batch_update)
            batch_update = []
            num_ops += 1
            tqdm_iter.desc = f"Performed update {num_ops}"

