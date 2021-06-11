import collections
from typing import (
    List,
    Optional,
    Tuple,
    Union,
    NamedTuple,
    Dict,
    Any,
)

import numpy as np
import torch
from torch import nn
from torch.cuda.amp import autocast
from torch.utils.data.dataloader import DataLoader
from torch.utils.data.dataset import IterableDataset

# Integrations must be imported before ML frameworks:
from transformers.trainer_seq2seq import Seq2SeqTrainer
from transformers.integrations import (  # isort: split
    deepspeed_init,
    is_deepspeed_zero3_enabled,
)
from transformers.trainer_pt_utils import (
    IterableDatasetShard,
    find_batch_size,
    nested_concat,
    nested_numpify,
    nested_truncate,
)
from transformers.trainer_utils import (
    EvalLoopOutput,
    denumpify_detensorize,
)
import logging


class EvalPredictionWithMetadata(NamedTuple):
    """
    Evaluation output (always contains labels), to be used to compute metrics.

    Parameters:
        predictions (:obj:`np.ndarray`): Predictions of the model.
        label_ids (:obj:`np.ndarray`): Targets to be matched.
    """

    predictions: Union[np.ndarray, Tuple[np.ndarray]]
    label_ids: np.ndarray
    metadata: List[dict]


logger = logging.getLogger(__name__)


