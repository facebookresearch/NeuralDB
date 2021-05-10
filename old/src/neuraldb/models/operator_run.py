from neuraldb.dataset.unary_operator_reader import UnaryOperatorReader
from neuraldb.models.seq2seqargs_operator import Seq2seqOperatorTrainer


class RunSeq2seqOperatorTrainer(Seq2seqOperatorTrainer):
    def __init__(self, hparams):
        # Call parent of the seq2seq model to init pytorch
        super(Seq2seqOperatorTrainer, self).__init__(hparams)
        self.em = 0
        self.source_length = self.hparams.max_source_length
        self.target_length = self.hparams.max_target_length

        self.metrics = {"validation": []}

        special_tokens = []
        for i in range(0, 101):
            special_tokens.append("<extra_id_" + str(i) + ">")

        special_tokens.extend(["NDB:"])
        self.tokenizer.add_special_tokens({"additional_special_tokens": special_tokens})

        self.bad_words = [
            [self.tokenizer.convert_tokens_to_ids(bad_word)]
            for bad_word in self.tokenizer.additional_special_tokens
        ]

        self.data_generator = self.construct_generator()
        self.reader = UnaryOperatorReader(self.data_generator)
        self.model.resize_token_embeddings(len(self.tokenizer))
