from flask import Flask
from flask_restful import Api
from resources.client import ClientList
from database import db_session
from models.base_model import BaseModel

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

api.add_resource(ClientList, "/clients")

if __name__ == "__main__":
    app.run(port=5000, debug=True)