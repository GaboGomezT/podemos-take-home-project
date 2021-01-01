from flask_restful import Resource
from models.client import ClientModel

class ClientList(Resource):
    def get(self):
        print(f"\033[94mCLIENT LIST RESOURCE\033[0m")
        return {"clients": [client.json() for client in ClientModel.query.all()]}
