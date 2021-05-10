import logging
import json
from abc import ABC

from torch.utils.data import DataLoader
from transformers import AutoConfig, T5Tokenizer, T5Model
from neuraldb.dataset.deferred_dataset import DeferredDataset
from neuraldb.dataset.e2e_generator.seq2seq_deferred_reader import (
    DeferredSeq2SeqSpecificGenerator,
)
from neuraldb.dataset.search_engines.mips import MaximumInnerProductSearch
from neuraldb.models.cnn_encoder import CNNEncoder
from neuraldb.models.modelling_adaptive_t5 import (
    AdaptiveT5Model,
    AdaptiveT5ForConditionalGeneration,
)
from neuraldb.models.modelling_t2point5 import T2Point5Model
from neuraldb.models.seq2seqargs import Seq2seqTrainer

logger = logging.getLogger(__name__)


def save_json(content, path):
    with open(path, "w") as f:
        json.dump(content, f, indent=4)


class Seq2seqTrainerRet(Seq2seqTrainer, ABC):
    def __init__(self, hparams):
        super().__init__(hparams)
        self.retriever_scale = hparams.scale

    def construct_model(self, cache_dir, mode="base"):
        return AdaptiveT5ForConditionalGeneration.from_pretrained(
            self.hparams.model_name_or_path,
            from_tf=bool(".ckpt" in self.hparams.model_name_or_path),
            config=self.config,
            cache_dir=cache_dir,
            max_ret_layer=None,
        )

    def construct_generator(self):
        return DeferredSeq2SeqSpecificGenerator(
            self.tokenizer,
            update_search=self.search_retriever,
            context_limit=self.source_length,
            answer_limit=self.target_length,
        )

    def get_dataloader(
        self, type_path: str, batch_size: int, shuffle: bool = False
    ) -> DataLoader:
        ds = DeferredDataset(self.reader, self.data_generator)
        ds.read(type_path)
        data_loader = DataLoader(
            ds,
            batch_size=batch_size,
            collate_fn=self.data_generator.collate_fn,
            shuffle=shuffle,
        )
        return data_loader

    def _step(self, batch):
        pad_token_id = self.tokenizer.pad_token_id

        if "bart" in self.hparams.model_name_or_path:
            lm_labels = batch["lm_labels"][:, :-1].contiguous()
            lm_labels = lm_labels[:, 1:].clone()
            lm_labels[lm_labels[:, 1:] == pad_token_id] = -100
            outputs = self(
                batch["input_ids"],
                attention_mask=batch["attention_mask"],
                decoder_input_ids=batch["input_ids"],
                lm_labels=lm_labels,
            )

        if "t5" in self.hparams.model_name_or_path:
            lm_labels = batch["decoder_input_ids"]
            lm_labels = lm_labels.clone()
            lm_labels[lm_labels == pad_token_id] = -100
            embs = self.model.encoder.embed_tokens(batch["input_ids"])
            # bs = embs.shape[0]
            # embs = embs.view(-1,self.source_length*bs).mul(batch['scale'].view(self.source_length*bs)).view(-1,self.source_length,768)
            assert batch["scale"].shape[1] == self.source_length
            outputs = self(
                inputs_embeds=embs,
                attention_mask=batch["attention_mask"],
                lm_labels=lm_labels,
                retriever_bias=self.retriever_scale * batch["scale"],
            )

        loss = outputs[0]

        return loss

    def validation_step(self, batch, batch_idx):

        generated_ids = self.model.generate(
            input_ids=batch["input_ids"],
            attention_mask=batch["attention_mask"],
            num_beams=1,
            max_length=self.target_length,
            repetition_penalty=1,
            length_penalty=1.0,
            early_stopping=True,
            use_cache=True,
            do_sample=False,
            top_p=0.95,
            top_k=50,
            bad_words_ids=self.bad_words,
            retriever_bias=self.retriever_scale * batch["scale"],
        )

        preds = [
            self.tokenizer.decode(g, skip_special_tokens=True) for g in generated_ids
        ]
        target = [
            self.tokenizer.decode(t, skip_special_tokens=True)
            for t in batch["decoder_input_ids"]
        ]
        loss = self._step(batch)
        sources = [self.tokenizer.decode(s) for s in batch["input_ids"]]

        return {"val_loss": loss, "sources": sources, "preds": preds, "targets": target}

    def forward(
        self,
        input_ids=None,
        inputs_embeds=None,
        attention_mask=None,
        decoder_input_ids=None,
        lm_labels=None,
        retriever_bias=None,
    ):
        if decoder_input_ids == None:
            return self.model(
                input_ids=input_ids,
                inputs_embeds=inputs_embeds,
                attention_mask=attention_mask,
                lm_labels=lm_labels,
                retriever_bias=retriever_bias,
            )
        else:
            return self.model(
                input_ids=input_ids,
                inputs_embeds=inputs_embeds,
                attention_mask=attention_mask,
                decoder_input_ids=decoder_input_ids,
                lm_labels=lm_labels,
                retriever_bias=retriever_bias,
            )

    @staticmethod
    def add_model_specific_args(parser, root_dir):
        Seq2seqTrainer.add_model_specific_args(parser, root_dir)

        parser.add_argument(
            "--scale",
            default=1.0,
            type=float,
            help="Beta scaling factor for retriever",
        )

        return parser
