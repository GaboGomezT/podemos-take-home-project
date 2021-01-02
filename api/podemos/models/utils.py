from podemos.models.client import ClientModel

def get_all_clients():
    return [client.json() for client in ClientModel.query.all()]