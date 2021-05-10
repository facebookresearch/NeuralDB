import torch


def ScaledTokensEvidenceCombiner():
    def _resolve_context(self, context, query_string, query_tokens):
        self.update_search.set_document_database(context)
        scores = self.update_search.find_top_k(query_string)
        sort_scores = scores.sort(descending=True)

        toks = self._tokenizer.batch_encode_plus(context, add_special_tokens=False)

        if "input_ids" in toks:
            filtered_sents, filtered_indices = self.aa_filter_context(
                toks["input_ids"],
                self._context_limit - len(query_tokens) - 1 - 2,
                sort_scores[1],
            )
            concat_context = self.concatenate_context(filtered_sents)
            # scale = torch.cat([torch.FloatTensor(len(tokens) * [scores[page_index]]) for tokens, page_index in zip(filtered_sents, filtered_indices)])

            if len(filtered_sents) > 0:
                scale = torch.cat(
                    [
                        scores[page_index].repeat(len(tokens))
                        for tokens, page_index in zip(filtered_sents, filtered_indices)
                    ]
                )
                assert not (
                    self.update_search._encoder.training and scale.grad_fn is None
                )

                pad_scale = torch.cat(
                    [
                        torch.FloatTensor(
                            (len(self.concatenate_context(filtered_sents)) - len(scale))
                            * [1.0]
                        ),
                        scale,
                        torch.FloatTensor(
                            (self._context_limit - len(concat_context)) * [1.0]
                        ),
                    ]
                )
                assert len(pad_scale) == self._context_limit

                return (
                    self._tokenizer.encode_plus(
                        concat_context, ["[QRY] "] + query_tokens, is_pretokenized=True
                    ),
                    pad_scale,
                )

        return (
            self._tokenizer.encode_plus(
                ["[QRY] "] + query_tokens, is_pretokenized=True
            ),
            torch.FloatTensor(self._context_limit * [1.0]),
        )
