import pytest
from podemos.resources.client import ClientModel
from database import db_session
from podemos.errors import ClientAlreadyExists
from podemos.models.utils import get_all_clients

def test_save_client():
    client = ClientModel("zzx", "Eduardo David")
    client.save_to_db()
    saved_client = db_session.query(ClientModel).get(client.id)

    assert saved_client is not None

    db_session.delete(client)
    db_session.commit()

def test_save_client_already_exists():
    client = ClientModel("zzx", "Eduardo David")
    client.save_to_db()
    with pytest.raises(ClientAlreadyExists):
        client.save_to_db()
    db_session.delete(client)
    db_session.commit()

def test_all_clients():
    result = get_all_clients()
    assert type(result) is list
    assert len(result) > 0 # Esto es porque no tenemos una bd solamente para pruebas. Espacio de mejora.
    assert type(result[0]) is dict
    assert len(set(result[0].keys()) and set(["id", "nombre"])) == 2   