from src.models.history_model import HistoryModel
from src.models.user_model import UserModel


def test_history_delete(app_test, monkeypatch):
    # insere um chat no banco de dados
    history_chat = HistoryModel(
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        }
    ).save()

    response = app_test.get("/history/")
    assert len(response.json) == 1

    user = UserModel(
        {"name": "user autorizado", "token": "token do usuário"}
    ).save()

    # testa se a aplicação falha com um token inválido
    response = app_test.delete(
        f"/admin/history/{history_chat.id}",
        headers={
            "Authorization": "token diferente do usuário",
            "User": user.data["name"],
        },
    )

    assert response.status_code == 401
    assert response.json["error"] == "Unauthorized Access"

    # testa se a aplicação deleta do historico caso tenha um token válido
    response = app_test.delete(
        f"/admin/history/{history_chat.id}",
        headers={
            "Authorization": "token do usuário",
            "User": user.data["name"],
        },
    )

    assert response.status_code == 204

    response = app_test.get("/history/")
    assert len(response.json) == 0

    # testa se a aplicação falha ao tentar deletar um historico inexistente
    response = app_test.delete(
        f"/admin/history/{history_chat.id}",
        headers={
            "Authorization": "token do usuário",
            "User": user.data["name"],
        },
    )

    assert response.status_code == 404
    assert response.json["error"] == "History not found"
    pass
