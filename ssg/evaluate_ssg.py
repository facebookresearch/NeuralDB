import json




def find_matches(a , a_set):
    exact = 0
    soft = 0
    found = False
    for s in a_set:
        s_set = set(s)
        if a == s_set:
            exact =  1
            soft = 1
            found = True
            break
    if not found:
        for s in a_set:
            s_set = set(s)
            if a <= s_set:
                soft = 1
                break

    return exact, soft


def evaluate_ndb_with_ssg(data_file):
    with open(data_file) as json_file:
        data = json.load(json_file)

    counter = 0

    Ps_soft = {}
    Rs_soft = {}

    Ps_exact = {}
    Rs_exact = {}

    C = {}

    for d in data:
        counter = counter + 1
        gold_facts = set(d["gold_facts"])
        ssg_output = d["ssg_output"]
        answer = d["answer"]
        q_type = d["metadata"]['query_type']

        if q_type not in Ps_soft:
            P_soft = 0
            P_exact = 0
            R_soft = 0
            R_exact = 0
            c = 1
        else:
            P_soft = Ps_soft[q_type]
            R_soft = Rs_soft[q_type]
            P_exact = Ps_exact[q_type]
            R_exact = Rs_exact[q_type]
            c = C[q_type]+1


        ssg_count = 0
        gold_count = 0
        total_soft = 0
        total_exact = 0

        ssg_output = [[f[0] for f in ss] for ss in ssg_output]


        ## precision
        if len(ssg_output) == 0:
            total_soft =  1
            total_exact =  1
            ssg_count = 1

        for s in ssg_output:

            s_set = set(s)
            ssg_count = ssg_count + 1
            if 'join' in q_type or len(gold_facts) <= 1:

                if s_set == gold_facts or len(s_set) ==0:
                    total_soft = total_soft+1
                    total_exact = total_exact+1
                else:
                    if s_set > gold_facts:
                        total_soft = total_soft+1
            else:
                gold_ssg = [set([f]) for f in gold_facts]
                if s_set in gold_ssg or len(s_set) == 0:
                    total_soft = total_soft + 1
                    total_exact = total_exact + 1
                else:
                    for gold_s in gold_ssg:
                        if gold_s <= s_set:
                            total_soft = total_soft + 1
                            break
        print(total_soft/ssg_count, total_exact/ssg_count)
        P_soft = P_soft + total_soft/ssg_count
        P_exact = P_exact + total_exact/ssg_count
        total_exact = 0
        total_soft = 0
        ## Recall
        if len(gold_facts) == 0 or answer=="None":
            total_soft = 1
            total_exact = 1
            gold_count=1
        else:

            print(q_type)
            print("gold:")
            print(gold_facts)
            print("ssg:")
            print(ssg_output)
            if 'join' in q_type or len(gold_facts) == 1:
                exact, soft = find_matches(gold_facts, ssg_output)
                total_soft = total_soft + soft
                total_exact = total_exact + exact
                gold_count =1
            else:
                gold_ssg = [set([f]) for f in gold_facts]
                for g in gold_ssg:
                    gold_count = gold_count+1
                    exact, soft = find_matches(g, ssg_output)
                    total_soft = total_soft + soft
                    total_exact = total_exact + exact

        print(total_soft, total_exact)
        R_soft = R_soft + total_soft / gold_count
        R_exact = R_exact + total_exact / gold_count

        Ps_exact[q_type] = P_exact
        Rs_exact[q_type] = R_exact
        Ps_soft[q_type] = P_soft
        Rs_soft[q_type] = R_soft
        C[q_type] = c

    total_p_exact = 0
    total_r_exact = 0
    total_p_soft = 0
    total_r_soft = 0
    total_c = 0

    for t in Ps_exact:
        print(t + ':')
        print(Ps_exact[t] / C[t], Rs_exact[t] / C[t])
        print(Ps_soft[t] / C[t], Rs_soft[t] / C[t])
        total_c = total_c + C[t]
        total_r_exact = total_r_exact + Rs_exact[t]
        total_p_exact = total_p_exact + Ps_exact[t]
        total_r_soft = total_r_soft + Rs_soft[t]
        total_p_soft = total_p_soft + Ps_soft[t]

    print('total: ')
    print(total_p_exact / total_c, total_r_exact / total_c)
    print(total_p_soft / total_c, total_r_soft / total_c)


evaluate_ndb_with_ssg("../v0.5/dev.json")
