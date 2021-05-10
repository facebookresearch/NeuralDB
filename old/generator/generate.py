#!/usr/bin/env python3

import argparse
import json
import os
import random
from random import random, shuffle
from random import sample
from random import seed

import numpy as np
import re

seed(10)

relatives = ['mother', 'father', 'spouse', 'brother', 'sister']  # 'child',
relative_rel = "relative"


def gen_random(min, max):
    rand_value = int(min + (random() * (max - min)))
    return rand_value


def replace_with_article(phrase, param, value):
    regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
    if (re.search(regex, value)) and "a {}".format(param) in phrase:
        replaced = phrase.replace("a {}".format(param), "an {}".format(value))
    else:
        replaced = phrase.replace(param, value)
    return replaced


def gen_updates_queries(person, people, relations, index=0, relative=None, of_person=None):
    import random
    person_updates = []
    person_queries = []
    person_join_queries = []
    used_params = []
    person_props = {}
    relative_name = None
    if relative is not None:
        relative_name = "{}'s {}".format(of_person, relative)
        person['$relative_name'] = relative_name
        person_updates.append((index, relative, "{} is {}".format(person['$person'], relative_name)))
        person_props['$person'] = (person['$person'], 0)

    rel_inds = list(range(len(relations)))
    for i in rel_inds:
        none_question = False
        relation = relations[i]
        relation_name = relation['relation']
        params = relation['params']
        unused_params = set([p for p in params if 'pronoun' not in p])
        missing_param = len([p for p in params if (p not in person or person[p] is None) and p != '$relative_name']) > 0
        if not missing_param:
            phrase = relation['phrases'][gen_random(0, len(relation['phrases']))]

            for param in params:
                if param in phrase:
                    if param in unused_params:
                        unused_params.remove(param)
                    if param == '$born_in':
                        unused_params.remove('$country_born_in')
                        unused_params.remove('$continent_born_in')
                    if param == '$location':
                        unused_params.remove('$country_location')
                        unused_params.remove('$continent_location')
                if param in person:
                    phrase = replace_with_article(phrase, param, person[param])
                    used_params.append(param)
                    if param not in person_props:
                        person_props[param] = (person[param], len(person_updates))
                another_param = param.replace('$', '$another_')
                if phrase.find(another_param) >= 0:
                    another_param_vals = [p[param.replace('$', '')] for p in people]
                    pi = gen_random(0, len(another_param_vals))
                    another_param_val = another_param_vals[pi]
                    while another_param_val == person[param] or another_param_val is None:
                        pi = gen_random(0, len(another_param_vals))
                        another_param_val = another_param_vals[pi]
                    phrase = replace_with_article(phrase, another_param, another_param_val)

            p_index = index + len(person_updates)
            person_updates.append((p_index, relation_name, phrase))

            num_queries = 1  # min(2, len(relation['queries']))  # gen_random(1, len(relation['queries']))

            valid_q_nums = 0
            invalid_q_nums = 0
            qs = relation['queries'][:]
            random.shuffle(qs)

            if relative is not None:
                rel_queries = [q for q in qs if '$relative_name' in q[0]]
                non_rel_queries = [q for q in qs if '$relative_name' not in q[0]]
                qs = rel_queries + non_rel_queries

            for qi in range(len(qs)):
                if valid_q_nums >= num_queries:
                    break
                query = qs[qi]
                question = query[0]
                answer = query[1]
                if relative is None and ('$relative_name' in question or '$relative_name' in answer):
                    continue
                # If the question contain information that was not provided in the update. Below is wrong
                # (0, 'Mitt has a baby')
                # (1, 'What is the name of Mitt"s son?', 'Tagg')
                invalid_query = False
                if '$spoken_lang' in unused_params and '$native_lang' not in unused_params and person['$spoken_lang'] == \
                        person['$native_lang']:
                    unused_params.remove('$spoken_lang')

                for param in unused_params:
                    another_param = param.replace('$', '$another_')
                    if param in question or param in answer or another_param in question:
                        invalid_query = True
                        break
                # If a param value is mentioned in phrase and the question contains that param with a different value,
                # the answer should be "No" and not "None"
                up = [p for p in params if p not in unused_params]
                if invalid_query:
                    for param in up:
                        another_param = param.replace('$', '$another_')
                        if another_param in question and 'No' == answer:
                            invalid_query = False

                params_p = params + ['$relative_name']
                for param in params_p:
                    if param in person:
                        answer = answer.replace(param, person[param])
                        question = replace_with_article(question, param, person[param])

                    another_param = param.replace('$', '$another_')

                    if question.find(another_param) >= 0:
                        if param == '$baby_gender':
                            another_param_val = 'son' if person[param] == 'daughter' else 'daughter'
                        else:
                            if param == '$adjective':
                                another_param_vals = def_entities['$adjective']
                            else:
                                another_param_vals = [p[param.replace('$', '')] for p in people]
                            pi = gen_random(0, len(another_param_vals))
                            another_param_val = another_param_vals[pi]
                        while another_param_val == person[param] or another_param_val is None:
                            pi = gen_random(0, len(another_param_vals))
                            another_param_val = another_param_vals[pi]
                        question = replace_with_article(question, another_param, another_param_val)
                if invalid_query:
                    if invalid_q_nums == 0:
                        # To avoid too many queries, we only add one invalid questions
                        b = np.random.binomial(size=1, n=1, p=0.5)[0]
                        if not none_question and b == 1:
                            qi = create_query(
                                index=p_index + 1,
                                relation_name=relation_name,
                                question_type='join' if (
                                        relative_name is not None and relation_name in question) else 'atomic',
                                question=question,
                                answer='None/ind'
                            )
                            person_queries.append(qi)
                            none_question = True
                        invalid_q_nums += 1
                else:
                    b = np.random.binomial(size=1, n=1, p=0.5)[0]
                    update_inds = []
                    query_type = 'join' if (relative_name is not None and relative_name in question) else 'atomic'
                    if query_type == 'join':
                        update_inds.append(index)
                    update_inds.append(p_index)
                    if not none_question and b == 0:
                        qd = create_query(
                            index=p_index,
                            relation_name=relation_name,
                            question_type=query_type,
                            question=question,
                            answer='None/dep',
                            updates=update_inds
                        )
                        person_queries.append(qd)
                        none_question = True

                    update_inds = []
                    query_type = 'join' if (relative_name is not None and relative_name in question) else 'atomic'
                    if query_type == 'join':
                        update_inds.append(index)
                    update_inds.append(p_index)

                    qa = create_query(
                        index=p_index + 1,
                        relation_name=relation_name,
                        question_type='join' if (relative_name is not None and relative_name in question) else 'atomic',
                        question=question,
                        answer=answer,
                        updates=update_inds
                    )
                    person_queries.append(qa)
                    valid_q_nums += 1
    person_queries.extend(person_join_queries)
    return person_updates, person_queries, used_params, person_props


