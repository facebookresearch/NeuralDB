import json

from wikidata_common.wikidata import Wikidata


def load_line(qa_dataset):
    with open(qa_dataset) as f:
        for line in f:
            instance = json.loads(line)
            yield instance

asked_questions = set()
def process_instances(lines):
    for line in lines:
        query_type = line["type"]

        if "negative" in query_type:
            continue

        if line["query"] in asked_questions:
            continue

        relation = wikidata.get_by_id_or_uri(line["prop"])["english_name"]
        filters = []

        subject = wikidata.get_by_id_or_uri(line["subject"])
        if subject["english_name"] in line["query"] or subject["english_wiki"] in line["query"]:
            filters.append(subject['english_name'])

        if line["object"].startswith("Q"):
            object = wikidata.get_by_id_or_uri(line["object"])
            if object["english_name"] in line["query"] or object["english_wiki"] in line["query"]:
                filters.append(object['english_name'])
        else:
            if line["object"] in line["query"]:
                filters.append(line["object"])

        if len(filters):
            filter_str = "filters: " + (" ".join(filters))
        else:
            filter_str = ""

        yield {
            "metadata": {
                "original": line
            },
            "target": line["query"],
            "source": f"query: {query_type} relation: {relation} {filter_str}".strip()

        }


if __name__ == "__main__":
    wikidata = Wikidata()
    for idx,i in enumerate(process_instances(load_line("../NeuralDB/generated_clean_train.jsonl"))):
        asked_questions.add(i["target"])
        print(i["source"])
        print(i["target"])
        print("**************")
        if idx>10000:
            break