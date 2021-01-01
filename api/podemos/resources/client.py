from flask_restful import Resource
from podemos.models.client import ClientModel
from flask import request
from database import db_session
class ClientList(Resource):
    def get(self):
        return {"clients": [client.json() for client in ClientModel.query.all()]}

class Client(Resource):
    def get(self):
        _id = request.args.get("id", type=str)
        if _id:
            client = ClientModel.get_client(_id)
            return client.json()
        return {"message": "id cannot be empty"}

    def post(self):
        _id = request.args.get("id", type=str)
        nombre = request.args.get("nombre", type=str)
        if _id and nombre:
            client = ClientModel(_id, nombre)
            client.save_to_db()
            return {"message": "New Client Sucessfully Created"}
        return {"message": "Both id and nombre are neccesary"}

