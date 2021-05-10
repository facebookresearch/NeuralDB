from argparse import ArgumentParser

import flask
from flask import request, render_template

from log_helper import setup_logging
from neuraldb.dataset.instance_generator import InstanceGenerator
from neuraldb.demo.helpers import (
    load_cls_model,
    load_nuo_model,
    cls_forward,
    nuo_forward,
)
from neuraldb.models.cls_operator import CLSTransformer
from neuraldb.models.operator_run import RunSeq2seqOperatorTrainer

if __name__ == "__main__":

    app = flask.Flask(
        __name__, instance_relative_config=True, template_folder="../../../www"
    )

    parser = ArgumentParser(conflict_handler="resolve")
    CLSTransformer.add_model_specific_args(parser, None)
    RunSeq2seqOperatorTrainer.add_model_specific_args(parser, None)
    parser.add_argument("--cls_model")
    parser.add_argument("--nuo_model")
    args = parser.parse_args()

    cls_model = load_cls_model(args)
    nuo_model = load_nuo_model(args)

    @app.route("/", methods=["GET"])
    def home():
        return render_template(
            "demo.html", **{"nuo_path": args.nuo_model, "cls_path": args.cls_model}
        )

    @app.route("/query", methods=["POST"])
    def post_query():
        result = {}

        request_body = request.json
        query = request_body["query"]
        db = [f.strip() for f in request_body["facts"].strip().split("\n")]

        if len(query) < 5:
            return {"error": "Query is too short"}, 400

        try:
            action = cls_forward(cls_model, query)
        except:
            return {"error": "Error predicting action type (see logs)"}, 500

        try:
            projected = nuo_forward(nuo_model, db, query)
        except:
            return {"error": "Error predicting projections (see logs)"}, 500

        result["projection"] = "\n".join(projected)
        result["action"] = action

        projected_clean = [
            a.split(maxsplit=1)[1]
            for a in projected
            if a != InstanceGenerator.null_answer_special
        ]

        if action == "set":
            result["computation"] = ", ".join(projected_clean)
        elif action == "count":
            result["computation"] = len(projected_clean)
        else:
            result["computation"] = "NOT IMPLEMENTED"

        return result

    app.run()
