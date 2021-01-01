from flask import Flask
from flask_restful import Api
from podemos.resources.client import ClientList, Client
from database import db_session
from podemos.models.base_model import BaseModel

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

api.add_resource(ClientList, "/clients")
api.add_resource(Client, "/client")

if __name__ == "__main__":
    app.run(port=5000, debug=True)