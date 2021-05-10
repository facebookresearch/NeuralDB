import logging
import json
from neuraldb.dataset.e2e_generator.seq2seq_fusion_reader import (
    Seq2SeqV1FusionSpecificGenerator,
)
from neuraldb.dataset.search_engines.bm25 import BM25SearchEngine
from neuraldb.dataset.search_engines.return_all import ReturnAll
from neuraldb.dataset.search_engines.tfidf import TFIDFSearchEngine
from neuraldb.models.modelling_fid_t5 import T5MergeForConditionalGeneration
from neuraldb.models.seq2seqargs import Seq2seqTrainer

logger = logging.getLogger(__name__)


def save_json(content, path):
    with open(path, "w") as f:
        json.dump(content, f, indent=4)


class Seq2seqFusionTrainer(Seq2seqTrainer):
    def construct_model(self, cache_dir):
        return T5MergeForConditionalGeneration.from_pretrained(
            self.hparams.model_name_or_path,
            config=self.config,
            cache_dir=cache_dir,
        )

    def construct_retriever(self, search_engine="tfidf"):
        if search_engine == "tfidf":
            return TFIDFSearchEngine(self.hparams.filter_size)
        elif search_engine == "all":
            return ReturnAll()
        elif search_engine == "bm25":
            return BM25SearchEngine()

    def construct_generator(self):
        return Seq2SeqV1FusionSpecificGenerator(
            self.tokenizer,
            update_search=self.search_retriever,
            context_limit=self.source_length,
            answer_limit=self.target_length,
            test_mode=hasattr(self.hparams, "external_test"),
            unlimited_budget=True,
            is_oracle=self.hparams.oracle,
        )

    def forward(
        self,
        input_ids=None,
        inputs_embeds=None,
        context_ids=None,
        context_mask=None,
        attention_mask=None,
        decoder_input_ids=None,
        lm_labels=None,
        retriever_bias=None,
    ):
        return self.model(
            input_ids=context_ids,
            attention_mask=attention_mask,
            context_ids=context_ids,
            context_mask=context_mask,
            decoder_input_ids=decoder_input_ids,
            lm_labels=lm_labels,
        )

    def validation_step(self, batch, batch_idx):
        generated_ids = self.model.generate(
            input_ids=batch["input_ids"],
            attention_mask=batch["attention_mask"],
            context_ids=batch["context_ids"],
            context_mask=batch["context_mask"],
            num_beams=1,
            max_length=self.target_length,
            repetition_penalty=1,
            length_penalty=1.0,
            use_cache=True,
            early_stopping=True,
            do_sample=False,
            top_p=0.95,
            top_k=50,
            bad_words_ids=self.bad_words,
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

    def test_step(self, batch, batch_idx):
        generated_ids = self.model.generate(
            input_ids=batch["input_ids"],
            attention_mask=batch["attention_mask"],
            context_ids=batch["context_ids"],
            context_mask=batch["context_mask"],
            num_beams=1,
            max_length=self.target_length,
            repetition_penalty=1,
            length_penalty=1.0,
            use_cache=True,
            early_stopping=True,
            do_sample=False,
            top_p=0.95,
            top_k=50,
            bad_words_ids=self.bad_words,
        )

        preds = [
            self.tokenizer.decode(g, skip_special_tokens=True) for g in generated_ids
        ]
        target = [
            self.tokenizer.decode(t, skip_special_tokens=True)
            for t in batch["decoder_input_ids"]
        ]
        sources = [self.tokenizer.decode(s) for s in batch["input_ids"]]

        return {
            "sources": sources,
            "preds": preds,
            "targets": target,
            "metadata": batch["metadata"] if "metadata" in batch else None,
        }

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
            outputs = self(
                batch["input_ids"],
                attention_mask=batch["attention_mask"],
                context_ids=batch["context_ids"],
                context_mask=batch["context_mask"],
                lm_labels=lm_labels,
            )

        loss = outputs[0]
        return loss

    def training_step(self, batch, batch_idx):
        if batch_idx == 0:
            self.trainer.total_loss = 0
        loss = self._step(batch)
        self.trainer.total_loss = getattr(self.trainer, "total_loss", 0.0) + loss
        self.trainer.avg_loss = loss  # self.trainer.total_loss/((batch_idx+1)*self.hparams.train_batch_size)
        tensorboard_logs = {"train_loss": loss}

        # if batch_idx%25 == 0:
        #    print([a.shape[0] for a in batch["context_ids"]], loss)

        return {"loss": loss, "log": tensorboard_logs}

    @staticmethod
    def add_model_specific_args(parser, root_dir):
        Seq2seqTrainer.add_model_specific_args(parser, root_dir)

        parser.add_argument(
            "--filter_size",
            default=10,
            type=int,
            help="The maximum number of sentences to be used",
        )

        return parser
