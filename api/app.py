from flask import Flask
from flask_restful import Api
from resources.client import ClientList
from database import db
from dotenv import load_dotenv
from os import getenv

load_dotenv()
    
user = getenv("PODEMOS_DB_USER")
password = getenv("PODEMOS_DB_PASS")
db_url = getenv("PODEMOS_DB_URL")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{user}:{password}@{db_url}:3306/podemos_eval"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
api = Api(app)

api.add_resource(ClientList, "/clients")

if __name__ == "__main__":
    db.init_app(app)
    app.run(port=5000, debug=True)