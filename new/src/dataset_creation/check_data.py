import json

if __name__ == "__main__":
    with open("v1.7_train") as f:
        for line in f:
            db = json.loads(line)


            for query in db["queries"]:
                if "complex" in query["type"]:
                    print(query['facts'])
                    if len(query['facts']):
                        for xq in query['facts']:
                            print([db['facts'][i] for i in xq])
                    print(query['question'])
                    print(query['answer'])
                    print()


