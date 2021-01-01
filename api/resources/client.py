from flask_restful import Resource
from models.client import ClientModel

class ClientList(Resource):
    def get(self):
        return {"clients": [client.json() for client in ClientModel.query.all()]}
