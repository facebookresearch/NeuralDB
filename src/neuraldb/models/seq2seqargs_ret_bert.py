import logging
from abc import ABC
from transformers import AutoConfig, T5Tokenizer, BertTokenizer, BertModel
from neuraldb.dataset.search_engines.mips import MaximumInnerProductSearch
from neuraldb.models.cnn_encoder import CNNEncoder
from neuraldb.models.modelling_t2point5 import T2Point5Model
from neuraldb.models.seq2seqargs import Seq2seqTrainer
from neuraldb.models.seq2seqargs_ret import Seq2seqTrainerRet

logger = logging.getLogger(__name__)


class Seq2seqTrainerRetBert(Seq2seqTrainerRet):
    def construct_retriever(self):
        tok = BertTokenizer.from_pretrained(self.hparams.bert_type)

        auto_config = AutoConfig.from_pretrained(self.hparams.bert_type)

        self.tok_model = BertModel.from_pretrained(
            self.hparams.bert_type,
            config=auto_config,
        )

        return MaximumInnerProductSearch(tok, self.tok_model, None, None)

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
            "--bert_type",
            default="bert-base-uncased",
            type=str,
            help="Bert model",
        )

        return parser
