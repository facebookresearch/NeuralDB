import json

import numpy as np
import torch.nn as nn
from sentence_transformers import SentenceTransformer, util

from ssg_utils import read_NDB_v2



model = SentenceTransformer('ssg-sentencetransformer-alldata-weighted-2.3-x10', device='cuda:0')

thresholds = [ 0.8]


folder = '../v2.3_25'
names = ['dev', 'train']
#sizes = [50, 100, 500, 1000, 2000, 5000, 7000, 10000]

#names = ['dev_queries_last_']
#sizes = [50]

softmax = nn.Softmax()
for threshold in thresholds:
    for name in names:
        data_file = folder + "/" + name + ".jsonl"

        outfile = folder + "/" + name + "_"+str(threshold)+"_st_ssg_sup.json"
        dataset = read_NDB_v2(data_file)
        ssg_data = []
        Ps = {}
        Rs = {}
        C = {}
        db_count = 0
        for d in dataset:

            questions = d[1]
            ctx = d[0]
            # input_ids = context_tokenizer(ctx, return_tensors='pt', padding=True)["input_ids"]
            # context_embeddings = dpr_context_encoder(input_ids).pooler_output

            ctx.insert(0, '<eos>')
            ctx_reps = model.encode(ctx)
            q_count = 0
            for q in questions:

                states = [[[-1, q['query']]]]
                new_states = []
                final_sets = []
                a_reps = ctx_reps[0:q['height'] + 2]
                # input_ids = question_tokenizer(q[4], return_tensors='pt')["input_ids"]
                # q_embeddings = dpr_Question_encoder(input_ids).pooler_output

                for t in range(2):

                    while states:
                        state = states.pop(0)

                        state_text = [s[1] for s in state]
                        s_text = ["[SEP]".join(state_text)]
                        s_reps = model.encode(s_text)

                        cos_scores = util.pytorch_cos_sim(s_reps, a_reps)[0]
                        cos_scores = cos_scores.cpu()

                        next_actions = np.nonzero(cos_scores > threshold).squeeze(1)
                        # print(state)

                        next_actions = next_actions.tolist()

                        if not next_actions:
                            st = state.copy()
                            final_sets.append(st[1:])

                        for a in next_actions:
                            if a == 0:
                                st = state.copy()
                                final_sets.append(st[1:])
                            else:
                                pre_acts = [pre_act[0] for pre_act in state[1:]]
                                if (a-1) not in pre_acts:
                                    new_state = state.copy()
                                    new_state.append([a - 1, ctx[a]])
                                    new_states.append(new_state)
                    states = new_states
                    new_states = []

                for s in states:
                    st = s.copy()
                    facts = st[1:]
                    if facts not in final_sets and [facts[1] , facts[0]] not in final_sets:
                        final_sets.append(st[1:])
                data = {}
                data["db_id"] = db_count
                data["question_id"] = q_count
                data["query"] = q['query']
                data["context_height"] = q['height']
                data["gold_facts"] = q['facts']
                data["answer"] = q['answer']
                data["metadata"] = {"relation_type": q['relation'], "query_type": q['type']}
                data["ssg_output"] = final_sets

                '''
                preds_set = set()

                for s in final_sets:
                    for f in s:
                        preds_set.add(f[0])

                #print(preds_set)
                #print(q['facts'])
                golds = [d in s in q['facts']]
                intersect = preds_set.intersection(set(golds))
                # print(intersect)
                if q['type'] not in Ps:
                    P = 0
                    R = 0
                    c = 1
                else:
                    P = Ps[q['type']]
                    R = Rs[q['type']]
                    c = C[q['type']] + 1
                if len(preds_set) != 0:
                    P = P + len(intersect) / len(preds_set)
                else:
                    P = P + 1

                if len(golds) == 0 or (q['answer'] == "None"):
                    R = R + 1
                else:
                    R = R + len(intersect) / len(golds)

                Ps[q['type']] = P
                Rs[q['type']] = R
                C[q['type']] = c
                '''
                ssg_data.append(data)
                q_count = q_count+1

            db_count = db_count +1
        '''
        total_p = 0
        total_r = 0
        total_c =0
        print(threshold)
        for t in Ps:
            print(t + ':')
            print(Ps[t] / C[t], Rs[t] / C[t])
            total_c = total_c + C[t]
            total_r = total_r + Rs[t]
            total_p = total_p + Ps[t]

        print('total: ')
        print(total_p/total_c , total_r/total_c)
        '''

        with open(outfile, 'w') as out_file:
            json.dump(ssg_data, out_file)
