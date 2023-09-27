from flask import Blueprint, render_template, request
from models.language_model import LanguageModel

from deep_translator import GoogleTranslator

# from models.history_model import HistoryModel


translate_controller = Blueprint("translate_controller", __name__)


# utilitários
def set_value_by_tag_name(default_value, name_tag):
    if request.method == "GET":
        return default_value
    else:
        return request.form.get(name_tag)


# Reqs. 4 e 5
@translate_controller.route("/", methods=["GET", "POST"])
def index():
    languages = LanguageModel.list_dicts()
    translate_from = set_value_by_tag_name("pt", "translate-from")
    translate_to = set_value_by_tag_name("en", "translate-to")
    text_to_translate = set_value_by_tag_name("", "text-to-translate")

    translated = (
        ""
        if request.method == "GET"
        else GoogleTranslator(
            source=translate_from, target=translate_to
        ).translate(text=text_to_translate)
    )

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
    languages = LanguageModel.list_dicts()

    translate_from = request.form.get("translate-from")
    translate_to = request.form.get("translate-to")

    text_to_translate = request.form.get("text-to-translate")

    translated = (
        ""
        if request.method == "GET"
        else GoogleTranslator(
            source=translate_from, target=translate_to
        ).translate(text=text_to_translate)
    )

    return render_template(
        "index.html",
        languages=languages,
        translated=translated,
        text_to_translate=text_to_translate,

        # inverte os idiomas de tradução
        translate_from=translate_to,
        translate_to=translate_from,
    )
