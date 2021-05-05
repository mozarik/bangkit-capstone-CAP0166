import uuid
from application.User import User


def test_user_model_init():
    id = uuid.uuid4()
    user = User(id, name="Zein", birth_place="Makassar")

    assert user.id == id
    assert user.name == "Zein"
    assert user.birth_place == "Makassar"