def check_country(country, def_countries):
    if country == 'England':
        country = 'United Kingdom'
    if country == 'United States of America' or country == 'USA':
        country = 'United States'
    if country not in def_countries:
        print("Country {} was not found!".format(country))
        country = None
    return country


def get_value(ent, all_ents, prop):
    if ent[prop] is not None and ent[prop] in all_ents and all_ents[ent[prop]]['name'] is not None:
        val = all_ents[ent[prop]]['name']
    else:
        val = None
    return val


def read_wiki_entities(def_orgs, def_countries, file_paths):
    people = {}
    all_ents = {}
    for f in file_paths:
        ents_ = json.load(open(f))
        all_ents.update(ents_)
    for k in all_ents:
        entity = all_ents[k]
        ent = entity
        if ent is not None and ent['type_id'] == 'Q5':
            if ent['occupation'] in all_ents and ent['place_of_birth'] in all_ents:
                org = def_orgs[gen_random(0, len(def_orgs) - 1)]
                # Q6581097: male, Q6581072:female
                ent['id'] = k
                ent['sex'] = 'M' if ent['sex_or_gender'] == 'Q6581097' else 'F'
                ent['pronoun'] = 'he' if ent['sex'] == 'M' else 'she'
                ent['poss_pronoun'] = 'his' if ent['sex'] == 'M' else 'her'
                name = ent['name'].split()[0].replace(',', '')
                ent['person'] = name
                ent['dob'] = ent['date_of_birth']
                ent['dod'] = ent['date_of_death']
                ent['educated_at'] = get_value(ent, all_ents, 'educated_at')
                ent['award_received'] = get_value(ent, all_ents, 'award_received')
                ent['member_of_sports_team'] = get_value(ent, all_ents, 'member_of_sports_team')
                ent['profession'] = None
                ent['sport'] = get_value(ent, all_ents, 'sport')
                if ent['sport'] is not None:
                    ent['sport'] = ent['sport'].replace('association', '').strip()
                else:
                    # if a person has sport, it's their profession and adding profession is redundant
                    ent['profession'] = get_value(ent, all_ents, 'occupation')
                    if ent['profession'] is not None:
                        ent['profession'] = ent['profession'].replace('film actor', 'actor').strip()
                        ent['profession'] = ent['profession'].replace('association', '').strip()
                ent['native_lang'] = get_value(ent, all_ents, 'native_language')
                ent['spoken_lang'] = get_value(ent, all_ents, 'languages_spoken_or_written')
                ent['religion'] = get_value(ent, all_ents, 'religion')
                ent['member_of_political_party'] = get_value(ent, all_ents, 'member_of_political_party')
                country = get_value(ent, all_ents, 'country_of_citizenship')
                city = None
                continent = None
                if city == "Washington D.C.":
                    country = "United States"
                if country is not None:
                    country = check_country(country, def_countries)
                    if country is not None:
                        city = def_countries[country]["capital"]
                        continent = def_countries[country]["continent"]
                if continent is None or country is None:
                    city = None
                    country = None
                ent['location'] = city
                ent['country_location'] = country
                ent['continent_location'] = continent
                birth_place_city = None
                birth_place_country = None
                birth_place_continent = None
                if all_ents[ent['place_of_birth']] is not None:
                    birth_place_city = all_ents[ent['place_of_birth']]['name']
                    if birth_place_city == "Washington D.C.":
                        birth_place_country = "United States"

                    if all_ents[ent['place_of_birth']]['desc'] is not None:
                        birth_place_country = all_ents[ent['place_of_birth']]['desc'].split(', ')[-1]
                        birth_place_country = check_country(birth_place_country, def_countries)
                    if birth_place_country is not None:
                        birth_place_continent = def_countries[birth_place_country]["continent"]
                if birth_place_country is None or birth_place_continent is None:
                    birth_place_city = None

                ent['born_in'] = birth_place_city
                ent['country_born_in'] = birth_place_country
                ent['continent_born_in'] = birth_place_continent
                ent['org'] = org
                people[k] = ent
    for k in people:
        p = people[k]
        for relative in relatives + ['child']:
            if relative in p and p[relative] in people:
                p[relative] = people[p[relative]]
            else:
                p[relative] = None

    return list(people.values())


