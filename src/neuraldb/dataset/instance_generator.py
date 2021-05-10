import itertools
import logging
from collections import defaultdict
from functools import reduce
from operator import itemgetter
from typing import List

from tqdm import tqdm
from transformers import PreTrainedTokenizer
from neuraldb.dataset.search_engines.return_all import ReturnAll
from neuraldb.search_engine import SearchEngine

logger = logging.getLogger(__name__)


class InstanceGenerator(object):
    empty_context_special = "[EMPTY_CONTEXT]"

    null_answer_special = "[NULL_ANSWER]"
    empty_list_answer_special = "[EMPTY_LIST_ANSWER]"
    yes_answer_special = "[YES_ANSWER]"
    no_answer_special = "[NO_ANSWER]"

    def __init__(
        self,
        tokenizer: PreTrainedTokenizer,
        update_search: SearchEngine = ReturnAll(),
        context_limit: int = 256,
        unlimited_budget: bool = False,
        iterate: bool = False,
        is_oracle: bool = False,
    ) -> object:

        logger.info("Generating instances with {} tokenizer".format(repr(tokenizer)))
        self._tokenizer = tokenizer
        self.update_search = update_search

        logger.info("Adding special token types")
        self._tokenizer.add_tokens(self.empty_context_special)
        self._tokenizer.add_tokens(self.null_answer_special)
        self._tokenizer.add_tokens(self.empty_list_answer_special)
        self._tokenizer.add_tokens(self.yes_answer_special)
        self._tokenizer.add_tokens(self.no_answer_special)

        self._context_limit = context_limit
        self._delimiter_tokens = []

        logger.info("Iterator instance generator")
        self.iterate = iterate

        self.is_oracle = is_oracle

        self.unlimited_budget = unlimited_budget

    def generate(self, database):
        return self._generate(database)

    def concatenate_context(self, context):
        # TODO check this fit in the context limit
        return (
            list(itertools.chain(*context))
            if len(context)
            else [self.empty_context_special]
        )

    def filter_context(self, updates, context_height, budget, search_results=None):
        # TODO later we might want to split into multiple contexts

        # For debugging, if we have no search results, return the entire DB as a single search result
        if search_results is None:
            return [updates[:context_height]]

        filtered = []

        flattened = defaultdict(int)
        for result in search_results:
            if isinstance(result,list):
                for i in result:
                    flattened[i] += 1
            else:
                flattened[result] += 1

        for idx, result in enumerate(
            filter(lambda result: result < context_height, flattened.keys())
        ):

            tokens = updates[result]
            remaining = sum(len(a) for a in filtered) + len(
                self._delimiter_tokens
            ) * len(filtered)
            if budget is not None and len(tokens) + remaining > budget:
                if len(filtered) == 0:
                    filtered.append(tokens[:remaining])
                break
            else:
                filtered.append(tokens)

        return [filtered]

    def maybe_tokenize_db(self, db_text):
        return map(self._tokenizer.tokenize, db_text)

    def _generate(self, database):
        if not self.is_oracle:
            db_text = list(map(itemgetter("text"), database["updates"]))
            update_tokens = list(self.maybe_tokenize_db(db_text))
            self.update_search.set_document_database(db_text)
            self.update_search.reindex()

            for query in database["queries"]:
                query_tokens = self._tokenizer.tokenize(query["input"])
                answer = self._preprocess_answer(query["output"], query["output_type"])
                context_height = query["context_height"]

                budget = (
                    self._context_limit - (len(query_tokens) + 1 + 2)
                    if not self.unlimited_budget
                    else None
                )

                search_query = query["input"]
                all_results = []
                orignal_results = []

                for i in range(5 if self.iterate else 1):
                    len_before = len(all_results)
                    search_results = self.update_search.filter(search_query)
                    if not len(all_results):
                        orignal_results = search_results

                    if search_results is None:
                        all_results = None
                        break
                    else:
                        all_results.extend(
                            [a for a in search_results if a not in all_results]
                        )
                        search_query = " ".join(
                            [query["input"]]
                            + [
                                self._tokenizer.convert_tokens_to_string(
                                    update_tokens[i]
                                )
                                for i in all_results
                            ]
                        )

                        if len_before >= len(all_results):
                            break

                filtered_contexts = self.filter_context(
                    update_tokens, context_height, budget, all_results
                )
                meta = {}
                if "metadata" in query:
                    meta.update(query["metadata"])
                meta["query"] = query
                meta["search_results"] = all_results
                for context in filtered_contexts:
                    yield from self._generate_instances(
                        context, query_tokens, answer, meta
                    )
        else:
            facts = list(database["updates"])
            db_text = list(map(itemgetter("text"), facts))
            update_tokens = list(self.maybe_tokenize_db(db_text))

            for query in tqdm(database["queries"]):
                query_tokens = self._tokenizer.tokenize(query["input"])
                answer = self._preprocess_answer(query["output"], query["output_type"])
                context_height = query["context_height"]

                budget = (
                    self._context_limit - (len(query_tokens) + 1 + 2)
                    if not self.unlimited_budget
                    else None
                )
                filtered_contexts = self.filter_context(
                    update_tokens, context_height, budget, query["gold_facts"]
                )

                meta = {}
                if "metadata" in query:
                    meta.update(query["metadata"])
                meta["query"] = query
                meta["search_results"] = query["gold_facts"]

                for context in filtered_contexts:
                    yield from self._generate_instances(
                        context, query_tokens, answer, meta
                    )

    def _generate_instances(self, all_context, query, answer, metadata=None):
        raise NotImplementedError("not implemented")

    def _preprocess_answer(self, answer, answer_type):
        raise NotImplementedError("Not implemented")

    def apply_padding(self, toks: List[int], limit=None):
        if limit is None:
            limit = self._context_limit

        # assert len(toks)<=limit, "Was expecting token sequence to be under the limit of {}. But instead got {} which is {} tokens long".format(limit,toks,len(toks))

        padding = [0] * (limit - len(toks))
        return toks + padding

    def pad(self, example):
        raise NotImplementedError()
