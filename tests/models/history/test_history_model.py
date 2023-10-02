import json
from src.models.history_model import HistoryModel

mock1 = {
    "text_to_translate": "Hello, I like videogame",
    "translate_from": "en",
    "translate_to": "pt",
}
mock2 = {
    "text_to_translate": "Do you love music?",
    "translate_from": "en",
    "translate_to": "pt",
}


# Req. 7
def test_request_history(prepare_base):
    string_chats = HistoryModel.list_as_json()

    assert '"text_to_translate": "Hello, I like videogame",' in string_chats
    assert '"translate_from": "en",' in string_chats
    assert '"translate_to": "pt"' in string_chats

    assert '"text_to_translate": "Do you love music?",' in string_chats
    assert '"translate_from": "en",' in string_chats
    assert '"translate_to": "pt"' in string_chats
    pass
