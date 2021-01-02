from flask_restful import Resource
from podemos.models.client import ClientModel
from podemos.models.utils import get_all_clients
from flask import request
from database import db_session
from podemos.errors import ClientAlreadyExists

class ClientList(Resource):
    def get(self):
        return {"clients": get_all_clients()}

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
            try:
                client.save_to_db()
            except ClientAlreadyExists:
                return {"message": "Client already exists in DB"}, 400
            return {"message": "New Client Sucessfully Created"}
        return {"message": "Both id and nombre are neccesary"}, 400

