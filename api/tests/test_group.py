import pytest
from podemos.resources.group import GroupModel
from database import db_session
from podemos.errors import GroupAlreadyExists
from podemos.models.utils import get_all_groups


def test_save_group():
    group = GroupModel("ZZZ", "Power Rangers")
    group.save_to_db()
    saved_group = db_session.query(GroupModel).get(group.id)

    assert saved_group is not None

    db_session.delete(group)
    db_session.commit()

def test_save_group_already_exists():
    group = GroupModel("ZZZ", "Power Rangers")
    group.save_to_db()
    with pytest.raises(GroupAlreadyExists):
        group.save_to_db()
    db_session.delete(group)
    db_session.commit()

def test_get_all_groups():
    result = get_all_groups()
    assert type(result) is list
    assert len(result) > 0 # Esto es porque no tenemos una bd solamente para pruebas. Espacio de mejora.
    assert type(result[0]) is dict
    assert len(set(result[0].keys()) and set(["id", "nombre"])) == 2   