from typing import List

import torch

from neuraldb.models.cnn_encoder import CNNEncoder
from neuraldb.search_engine import SearchEngine
from neuraldb.sparsemax import Sparsemax


class MaximumInnerProductSearch(SearchEngine):
    def __init__(self, tokenizer, query_encoder, qcnn, dcnn):
        super().__init__()
        self.tokenizer = tokenizer
        self._encoder = query_encoder

        self._q_cnn = qcnn
        self._d_cnn = dcnn
        self.is_prob_distribution = False

        if self.is_prob_distribution:
            self.sparsemax = Sparsemax()

    def apply_padding(self, toks: List[int], limit=48):
        padding = [0] * (limit - len(toks))
        return toks + padding

    def find_top_k(self, query: str, k: int = 5) -> List[str]:
        query_tokens = self.tokenizer.encode(query)
        q_toks = torch.LongTensor([self.apply_padding(query_tokens)])

        q_outputs = self._encoder(
            q_toks.to(self._encoder.device),
            attention_mask=(q_toks > 0).to(self._encoder.device),
        )

        query_emb = (
            self._q_cnn(
                q_outputs,
                mask=torch.LongTensor(
                    [[a > 0 for a in self.apply_padding(query_tokens)]]
                ).to(self._encoder.device),
            )
            if self._q_cnn is not None
            else q_outputs[1]
        )

        if len(self.updates):
            doc_enc = self.tokenizer.batch_encode_plus(self.updates)
            doc_tokens = doc_enc["input_ids"]

            max_len_batch = max(len(t) for t in doc_tokens)
            d_toks = torch.LongTensor(
                [self.apply_padding(t, max_len_batch) for t in doc_tokens]
            )
            d_outputs = self._encoder(
                d_toks.to(self._encoder.device),
                attention_mask=(d_toks > 0).to(self._encoder.device),
            )
            doc_emb = (
                self._d_cnn(
                    d_outputs,
                    mask=torch.LongTensor(
                        [
                            [a > 0 for a in self.apply_padding(t, max_len_batch)]
                            for t in doc_tokens
                        ]
                    ).to(self._encoder.device),
                )
                if self._d_cnn is not None
                else d_outputs[1]
            )

            scores = torch.bmm(
                query_emb.unsqueeze(1), doc_emb.unsqueeze(0).transpose(1, 2)
            ).squeeze()

            scaled_mips = scores / (query_emb.norm(p=2) * doc_emb.norm(dim=1, p=2))

            if self.is_prob_distribution:
                if len(scores.shape) == 0:
                    scaled_mips = self.sparsemax(scores.unsqueeze(0))
                else:
                    scaled_mips = self.sparsemax(scores)

            assert not (self._encoder.training and scaled_mips.grad_fn is None)
            return scaled_mips.cpu()

        return torch.FloatTensor().cpu()

    def filter(self, query):
        return self.updates

    def reindex(self):
        pass
