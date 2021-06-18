#
# Copyright (c) 2021 Facebook, Inc. and its affiliates.
#
# This file is part of NeuralDB.
# See https://github.com/facebookresearch/NeuralDB for further info.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import json
import re
from argparse import ArgumentParser
from collections import defaultdict
from tqdm import tqdm
from wikidata_common.wikidata import Wikidata
from wikidata_common.wikpedia import Wikipedia


def clean(name):
    return (
        name.replace("( ", "(")
        .replace(" )", ")")
        .replace(" + ", "+")
        .replace(" : ", ":")
        .replace(" ,", ",")
        .replace(" !", "!")
        .replace(" -- ", "–")
        .replace(" 's", "'s")
    )


def clean_title(name):
    return name.replace(" 's", "'s").replace("--", "-")


def find_longest_match(searches, search_key, restrict_relation=False):
    search_toks = []
    for s in searches:
        search_toks.append(s[1])

    ents = wikidata.find_custom(search_key, search_toks)
    highest_query_index = None

    n_count = defaultdict(set)
    for result in ents:

        if restrict_relation and result["wikidata_id"].strip()[0] != "P":
            continue
        elif not restrict_relation and result["wikidata_id"].strip()[0] != "Q":
            continue

        if "." in search_key:
            first, second = search_key.split(".", maxsplit=1)

            for nested in result[first]:
                try:
                    query_index = search_toks.index(nested[second])

                    n_count[nested[second]].add(result["wikidata_id"])

                    if highest_query_index is None or highest_query_index < query_index:
                        highest_query_index = query_index
                        # ent_id = result["wikidata_id"]
                except ValueError:
                    pass
        else:
            query_index = search_toks.index(result[search_key])
            n_count[result[search_key]].add(result["wikidata_id"])

            if highest_query_index is None or highest_query_index < query_index:
                highest_query_index = query_index
                # ent_id = result["wikidata_id"]

    return (
        search_toks[highest_query_index] if highest_query_index is not None else None,
        list(n_count[search_toks[highest_query_index]])
        if highest_query_index is not None
        else None,
        highest_query_index if highest_query_index is not None else -1,
    )


def resolve_redirect(searches):
    return wikipedia.resolve_redirect(searches)


def final_period(item):
    if item[-1] != "." and "." in item:
        return item + "."
    return item


def lookup_entity(searches):
    # redirs = resolve_redirect(searches)
    # searches.extend(redirs)
    toks, eid, pos = find_longest_match(searches, "english_wiki", False)
    # if toks is not None:
    #     toks = searches[[len(s[1].split()) for s in searches].index(len(toks.split()))][1]

    if toks is None or eid is None:
        toks, eid, pos = find_longest_match(searches, "sitelinks.title", False)
        # if toks is not None:
        #     toks = searches[[len(s[1].split()) for s in searches].index(len(toks.split()))][1]

    if toks is None or eid is None:
        toks, eid, pos = find_longest_match(searches, "english_name", False)
        # if toks is not None:
        #     toks = searches[[len(s[1].split()) for s in searches].index(len(toks.split()))][1]

    return toks, eid, pos


def lookup_relation(searches):
    toks, eid, pos = find_longest_match(searches, "english_name", True)
    if toks is None or eid is None:
        toks, eid, pos = find_longest_match(searches, "sitelinks.title", True)

    return toks, eid, pos


def get_longest(toks, start, restrict_relation=False):
    if start >= len(toks):
        return None, None, 0, 0

    search_str = ""
    searches = []

    for tok_len, tok in enumerate(toks):
        if tok_len < start:
            continue

        if len(searches) == 0 and (tok.startswith("+") or tok == "+"):
            return clean(" ".join(toks[tok_len:])), "numeric", start, tok_len

        search_str += tok + " "
        query = clean(search_str).strip()
        searches.append((tok_len, query))

    final_start = start
    if restrict_relation:
        text, id, pos = lookup_relation(searches)
        if text is None or id is None:
            text, id, final_start, pos = get_longest(toks, start + 1, restrict_relation)

        if text == "participant" and " ".join(toks[start:]).startswith(
            "participant of"
        ):
            pos += 1

    else:
        text, id, pos = lookup_entity(searches)

    return text, id, final_start, pos + start


def try_recovery(name):
    date_groups = re.match(
        r"^([0-9]{2}) ?(January|February|March|April|May|June|July|"
        r"August|September|October|November|December)? ([0-9]{1,4})$",
        name,
    )
    if date_groups is not None:
        year = date_groups.group(3)
        month = date_groups.group(2)
        day = date_groups.group(1)

        if day != "00":
            return (date_groups.group(0), {"day": day, "month": month, "year": year})
        elif month is not None:
            return (
                " ".join((date_groups.group(2), date_groups.group(3))),
                {"year": year, "month": month},
            )
        else:
            return (date_groups.group(3), {"year": year})

    searches = [
        [0, clean(name)],
        [0, clean_title(name)],
        [0, final_period(name)],
        [0, final_period(clean(name))],
        [0, final_period(clean_title(name))],
    ]

    toks, eid, pos = find_longest_match(searches, "english_wiki", False)

    if toks is None or eid is None:
        toks, eid, pos = find_longest_match(searches, "sitelinks.title", False)

    if toks is None or eid is None:
        toks, eid, pos = find_longest_match(searches, "english_name", False)

    if toks is not None and eid is not None:
        return (toks, eid)

    res = clean_title(name)
    resolved = resolve_redirect([res, clean_title(res), clean(res)])
    for r in resolved:
        text, id, tmp_start, tmp_end = get_longest(r.split(), 0, False)
        if tmp_end + 1 - tmp_start == len(r.split()):
            return (text, id)

    return None


