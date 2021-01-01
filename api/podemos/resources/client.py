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
            client = get_client(_id)
            return client.json()
        return {"message": "id cannot be empty"}

    def post(self):
        _id = request.args.get("id", type=str)
        nombre = request.args.get("nombre", type=str)
        if _id and nombre:
            save_client(_id, nombre)
            return {"message": "New Client Sucessfully Created"}
        return {"message": "Both id and nombre are neccesary"}

def save_client(_id, nombre):
    new_client = ClientModel(_id, nombre)
    db_session.add(new_client)
    db_session.commit()

def get_client(_id):
    return db_session.query(ClientModel).get(_id)
