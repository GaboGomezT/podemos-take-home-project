from flask import Flask
from flask_restful import Api
from podemos.resources.client import ClientList, Client
from podemos.resources.group import GroupList, Group
from podemos.resources.account import AccountList, Account
from podemos.resources.payment import Payment
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
api.add_resource(GroupList, "/groups")
api.add_resource(Group, "/group")
api.add_resource(AccountList, "/accounts")
api.add_resource(Account, "/account")
api.add_resource(Payment, "/payment")

if __name__ == "__main__":
    app.run(port=5000, debug=True)