import json
from flask import Blueprint, jsonify
from models.history_model import HistoryModel

history_controller = Blueprint("history_controller", __name__)


@history_controller.route("/", methods=["GET"])
def history():
    string_history = HistoryModel.list_as_json()
    json_history = json.loads(string_history)

    return jsonify(json_history), 200
