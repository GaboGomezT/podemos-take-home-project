import pytest
from factories.client import ClientFactory
from podemos.resources.client import save_client, get_client, ClientModel
from database import db_session

def test_save_client():
    save_client("a1", "Eduardo")
    client = db_session.query(ClientModel).get("a1")
    
    assert client is not None

    # Delete inserted row after