def resolve_first_ref(ref):
    ref = ref.replace("$COMMA$", ",")
    toks = ref.split()

    parsed = []
    next_id = 0
    is_relation = False

    iteration = 0
    prev_end = 0
    while next_id < len(toks) and iteration <= 2:
        iteration += 1

        text, resolved_id, startptr, nextptr = get_longest(
            toks, next_id, restrict_relation=is_relation
        )

        if toks[next_id] == ",":
            next_id += 1
            continue

        if text is not None and resolved_id is not None:
            next_id = nextptr + 1
            is_relation = not is_relation
            parsed.append((text, resolved_id))

            # Fix previous resolution
            if prev_end != startptr:
                recovered = try_recovery(" ".join(toks[:startptr]))
                if recovered is not None:
                    parsed[-2] = recovered
                else:

                    print(f"Failed to fix {ref}")
                    print(parsed)
                    del parsed[-2]

            elif len(parsed) >= 3:
                # Fix this resolution
                aa = clean(" ".join(toks[startptr:])).split()
                if len(parsed[-1][0].split()) < len(aa):
                    recovery = try_recovery(" ".join(toks[startptr:]))
                    if recovery is not None:
                        parsed[-1] = recovery
                    else:
                        print(f"Failed to fix2 {ref}")
                        print(parsed)
                        del parsed[-1]

            prev_end = nextptr + 1
            if len(parsed) >= 3:
                break

        else:
            if len(parsed) > 1:
                print(ref)
                print("Early stop")
                print(toks[next_id:])
                print(parsed)
                print()
                break

    return parsed


def resolve_later_ref(subject, ref):
    ref = ref.replace("$COMMA$", ",")
    toks = ref.split()

    parsed = []
    next_id = 0
    is_relation = True

    iteration = 0
    prev_end = 0

    parsed.append(subject)

    while next_id < len(toks) and iteration <= 2:
        iteration += 1

        text, resolved_id, startptr, nextptr = get_longest(
            toks, next_id, restrict_relation=is_relation
        )

        if toks[next_id] == ",":
            next_id += 1
            continue

        if text is not None and resolved_id is not None:
            next_id = nextptr + 1
            is_relation = not is_relation
            parsed.append((text, resolved_id))

            # Fix previous resolution
            if prev_end != startptr:
                recovered = try_recovery(" ".join(toks[:startptr]))
                if recovered is not None:
                    parsed[-2] = recovered
                else:

                    print(f"Failed to fix (later) {ref}")
                    print(parsed)
                    del parsed[-2]

            elif len(parsed) >= 3:
                # Fix this resolution
                aa = clean(" ".join(toks[startptr:])).split()
                if len(parsed[-1][0].split()) < len(aa):
                    recovery = try_recovery(" ".join(toks[startptr:]))
                    if recovery is not None:
                        parsed[-1] = recovery
                    else:
                        print(f"Failed to fix2 (later) {ref}")
                        print(parsed)
                        del parsed[-1]

            prev_end = nextptr + 1
            if len(parsed) >= 3:
                break

        else:
            if len(parsed) > 1:
                print(ref)
                print("Early stop")
                print(toks[next_id:])
                print(parsed)
                print()
                break

    return parsed


if __name__ == "__main__":
    wikipedia = Wikipedia()
    wikidata = Wikidata()

    parser = ArgumentParser()
    parser.add_argument("in_file")
    parser.add_argument("out_file")
    parser.add_argument("err_file")
    args = parser.parse_args()

    with open(args.in_file) as f, open(args.out_file, "w+") as of, open(
        args.err_file, "w+"
    ) as ef:
        for line in tqdm(f, total=1000000):
            instance = json.loads(line)
            instance["parse_targets"] = []

            refs = (
                instance["reference"]
                .strip()
                .rstrip(".")
                .replace(" , ", " $COMMA$ ")
                .replace(", ", " , ")
            )
            ref = refs.split(" , ")

            parsed = resolve_first_ref(ref[0])
            instance["parses"] = [parsed]
            instance["error_parses"] = []
            instance["parse_targets"].append(ref[0])

            if len(parsed) != 3:
                ef.write(json.dumps(instance) + "\n")
                continue

            for next_ref in ref[1:]:
                if "start time" in next_ref or "end time" in next_ref:
                    continue

                parsed = resolve_later_ref(parsed[0], next_ref)
                if len(parsed) == 3:
                    instance["parses"].append(parsed)
                else:
                    instance["error_parses"].append(parsed)

                instance["parse_targets"].append(next_ref)

            if len(parsed) == 3:
                of.write(json.dumps(instance) + "\n")
