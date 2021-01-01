import pytest
from factories.client import ClientFactory
from podemos.resources.client import ClientModel
from database import db_session

def test_save_client():
    client = ClientModel("zzz", "Eduardo David")
    client.save_to_db()
    saved_client = db_session.query(ClientModel).get(client.id)

    assert saved_client is not None

    db_session.delete(client)
    db_session.commit()
