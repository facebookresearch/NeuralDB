# Copyright 2018 Amazon Research Cambridge
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import argparse

import xml
from bz2 import BZ2File

import pymongo

from dataset_creation.readers.wiki_reader import WikiReader

def article_cb(title,text):
    pass

def redirect_cb(batch,title,target):

    collection.insert_one({"sitename": "enwiki",
      "title": title,
      "target": target
    })






if __name__ == "__main__":



    parser = argparse.ArgumentParser()
    parser.add_argument('--wiki_dump', required=True)
    args = parser.parse_args()

    client = pymongo.MongoClient("mongodb://jt:jt@localhost:27017")
    db = client["wikidata"]
    collection = db["wiki_redirect"]

    reader = WikiReader(lambda ns: ns == 0,
                        lambda a,b: None,
                        lambda title, target: redirect_cb(batch,title,target)
                        )
    wiki = BZ2File(args.wiki_dump)
    batch = []

    try:
        xml.sax.parse(wiki, reader)

    except Exception as e:
        print(e)

    finally:
        collection.insert_many(batch)
        client.close()