def gen_aggregates(index, people_props):
    qs = []
    # ----------------------- $person -------------------------
    questions = {
        'set': ["List all the people in the database.", "list everyone in the database.",
                "what are the names of people in the database?"],
        'count': ["How many people are there in the database?", "What is the count of people in the database?"]
    }
    relation_name = '$person'
    ps = [p[relation_name] for p in people_props if relation_name in p]
    reps = [p[0] for p in ps]
    ps_values = [p[0] for p in ps]
    ps_updates = [p[1] for p in ps]
    qs.append(create_query(index, relation_name,
                           question_type='set',
                           question=sample(questions['set'], 1)[0],
                           answer=', '.join(ps_values), updates=ps_updates, reps=reps))
    qs.append(create_query(index, relation_name,
                           question_type='count',
                           question=sample(questions['count'], 1)[0],
                           answer=len(ps_values), updates=ps_updates, reps=reps))

    # ----------------------- $org -------------------------
    questions = {
        'set': ["List all the organisations in the database.",
                "What are the names of organisations mentioned in the database?"],
        'count': ["How many organisations are there in the database?",
                  "What is the count of organisations in the database?"]
    }
    relation_name = '$org'
    ps = [(p[relation_name][0], p[relation_name][1], p['$person']) for p in people_props if relation_name in p]
    reps = [p[0] for p in ps]
    ps_values = set([p[0] for p in ps])
    ps_updates = [p[1] for p in ps]
    qs.append(create_query(index, relation_name,
                           question_type='set',
                           question=sample(questions['set'], 1)[0],
                           answer=', '.join(ps_values), updates=ps_updates, reps=reps))
    qs.append(create_query(index, relation_name,
                           question_type='count',
                           question=sample(questions['count'], 1)[0],
                           answer=len(ps_values), updates=ps_updates, reps=reps))

    # ----------------------- $profession -------------------------
    questions = {
        'set': ["List all the professions in the database.",
                "What are all the professions in the database?"],
        'count': ["How many different professions people have in the database?",
                  "What is the count of professions in the database?"]
    }
    relation_name = '$profession'
    ps = [(p[relation_name][0], p[relation_name][1], p['$person']) for p in people_props if relation_name in p]
    reps = [p[0] for p in ps]
    ps_values = set([p[0] for p in ps])
    ps_updates = [p[1] for p in ps]
    qs.append(create_query(index, relation_name,
                           question_type='set',
                           question=sample(questions['set'], 1)[0],
                           answer=', '.join(ps_values), updates=ps_updates, reps=reps))
    qs.append(create_query(index, relation_name,
                           question_type='count',
                           question=sample(questions['count'], 1)[0],
                           answer=len(ps_values), updates=ps_updates, reps=reps))

    # ----------------------- $educated_at -------------------------
    questions = {
        'set': ["List all the colleges and universities in the database.",
                "What are all the colleges and universities in the database?"],
        'count': ["How many different colleges and universities people have the database have attended?",
                  "What is the count of all different colleges and universities in the database?"]
    }
    relation_name = '$educated_at'
    ps = [(p[relation_name][0], p[relation_name][1], p['$person']) for p in people_props if relation_name in p]
    reps = [p[0] for p in ps]
    ps_values = set([p[0] for p in ps])
    ps_updates = [p[1] for p in ps]
    qs.append(create_query(index, relation_name,
                           question_type='set',
                           question=sample(questions['set'], 1)[0],
                           answer=', '.join(ps_values), updates=ps_updates, reps=reps))
    qs.append(create_query(index, relation_name,
                           question_type='count',
                           question=sample(questions['count'], 1)[0],
                           answer=len(ps_values), updates=ps_updates, reps=reps))

    # ----------------------- $born_in -------------------------
    questions = {
        'set': ["List all the birth cities of the people in the database.",
                "What are all the birth cities of the people in the database?"],
        'count': ["How many different birth cities people in the database have?",
                  "What is the count of all birth cities of the people in the database?"]
    }
    relation_name = '$born_in'
    ps = [(p[relation_name][0], p[relation_name][1], p['$person']) for p in people_props if relation_name in p]
    reps = [p[0] for p in ps]
    ps_values = set([p[0] for p in ps])
    ps_updates = [p[1] for p in ps]
    qs.append(create_query(index, relation_name,
                           question_type='set',
                           question=sample(questions['set'], 1)[0],
                           answer=', '.join(ps_values), updates=ps_updates, reps=reps))
    qs.append(create_query(index, relation_name,
                           question_type='count',
                           question=sample(questions['count'], 1)[0],
                           answer=len(ps_values), updates=ps_updates, reps=reps))

    # ----------------------- $country_born_in -------------------------
    questions = {
        'set': ["List all the birth countries of the people in the database.",
                "What are all the birth countries of the people in the database?"],
        'count': ["How many different birth countries people in the database have?",
                  "What is the count of different birth countries of the people in the database?"]
    }
    relation_name = '$country_born_in'
    ps = [(p[relation_name][0], p[relation_name][1], p['$person'][0]) for p in people_props if relation_name in p]
    reps = [p[0] for p in ps]
    ps_values = set([p[0] for p in ps])
    ps_updates = [p[1] for p in ps]
    qs.append(create_query(index, relation_name,
                           question_type='set',
                           question=sample(questions['set'], 1)[0],
                           answer=', '.join(ps_values), updates=ps_updates, reps=reps))
    qs.append(create_query(index, relation_name,
                           question_type='count',
                           question=sample(questions['count'], 1)[0],
                           answer=len(ps_values), updates=ps_updates, reps=reps))

    #  For some of the countries ::

    all_countries = list(set([p[0] for p in ps]))
    n_sample = 2 if 2 < len(all_countries) else len(all_countries)
    unique_countries = sample(all_countries, n_sample)
    for country in unique_countries:
        pc = [p[2] for p in ps if p[0] == country]
        pc_ups = [p[1] for p in ps if p[0] == country]
        reps_country = [p[2] for p in ps if p[0] == country]
        qs.append(create_query(index, relation_name,
                               question_type='set',
                               question="List all the people who were born in {}".format(country),
                               answer=', '.join(pc), updates=pc_ups, reps=reps_country))
        qs.append(create_query(index, relation_name,
                               question_type='count',
                               question="How many people were born in {}".format(country),
                               answer=len(pc), updates=pc_ups, reps=reps_country))

    # ----------------------- $continent_born_in -------------------------
    questions = {
        'set': ["List all the birth continents of the people in the database.",
                "What are all the birth continents of the people in the database?"],
        'count': ["How many different birth continents people in the database have?",
                  "What is the count of different birth continents of the people in the database?"]
    }
    relation_name = '$continent_born_in'
    ps = [(p[relation_name][0], p[relation_name][1], p['$person'][0]) for p in people_props if relation_name in p]
    reps = [p[0] for p in ps]
    ps_values = set([p[0] for p in ps])
    ps_updates = [p[1] for p in ps]
    qs.append(create_query(index, relation_name,
                           question_type='set',
                           question=sample(questions['set'], 1)[0],
                           answer=', '.join(ps_values), updates=ps_updates, reps=reps))
    qs.append(create_query(index, relation_name,
                           question_type='count',
                           question=sample(questions['count'], 1)[0],
                           answer=len(ps_values), updates=ps_updates, reps=reps))
    #  For each continent::
    unique_continents = set([p[0] for p in ps])
    for continent in unique_continents:
        pc = [p[2] for p in ps if p[0] == continent]
        pc_ups = [p[1] for p in ps if p[0] == continent]
        reps_continent = [p[2] for p in ps if p[0] == continent]
        qs.append(create_query(index, relation_name,
                               question_type='set',
                               question="List all the people who were born in {}".format(continent),
                               answer=', '.join(pc), updates=pc_ups, reps=reps_continent))
        qs.append(create_query(index, relation_name,
                               question_type='count',
                               question="How many people were born in {}".format(continent),
                               answer=len(pc), updates=pc_ups, reps=reps_continent))

    # ----------------------- $dob -------------------------
    questions = {
        'set': ["List all the different birth years of the people in the database.",
                "What are all the different birth years of the people in the database?"],
        'count': ["How many different birth years people in the database have?",
                  "What is the count of different birth years of the people in the database?"]
    }
    relation_name = '$dob'
    ps = [(p[relation_name][0], p[relation_name][1], p['$person'][0]) for p in people_props if relation_name in p]
    reps = [p[0] for p in ps]
    ps_values = set([p[0] for p in ps])
    ps_updates = [p[1] for p in ps]
    qs.append(create_query(index, relation_name,
                           question_type='set',
                           question=sample(questions['set'], 1)[0],
                           answer=', '.join(ps_values), updates=ps_updates, reps=reps))
    qs.append(create_query(index, relation_name,
                           question_type='count',
                           question=sample(questions['count'], 1)[0],
                           answer=len(ps_values), updates=ps_updates, reps=reps))

    if len(ps) > 1:
        ps_sorted = sorted(ps, key=lambda p: int(p[0]))
        y1 = sample(list(range(len(ps_sorted) - 1)), 1)[0]
        y2 = sample(list(range(len(ps_sorted))), 1)[0]
        while y2 == y1:
            y2 = sample(list(range(len(ps_sorted))), 1)[0]
        if y1 > y2:
            a = y1
            y1 = y2
            y2 = a
        ba = [p[2] for p in ps if int(p[0]) <= int(ps_sorted[y1][0])]
        reps_ba = [p[2] for p in ps if int(p[0]) <= int(ps_sorted[y1][0])]
        ps_updates_ba = [p[1] for p in ps if int(p[0]) <= int(ps_sorted[y1][0])]
        # ba = [p[2] for p in ps_sorted[:y1 + 1]]
        qs.append(create_query(index, relation_name,
                               question_type='set',
                               question="List all the people who were born before or in {}.".format(ps_sorted[y1][0]),
                               answer=', '.join(ba), updates=ps_updates_ba,
                               reps=reps_ba))
        qs.append(create_query(index, relation_name,
                               question_type='count',
                               question="Count all the people who were born before or in {}.".format(ps_sorted[y1][0]),
                               answer=len(ba), updates=ps_updates_ba,
                               reps=reps_ba))

        aa = [p[2] for p in ps if int(p[0]) > int(ps_sorted[y2][0])]
        reps_aa = [p[2] for p in ps if int(p[0]) > int(ps_sorted[y2][0])]
        ps_updates_aa = [p[1] for p in ps if int(p[0]) > int(ps_sorted[y2][0])]
        # aa = [p[2] for p in ps_sorted[y2 + 1:]]
        qs.append(create_query(index, relation_name,
                               question_type='set',
                               question="List all the people who were born after {}.".format(ps_sorted[y2][0]),
                               answer=', '.join(aa), updates=ps_updates_aa,
                               reps=reps_aa))
        qs.append(create_query(index, relation_name,
                               question_type='count',
                               question="Count all the people who were born after {}.".format(ps_sorted[y2][0]),
                               answer=len(aa), updates=ps_updates_aa, reps=reps_aa))

        abb = [p[2] for p in ps if int(ps_sorted[y1][0]) < int(p[0]) < int(ps_sorted[y2][0])]
        reps_abb = [p[2] for p in ps if int(ps_sorted[y1][0]) < int(p[0]) < int(ps_sorted[y2][0])]
        ps_updates_abb = [p[1] for p in ps if int(ps_sorted[y1][0]) < int(p[0]) < int(ps_sorted[y2][0])]
        qs.append(create_query(index, relation_name,
                               question_type='set',
                               question="List all the people who were born after {} and before {}.".format(
                                   ps_sorted[y1][0],
                                   ps_sorted[y2][
                                       0]),
                               answer=', '.join(abb), updates=ps_updates_abb,
                               reps=reps_abb))
        qs.append(create_query(index, relation_name,
                               question_type='count',
                               question="Count all the people who were born after {} and before {}.".format(
                                   ps_sorted[y1][0],
                                   ps_sorted[y2][0]),
                               answer=len(abb), updates=ps_updates_abb,
                               reps=reps_abb))

        reps_arg = [(p[2], p[0]) for p in ps]
        youngest = [p[2] for p in ps if int(ps_sorted[-1][0]) == int(p[0])]
        qs.append(create_query(index, relation_name,
                               question_type='min/max',
                               question="Who is the youngest person in the database?",
                               answer=', '.join(youngest), updates=ps_updates, reps=reps_arg))
        oldest = [p[2] for p in ps if int(ps_sorted[0][0]) == int(p[0])]
        qs.append(create_query(index, relation_name,
                               question_type='min/max',
                               question="Who is the oldest person in the database?",
                               answer=', '.join(oldest), updates=ps_updates,
                               reps=reps_arg))

    return qs