class NeuralDBTrainer(Seq2SeqTrainer):
    def evaluation_loop(
        self,
        dataloader: DataLoader,
        description: str,
        prediction_loss_only: Optional[bool] = None,
        ignore_keys: Optional[List[str]] = None,
        metric_key_prefix: str = "eval",
    ) -> EvalLoopOutput:
        """
        Prediction/evaluation loop, shared by :obj:`Trainer.evaluate()` and :obj:`Trainer.predict()`.
        Works both with or without labels.
        """
        prediction_loss_only = (
            prediction_loss_only
            if prediction_loss_only is not None
            else self.args.prediction_loss_only
        )

        # if eval is called w/o train init deepspeed here
        if self.args.deepspeed and not self.deepspeed:

            # XXX: eval doesn't have `resume_from_checkpoint` arg but we should be able to do eval
            # from the checkpoint eventually
            deepspeed_engine, _, _ = deepspeed_init(
                self, num_training_steps=0, resume_from_checkpoint=None
            )
            self.model = deepspeed_engine.module
            self.model_wrapped = deepspeed_engine
            self.deepspeed = deepspeed_engine
            # XXX: we don't need optim/sched for inference, but this needs to be sorted out, since
            # for example the Z3-optimizer is a must for zero3 to work even for inference - what we
            # don't need is the deepspeed basic optimizer which is self.optimizer.optimizer
            deepspeed_engine.optimizer.optimizer = None
            deepspeed_engine.lr_scheduler = None

        model = self._wrap_model(self.model, training=False)

        # if full fp16 is wanted on eval and this ``evaluation`` or ``predict`` isn't called while
        # ``train`` is running, halve it first and then put on device
        if not self.is_in_train and self.args.fp16_full_eval:
            model = model.half().to(self.args.device)

        batch_size = dataloader.batch_size

        logger.info(f"***** Running {description} *****")
        if isinstance(dataloader.dataset, collections.abc.Sized):
            logger.info(f"  Num examples = {self.num_examples(dataloader)}")
        else:
            logger.info("  Num examples: Unknown")
        logger.info(f"  Batch size = {batch_size}")

        model.eval()

        self.callback_handler.eval_dataloader = dataloader
        # Do this before wrapping.
        eval_dataset = dataloader.dataset
        #
        # if is_torch_tpu_available():
        #     dataloader = pl.ParallelLoader(dataloader, [self.args.device]).per_device_loader(self.args.device)

        if self.args.past_index >= 0:
            self._past = None

        # Initialize containers
        # losses/preds/labels on GPU/TPU (accumulated for eval_accumulation_steps)
        losses_host = None
        preds_host = None
        labels_host = None
        # losses/preds/labels on CPU (final containers)
        all_losses = None
        all_preds = None
        all_labels = None
        # Will be useful when we have an iterable dataset so don't know its length.

        observed_num_examples = 0
        # Main evaluation loop
        all_metadata = []
        for step, inputs in enumerate(dataloader):
            # Update the observed num examples
            observed_batch_size = find_batch_size(inputs)
            if observed_batch_size is not None:
                observed_num_examples += observed_batch_size

            if "metadata" in inputs:
                all_metadata.extend(inputs.pop("metadata"))
            else:
                logger.warning(f"missing metadata for {len(inputs)} records")
                all_metadata.extend([{} for _ in inputs])

            # Prediction step
            loss, logits, labels = self.prediction_step(
                model, inputs, prediction_loss_only, ignore_keys=ignore_keys
            )

            # Update containers on host
            if loss is not None:
                losses = self._nested_gather(loss.repeat(batch_size))
                losses_host = (
                    losses
                    if losses_host is None
                    else torch.cat((losses_host, losses), dim=0)
                )
            if logits is not None:
                logits = self._pad_across_processes(logits)
                logits = self._nested_gather(logits)
                preds_host = (
                    logits
                    if preds_host is None
                    else nested_concat(preds_host, logits, padding_index=-100)
                )
            if labels is not None:
                labels = self._pad_across_processes(labels)
                labels = self._nested_gather(labels)
                labels_host = (
                    labels
                    if labels_host is None
                    else nested_concat(labels_host, labels, padding_index=-100)
                )
            self.control = self.callback_handler.on_prediction_step(
                self.args, self.state, self.control
            )

            # Gather all tensors and put them back on the CPU if we have done enough accumulation steps.
            if (
                self.args.eval_accumulation_steps is not None
                and (step + 1) % self.args.eval_accumulation_steps == 0
            ):
                if losses_host is not None:
                    losses = nested_numpify(losses_host)
                    all_losses = (
                        losses
                        if all_losses is None
                        else np.concatenate((all_losses, losses), axis=0)
                    )
                if preds_host is not None:
                    logits = nested_numpify(preds_host)
                    all_preds = (
                        logits
                        if all_preds is None
                        else nested_concat(all_preds, logits, padding_index=-100)
                    )
                if labels_host is not None:
                    labels = nested_numpify(labels_host)
                    all_labels = (
                        labels
                        if all_labels is None
                        else nested_concat(all_labels, labels, padding_index=-100)
                    )

                # Set back to None to begin a new accumulation
                losses_host, preds_host, labels_host = None, None, None

        if self.args.past_index and hasattr(self, "_past"):
            # Clean the state at the end of the evaluation loop
            delattr(self, "_past")

        # Gather all remaining tensors and put them back on the CPU
        if losses_host is not None:
            losses = nested_numpify(losses_host)
            all_losses = (
                losses
                if all_losses is None
                else np.concatenate((all_losses, losses), axis=0)
            )
        if preds_host is not None:
            logits = nested_numpify(preds_host)
            all_preds = (
                logits
                if all_preds is None
                else nested_concat(all_preds, logits, padding_index=-100)
            )
        if labels_host is not None:
            labels = nested_numpify(labels_host)
            all_labels = (
                labels
                if all_labels is None
                else nested_concat(all_labels, labels, padding_index=-100)
            )

        # Number of samples
        if not isinstance(eval_dataset, IterableDataset):
            num_samples = len(eval_dataset)
        elif isinstance(eval_dataset, IterableDatasetShard):
            num_samples = eval_dataset.num_examples
        else:
            num_samples = observed_num_examples

        # Number of losses has been rounded to a multiple of batch_size and in a distributed training, the number of
        # samplers has been rounded to a multiple of batch_size, so we truncate.
        if all_losses is not None:
            all_losses = all_losses[:num_samples]
        if all_preds is not None:
            all_preds = nested_truncate(all_preds, num_samples)
        if all_labels is not None:
            all_labels = nested_truncate(all_labels, num_samples)

        # Metrics!
        if (
            self.compute_metrics is not None
            and all_preds is not None
            and all_labels is not None
        ):
            metrics = self.compute_metrics(
                EvalPredictionWithMetadata(
                    predictions=all_preds, label_ids=all_labels, metadata=all_metadata
                )
            )
        else:
            metrics = {}

        # To be JSON-serializable, we need to remove numpy types or zero-d tensors
        metrics = denumpify_detensorize(metrics)

        if all_losses is not None:
            metrics[f"{metric_key_prefix}_loss"] = all_losses.mean().item()

        # Prefix all keys with metric_key_prefix + '_'
        for key in list(metrics.keys()):
            if not key.startswith(f"{metric_key_prefix}_"):
                metrics[f"{metric_key_prefix}_{key}"] = metrics.pop(key)

        return EvalLoopOutput(
            predictions=all_preds,
            label_ids=all_labels,
            metrics=metrics,
            num_samples=num_samples,
        )

    def compute_loss(self, model, inputs, return_outputs=False):
        if "metadata" in inputs:
            inputs.pop("metadata")
        return super().compute_loss(model, inputs, return_outputs)

    def prediction_step(
        self,
        model: nn.Module,
        inputs: Dict[str, Union[torch.Tensor, Any]],
        prediction_loss_only: bool,
        ignore_keys: Optional[List[str]] = None,
    ) -> Tuple[Optional[float], Optional[torch.Tensor], Optional[torch.Tensor]]:
        """
        Perform an evaluation step on :obj:`model` using obj:`inputs`.

        Subclass and override to inject custom behavior.

        Args:
            model (:obj:`nn.Module`):
                The model to evaluate.
            inputs (:obj:`Dict[str, Union[torch.Tensor, Any]]`):
                The inputs and targets of the model.

                The dictionary will be unpacked before being fed to the model. Most modelling expect the targets
                under the argument :obj:`labels`. Check your model's documentation for all accepted arguments.
            prediction_loss_only (:obj:`bool`):
                Whether or not to return the loss only.

        Return:
            Tuple[Optional[float], Optional[torch.Tensor], Optional[torch.Tensor]]: A tuple with the loss, logits and
            labels (each being optional).
        """

        if not self.args.predict_with_generate or prediction_loss_only:
            return super().prediction_step(
                model,
                inputs,
                prediction_loss_only=prediction_loss_only,
                ignore_keys=ignore_keys,
            )

        has_labels = "labels" in inputs
        inputs = self._prepare_inputs(inputs)

        # XXX: adapt synced_gpus for fairscale as well
        gen_kwargs = {
            "max_length": self._max_length
            if self._max_length is not None
            else self.model.config.max_length,
            "num_beams": self._num_beams
            if self._num_beams is not None
            else self.model.config.num_beams,
            "synced_gpus": True if is_deepspeed_zero3_enabled() else False,
        }

        if "context_ids" in inputs:
            gen_kwargs["context_ids"] = inputs["context_ids"]
            gen_kwargs["context_mask"] = inputs["context_mask"]

        generated_tokens = self.model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"]
            if "attention_mask" in inputs
            else None,
            top_p=0.95,
            repetition_penalty=1.0,
            top_k=50,
            use_cache=True,
            do_sample=False,
            **gen_kwargs,
        )
        # in case the batch is shorter than max length, the output should be padded
        if generated_tokens.shape[-1] < gen_kwargs["max_length"]:
            generated_tokens = self._pad_tensors_to_max_len(
                generated_tokens, gen_kwargs["max_length"]
            )

        with torch.no_grad():
            if self.use_amp:
                with autocast():
                    outputs = model(**inputs)
            else:
                outputs = model(**inputs)
            if has_labels:
                if self.label_smoother is not None:
                    loss = (
                        self.label_smoother(outputs, inputs["labels"]).mean().detach()
                    )
                else:
                    loss = (
                        (outputs["loss"] if isinstance(outputs, dict) else outputs[0])
                        .mean()
                        .detach()
                    )
            else:
                loss = None

        if self.args.prediction_loss_only:
            return (loss, None, None)

        labels = inputs["labels"]
        if labels.shape[-1] < gen_kwargs["max_length"]:
            labels = self._pad_tensors_to_max_len(labels, gen_kwargs["max_length"])

        return (loss, generated_tokens, labels)

    def _prepare_inputs(
        self, inputs: Dict[str, Union[torch.Tensor, Any]]
    ) -> Dict[str, Union[torch.Tensor, Any]]:
        """
        Prepare :obj:`inputs` before feeding them to the model, converting them to tensors if they are not already and
        handling potential state.
        """

        for k, v in inputs.items():
            if isinstance(v, torch.Tensor):
                inputs[k] = v.to(self.args.device)
            elif (
                k != "metadata"
                and isinstance(v, list)
                and all(isinstance(elem, torch.Tensor) for elem in v)
            ):
                inputs[k] = [elem.to(self.args.device) for elem in v]

        if self.args.past_index >= 0 and self._past is not None:
            inputs["mems"] = self._past

        return inputs
