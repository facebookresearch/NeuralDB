import json
import os

from transformers import RobertaTokenizer


def NDB_to_extraction(data_dir, output_dir, type_path, sep_token):
    data_file = os.path.join(data_dir, type_path + ".json")

    classification_file = open(os.path.join(output_dir, type_path + ".classification"), 'w')
    span_file = open(os.path.join(output_dir, type_path + ".spans"), 'w')

    with open(data_file) as json_file:
        data = json.load(json_file)

    for d in data:
        updates = [u[1] for u in d['updates']]
        questions = d['queries']
        for q in questions:
            t = int(q[0])
            question = q[1]
            answer = q[2]
            label = answer
            print(label)
            if (answer != "Yes") & (answer != "No") & (answer != "None"):
                label = "Span"

            question_string = question
            context_string = ""
            context = updates[0:t]
            context.reverse()
            for u in context:
                context_string += u + " " + sep_token + " "
            classification_file.write(question_string + "\t" + context_string + "\t" + label + '\n')
            if label == "Span":
                span_file.write(question_string + "\t" + context_string + "\t" + answer + '\n')
    classification_file.close()
    span_file.close()


if __name__ == "__main__":
    tokenizer = RobertaTokenizer.from_pretrained("roberta-base")
    NDB_to_extraction('../data/gen/v0', '../data/gen/v0', 'dev', tokenizer.sep_token)
    NDB_to_extraction('../data/gen/v0', '../data/gen/v0', 'train', tokenizer.sep_token)
    NDB_to_extraction('../data/gen/v0', '../data/gen/v0', 'test', tokenizer.sep_token)