def create_query(index=None, relation_name=None, question_type=None, question=None, answer=None, updates=[], reps=[]):
    if index is None or relation_name is None or question_type is None or question is None or answer is None:
        raise Exception('All parameters are required')
    if question_type in ['atomic', 'join']:
        boolean_type = False
        bool_q_words = ["Does ", "Did ", "Was ", "Is ", "Can "]
        for bw in bool_q_words:
            if question.startswith(bw):
                boolean_type = True
                break
        if boolean_type:
            question_type += "_boolean"
        else:
            question_type += "_extractive"
    q = (index, updates, relation_name.replace('$', ''), question_type, question, answer, reps)
    return q


def create_update(index, relation_name, statement):
    u = (index, relation_name, statement)
    return u


def gen_people(humans, wiki_people, def_relations, def_entities, update_size):
    def populate_person(p):
        person = {
            '$person': p['person'],
            '$sex': p['sex'],
            '$pronoun': p['pronoun'],
            '$desc': p['desc'],
            '$poss_pronoun': p['poss_pronoun'],
            '$org': p['org'],
            '$dob': p['dob'],
            '$dod': p['dod'],
            '$educated_at': p['educated_at'],
            '$award_received': p['award_received'],
            '$member_of_sports_team': p['member_of_sports_team'],
            'member_of_political_party': p['member_of_political_party'],
            'religion': p['religion'],
            '$sport': p['sport'].replace('association', '').strip() if p['sport'] is not None else None,
            '$profession': p['profession'] if p['profession'] is not None else None,
            '$spoken_lang': p['spoken_lang'],
            '$native_lang': p['native_lang'],
            '$location': p['location'],
            '$country_location': p['country_location'],
            '$continent_location': p['continent_location'],
            '$born_in': p['born_in'],
            '$country_born_in': p['country_born_in'],
            '$continent_born_in': p['continent_born_in'],
            '$with_person': p['spouse']['person'] if p['spouse'] is not None else None,
            '$when': def_entities['$when'][sample(range(len(def_entities['$when'])), 1)[0]],
            '$is_word': def_entities['$is_word'][sample(range(len(def_entities['$is_word'])), 1)[0]],
            '$adjective': def_entities['$adjective'][sample(range(len(def_entities['$adjective'])), 1)[0]],
            '$period': def_entities['$period'][sample(range(len(def_entities['$period'])), 1)[0]],
        }
        baby_gender = None
        baby_poss_pronoun = None
        baby_name = None
        if p['child'] is not None and 'sex' in p['child']:
            baby_gender = 'son' if p['child']['sex'] == 'M' else 'daughter'
            baby_poss_pronoun = 'his' if p['child']['sex'] == 'M' else 'her'
            baby_name = p['child']['person']

        person['$baby_gender'] = baby_gender
        person['$baby_poss_pronoun'] = baby_poss_pronoun
        person['$baby_name'] = baby_name

        return person

    db_updates = []
    db_queries = []

    friends = set()
    update_ind = 0

    friends_with_spouse = []
    friends_sex = []
    friends_city = []
    friends_country = []
    friends_continent = []
    friends_dob = []

    people_props = []

    while update_ind < update_size and len(humans) > 0:
        h = humans.pop()
        ps = [wp for wp in wiki_people if wp['id'] == h]
        if len(ps) > 0:
            p = ps[0]
        else:
            continue
        person = populate_person(p)
        if p['person'] not in friends:
            friends.add(p['person'])
            fsex = 'female' if p['sex'] == 'F' else 'male'
            person_updates, person_queries, used_params, person_props = gen_updates_queries(person, wiki_people,
                                                                                            def_relations)  # update_ind
            people_props.append({k: (v[0], (v[1] + update_ind)) for k, v in person_props.items()})
            if len(person_updates) > 0:
                friends_sex.append((p['person'], fsex))
                if p['dob'] is not None and '$dob' in used_params:
                    friends_dob.append((p['person'], int(p['dob'])))
                if '$location' in used_params:
                    friends_city.append((p['person'], p['location']))
                    friends_country.append((p['person'], p['country_location']))
                    friends_continent.append((p['person'], p['continent_location']))

            for relative in relatives:
                rp = p[relative]
                if rp is not None:
                    inv_rel = None
                    relative_person = populate_person(p[relative])
                    if relative_person['$person'] != person['$person']:
                        if relative == 'child':
                            inv_rel = '$mother' if p['sex'] == 'F' else '$father'
                        elif relative in ['mother', 'father']:
                            inv_rel = '$child'
                            relative_person['$baby_gender'] = None
                            relative_person['$baby_poss_pronoun'] = None
                            relative_person['$baby_name'] = None
                        elif relative == 'spouse':
                            spouse = 'husband' if relative_person['$sex'] == 'M' else 'wife'
                            friends_with_spouse.append((person['$person'], spouse))
                            friends_with_spouse.append((person['$person'], 'spouse'))
                            friends_with_spouse.append((person['$person'], 'partner'))
                            inv_rel = '$spouse'
                        elif relative in ['brother', 'sister']:
                            inv_rel = '$sister' if p['sex'] == 'F' else '$brother'
                        relative_person[inv_rel] = None  # person['$person']
                        relative_person['$' + inv_rel] = None  # person['$person']

                        friends.add(relative_person['$person'])
                        rel_sex = 'female' if relative_person['$sex'] == 'F' else 'male'
                        rel_updates, rel_queries, rel_used_params, rel_props = gen_updates_queries(relative_person,
                                                                                                   wiki_people,
                                                                                                   def_relations,
                                                                                                   index=len(
                                                                                                       person_updates),
                                                                                                   relative=relative,
                                                                                                   of_person=p[
                                                                                                       'person'])
                        people_props.append(
                            {k: (v[0], (v[1] + update_ind + len(person_updates))) for k, v in rel_props.items()})
                        if len(rel_updates) > 0:
                            friends_sex.append((relative_person['$person'], rel_sex))
                            if '$location' in rel_used_params:
                                friends_city.append((relative_person['$person'], relative_person['$location']))
                                friends_country.append(
                                    (relative_person['$person'], relative_person['$country_location']))
                                friends_continent.append(
                                    (relative_person['$person'], relative_person['$continent_location']))
                            if relative_person['$dob'] is not None and '$dob' in rel_used_params:
                                friends_dob.append((relative_person['$person'], int(relative_person['$dob'])))
                        if inv_rel == '$spouse':
                            inv_rel = 'wife' if p['sex'] == 'F' else 'husband'
                        inv_rel_q = create_query(index=len(person_updates) + len(rel_updates),
                                                 relation_name=relative,  # 'inv_rel',
                                                 question_type='atomic',
                                                 question="Who is {}'s {}?".format(relative_person['$person'],
                                                                                   inv_rel.replace('$', '')),
                                                 answer=person['$person'],
                                                 updates=[len(person_updates)])
                        rel_queries.append(inv_rel_q)
                        person_updates.extend(rel_updates)
                        person_queries.extend(rel_queries)

            db_updates.append(person_updates)
            db_queries.append(person_queries)
            update_ind = sum([len(u) for u in db_updates])

    update_ind = sum([len(u) for u in db_updates])
    set_count_qs = gen_aggregates(update_ind, people_props)
    db_updates.append([])
    db_queries.append(set_count_qs)

    # len_updates = update_ind  # sum([len(u) for u in db_updates])
    # agg_queries = generate_aggregation_list_queries(friends_continent, friends_country, friends_dob, friends_sex,
    #                                                 friends_with_spouse, len_updates)
    # db_updates.append([])
    # db_queries.append(agg_queries)
    return db_updates, db_queries


