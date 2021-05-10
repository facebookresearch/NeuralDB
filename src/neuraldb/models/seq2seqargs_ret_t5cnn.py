import logging
from abc import ABC
from transformers import AutoConfig, T5Tokenizer
from neuraldb.dataset.search_engines.mips import MaximumInnerProductSearch
from neuraldb.models.cnn_encoder import CNNEncoder
from neuraldb.models.modelling_t2point5 import T2Point5Model
from neuraldb.models.seq2seqargs import Seq2seqTrainer
from neuraldb.models.seq2seqargs_ret import Seq2seqTrainerRet

logger = logging.getLogger(__name__)


class Seq2seqTrainerRetT5CNN(Seq2seqTrainerRet):
    def construct_retriever(self):
        tok = T5Tokenizer.from_pretrained(self.hparams.t5_type)

        auto_config = AutoConfig.from_pretrained(self.hparams.t5_type)

        self.tok_model = T2Point5Model.from_pretrained(
            self.hparams.t5_type,
            config=auto_config,
        )

        self.query_cnn = CNNEncoder(64, self.hparams.cnn_filters)
        self.doc_cnn = CNNEncoder(64, self.hparams.cnn_filters)

        return MaximumInnerProductSearch(
            tok, self.tok_model, self.query_cnn, self.doc_cnn
        )

    @staticmethod
    def add_model_specific_args(parser, root_dir):
        Seq2seqTrainerRet.add_model_specific_args(parser, root_dir)

        parser.add_argument(
            "--cnn_filters",
            default=10,
            type=int,
            help="Number of filters for CNN",
        )

        parser.add_argument(
            "--t5_type",
            default="t5-base",
            type=str,
            help="Number of filters for CNN",
        )

        return parser
