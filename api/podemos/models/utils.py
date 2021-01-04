from podemos.models.client import ClientModel
from podemos.models.group import GroupModel

def get_all_clients():
    return [client.json() for client in ClientModel.query.all()]

def get_all_groups():
    return [group.json() for group in GroupModel.query.all()]