def generate_aggregation_list_queries(friends_continent, friends_country, friends_dob, friends_sex, friends_with_spouse,
                                      len_updates):
    aggs_dict = {
        "spouse": {
            "friends": friends_with_spouse,
            "list": ["Who are people who have spouses?", "Who are people with partners?",
                     "list people who have spouses.", "list people with partners."],
            "count": ["How many people have spouses?", "How many people with partners exist?",
                      "Count everyone who has a spouse.", "Count everyone who has a partner."],
            "values": ['spouse']
        },
        "sex": {
            "friends": friends_sex,
            "list": ["Who are my {} friends?", "Who are my friends who are {}?",
                     "list all my friends who are {}.", "list all my {} friends."],
            "count": ["How many {} friends do I have?", "How many of my friends are {}s?",
                      "Count all my friends who are {}s.", "Count my {} friends."],
            "values": ['male', 'female']
        },
        "country_location": {
            "friends": friends_country,
            "list": ["Who are my friends who live in {}?", "Who are my friends who are located in {}?",
                     "list all my friends who live in {}.", "list all my friends that are located in {}."],
            "count": ["How many of my friends live in {}?",
                      "Count all my friends who live in {}."],
            "values": list(set([fr[1] for fr in friends_country]))
        },
        "continent_location": {
            "friends": friends_continent,
            "list": ["Who are my friends who live in {}?", "Who are my friends who are located in {}?",
                     "list all my friends who live in {}.", "list all my friends that are located in {}."],
            "count": ["How many of my friends live in {}?",
                      "Count all my friends who live in {}."],
            "values": list(set([c["continent"] for k, c in def_countries.items()]))
        }
    }
    agg_queries = []
    for key_agg in aggs_dict:
        agg_item = aggs_dict[key_agg]
        if len(agg_item["values"]) > 0:
            m = min(len(agg_item["values"]), 2)
            values = sample(agg_item["values"], m)
            for value in values:
                friends_agg = [af[0] for af in agg_item["friends"] if af[1] == value]

                list_q = sample(agg_item["list"], 1)[0].format(value)
                count_q = sample(agg_item["count"], 1)[0].format(value)

                list_query = create_query(index=len_updates, relation_name=key_agg, question_type='set',
                                          question=list_q,
                                          answer=', '.join(friends_agg))
                count_query = create_query(index=len_updates, relation_name=key_agg, question_type='agg',
                                           question=count_q,
                                           answer=len(friends_agg))

                agg_queries.append(list_query)
                agg_queries.append(count_query)
    # Min/Max queries
    male_friends = [f[0] for f in friends_sex if f[1] == 'male']
    female_friends = [f[0] for f in friends_sex if f[1] == 'female']
    sorted_friends_dob = sorted(friends_dob, key=lambda t: t[1])
    male_friends_sorted = [fd for fd in sorted_friends_dob if fd[0] in male_friends]
    female_friends_sorted = [fd for fd in sorted_friends_dob if fd[0] in female_friends]
    min_max = {
        "youngest_friend": mix_max_age(sorted_friends_dob, mode='min'),
        "oldest_friend": mix_max_age(sorted_friends_dob, mode='max'),
        "youngest_male_friend": mix_max_age(male_friends_sorted, mode='min'),
        "youngest_female_friend": mix_max_age(female_friends_sorted, mode='min'),
        "oldest_male_friend": mix_max_age(male_friends_sorted, mode='max'),
        "oldest_female_friend": mix_max_age(female_friends_sorted, mode='max'),
    }
    min_max_keys = sample(list(min_max.keys()), 2)
    for min_max_key in min_max_keys:
        q = "Who is my " + min_max_key.replace("_", " ") + "?"
        a = min_max[min_max_key]
        if a is not None:
            mm_query = create_query(index=len_updates, relation_name='born_in', question_type='min_max', question=q,
                                    answer=', '.join(a))
            agg_queries.append(mm_query)
    return agg_queries


