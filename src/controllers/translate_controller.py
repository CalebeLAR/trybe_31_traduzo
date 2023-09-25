from flask import Blueprint, render_template, request
from models.language_model import LanguageModel

from deep_translator import GoogleTranslator

# from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        languages = LanguageModel.list_dicts()
        translate_from = "pt"
        translate_to = "en"

        text_to_translate = "O que deseja traduzir"
        translated = "Tradução"

        return render_template(
            "index.html",
            languages=languages,
            text_to_translate=text_to_translate,
            translate_from=translate_from,
            translate_to=translate_to,
            translated=translated,
        )

    if request.method == "POST":
        languages = LanguageModel.list_dicts()
        translate_from = request.form.get("translate-from")
        translate_to = request.form.get("translate-to")

        text_to_translate = request.form.get("text-to-translate")

        translated = GoogleTranslator(
            source=translate_from, target=translate_to
        ).translate(text=text_to_translate)

        return render_template(
            "index.html",
            languages=languages,
            text_to_translate=text_to_translate,
            translate_from=translate_from,
            translate_to=translate_to,
            translated=translated,
        )


# Req. 6
@translate_controller.route("/reverse", methods=["POST"])
def reverse():
    raise NotImplementedError
