import glob
import json

from tqdm import tqdm

if __name__ == "__main__":
    files = glob.glob("complex_*")

    with open("all_questions_merged_complex_3", "w+") as out_file:
        global_idx = dict()
        for file in tqdm(files):
            with open(file) as f:
                for line in f:
                    instance = json.loads(line)

                    if (file,instance["idx"]) not in global_idx:
                        global_idx[(file,instance["idx"])] = len(global_idx)

                    instance["idx"] = global_idx[(file,instance["idx"])]
                    out_file.write(json.dumps(instance)+"\n")