def mix_max_age(friends, mode='min'):
    if len(friends) == 0:
        return None
    min_max_val = friends[-1][1] if mode == 'min' else friends[0][1]
    all_friends_val = [f[0] for f in friends if f[1] == min_max_val]
    return all_friends_val


def gen_db(data):
    # data is a collection of personal DBs
    formatted_data = []

    for d in data:
        # each personal DB contains a list of peron's updates and queries, for different people
        ups_, qrs_ = d
        db_updates = []
        db_queries = []
        ind = 0
        for i in range(len(ups_)):
            person_ups = ups_[i]
            person_qrs = qrs_[i]

            for p_up in person_ups:
                db_updates.append((p_up[0] + ind, p_up[1]))
            for p_q in person_qrs:
                db_queries.append((p_q[0] + ind, p_q[1], p_q[2].replace('/ind', '').replace('/dep', '')))
            ind += len(person_ups)

        formatted_data.append({'updates': db_updates, 'queries': db_queries})
    return formatted_data


def gen_qs_at_end(data):
    # data is a collection of personal DBs
    formatted_data = []

    for d in data:
        # each personal DB contains a list of peron's updates and queries, for different people
        ups_, qrs_ = d
        db_updates = []
        db_queries = []
        end_qs = []
        ind = 0
        len_all_ups = sum([len(up) for up in ups_])
        for i in range(len(ups_)):
            person_ups = ups_[i]
            person_qrs = qrs_[i]

            # updates
            for p_up in person_ups:
                db_updates.append((p_up[0] + ind, p_up[1], p_up[2]))
            # queries
            for q in person_qrs:
                # print(q)
                if q[3] not in ['set', 'count', 'min/max']:
                    q_up_inds = [ui + ind for ui in q[1]]
                else:
                    q_up_inds = q[1]
                    if len(q[1]) != len(q[6]):
                        print("ERROR in LENGTH!!")
                if q[-2] == 'None/dep':
                    db_queries.append((q[0] + ind, q_up_inds, q[2], q[3], q[4], 'None', q[6]))
                elif q[-2] == 'None/ind':
                    end_qs.append((len_all_ups, q_up_inds, q[2], q[3], q[4], 'None', q[6]))
                else:
                    end_qs.append((len_all_ups, q_up_inds, q[2], q[3], q[4], q[5], q[6]))
            ind += len(person_ups)

        db_queries.extend([(q[0], q[1], q[2], q[3], q[4], q[5], q[6]) for q in end_qs])
        formatted_data.append({'updates': db_updates, 'queries': db_queries})
    return formatted_data


