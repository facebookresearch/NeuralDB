from argparse import ArgumentParser
from copy import deepcopy
from torch.utils.data import DataLoader
import torch

from neuraldb.dataset.nuo_generator.nuo_op_classifier_generator import (
    NUOClassifierGenerator,
)
from neuraldb.dataset.nuo_generator.nuo_seq2seq_generator import (
    NUOSeq2SeqSpecificGenerator,
)
from neuraldb.models.cls_operator import CLSTransformer
from neuraldb.models.operator_run import RunSeq2seqOperatorTrainer


def load_cls_model(args):
    args_cls = deepcopy(args)
    args_cls.__dict__["model_name_or_path"] = "bert-base-uncased"
    cls_model = CLSTransformer(args_cls)
    return cls_model.load_from_checkpoint(
        args.cls_model + "/best_em.ckpt", external_test=True
    )


def load_nuo_model(args):
    args_nuo = deepcopy(args)
    args_nuo.__dict__["model_name_or_path"] = "t5-base"
    nuo_model = RunSeq2seqOperatorTrainer(args_nuo)
    return nuo_model.load_from_checkpoint(
        args.nuo_model + "/best_em.ckpt", external_test=True
    )


def nuo_forward(model, database, query, device="cpu"):
    generator: NUOSeq2SeqSpecificGenerator = model.reader.generator
    generator.test_mode = True

    loader = DataLoader(
        [generator.interactive(fact, query) for fact in database],
        batch_size=64,
        collate_fn=generator.collate_fn,
    )

    projected = []
    for batch in loader:
        batch = {
            k: v.to(device) if isinstance(v, torch.Tensor) else v
            for k, v in batch.items()
        }
        projected.extend(
            model.model.generate(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                num_beams=1,
                max_length=64,
                repetition_penalty=1,
                length_penalty=1.0,
                early_stopping=True,
                use_cache=True,
                do_sample=False,
                top_p=0.95,
                top_k=50,
                bad_words_ids=model.bad_words,
            )
        )

    return [generator._tokenizer.decode(p, skip_special_tokens=True) for p in projected]


def cls_forward(model, query):
    cls_generator: NUOClassifierGenerator = model.reader.generator
    cls_generator.test_mode = True
    cls_inst = cls_generator.interactive(query)
    batch = cls_generator.collate_fn([cls_inst])
    del batch["metadata"]

    cls = model.forward(**batch)
    return cls_generator.labels[torch.argmax(cls[0]).item()]
