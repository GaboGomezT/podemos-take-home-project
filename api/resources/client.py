from flask_restful import Resource
from models.client import ClientModel
from flask import request
from database import db_session
class ClientList(Resource):
    def get(self):
        return {"clients": [client.json() for client in ClientModel.query.all()]}

class Client(Resource):
    def post(self):
        _id = request.args.get("id", type=str)
        nombre = request.args.get("nombre", type=str)
        if _id and nombre:
            new_client = ClientModel(_id, nombre)
            db_session.add(new_client)
            db_session.commit()
            return {"message": "New Client Sucessfully Created"}
        return {"message": "Both id and nombre are neccesary"}