def gen_shuff_qs_at_end(data):
    # data is a collection of personal DBs
    formatted_data = []

    for d in data:
        # each personal DB contains a list of peron's updates and queries, for different people
        ups_, qrs_ = d

        inds = list(range(len(ups_)))  # index from 0 to number of people in this DB
        shuffle(inds)
        ups_shuff = [ups_[i] for i in inds]
        qrs_shuff = [qrs_[i] for i in inds]

        db_updates = []
        db_queries = []
        end_qs = []
        ind = 0
        for i in range(len(ups_shuff)):
            person_ups = ups_shuff[i]
            person_qrs = qrs_shuff[i]
            # updates
            for p_up in person_ups:
                db_updates.append((p_up[0] + ind, p_up[1]))
            # queries
            for q in person_qrs:
                if q[2] == 'None/dep':
                    db_queries.append((q[0] + ind, q[1], 'None'))
                elif q[2] == 'None/ind':
                    end_qs.append((0, q[1], 'None'))
                else:
                    end_qs.append((0, q[1], q[2]))

            ind += len(person_ups)

        db_queries.extend([(ind, q[1], q[2]) for q in end_qs])
        formatted_data.append({'updates': db_updates, 'queries': db_queries})
    return formatted_data


def get_all_json_data(files, fdir):
    jd = {}
    for f in files:
        jdi = json.load(open(os.path.join(fdir, f)))
        jd.update(jdi)
    return jd


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-num_humans", type=int, default=1000)
    parser.add_argument("-version", type=float, default=0.5)
    parser.add_argument("-updates", type=list, default=[50, 100, 500, 1000, 2000, 5000, 7000, 10000])
    parser.add_argument("-q", type=str, default="end")
    args = parser.parse_args()

    num_humans = args.num_humans
    update_sizes = args.updates
    version = args.version
    queries_at_the_end = True if args.q == 'end' else False

    out_path = '../data/gen/v{}/'.format(version)
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    def_orgs = [o.replace('\n', '') for o in open('in/orgs.txt').readlines()]
    def_entities = json.load(open('in/entities.json', 'r'))
    def_countries = json.load(open('in/countries_continents.json', 'r'))
    def_relations = json.load(open('in/relations.json', 'r'))

    # fdir = "/Users/marzieh/Documents/work/wikidata/data/{}_humans".format(num_humans)
    # initial_human_files = [f for f in os.listdir(fdir) if "_entities_{}_humans.json".format(num_humans) in f]
    # all_ent_files = [os.path.join(fdir, f) for f in os.listdir(fdir) if f.endswith(".json")]
    # json.dump(get_all_json_data(initial_human_files, fdir), open('in/main_humans.json', 'w'))
    # json.dump(get_all_json_data(all_ent_files, fdir), open('in/all_entities.json', 'w'))

    main_humans = list(json.load(open('in/main_humans.json')).keys())
    n_train = int(len(main_humans) * 0.8)
    n_dev = int(len(main_humans) * 0.1)
    n_test = len(main_humans) - n_train - n_dev
    wiki_ents = read_wiki_entities(def_orgs, def_countries, file_paths=['in/all_entities.json'])
    for update_size in update_sizes:
        sets = {
            'train': main_humans[:n_train],
            'dev': main_humans[n_train:n_train + n_dev],
            'test': main_humans[n_train + n_dev:]
        }
        for set_name in sets:
            data = []
            set_humans = sets[set_name]
            while len(set_humans) > 0:
                ind_updates, ind_queries = gen_people(set_humans, wiki_ents, def_relations, def_entities, update_size)
                data.append((ind_updates, ind_queries))
            if queries_at_the_end:
                dbs = gen_qs_at_end(data)
                with open("../data/gen/v{}/{}_queries_last_{}.json".format(version, set_name, update_size), 'w') as f:
                    json.dump(dbs, f, indent=True)
            else:
                dbs = gen_db(data)
                # shuffle the data
                # qs_at_end_shuff1 = gen_shuff_qs_at_end(data)
                # with open("../data/gen/v{}/{}_queries_last_shf1.json".format(version, set_name), 'w') as f:
                #     json.dump(qs_at_end_shuff1, f, indent=True)
                # # shuffle the data
                # qs_at_end_shuff2 = gen_shuff_qs_at_end(data)
                # with open("../data/gen/v{}/{}_queries_last_shf2.json".format(version, set_name), 'w') as f:
                #     json.dump(qs_at_end_shuff2, f, indent=True)
