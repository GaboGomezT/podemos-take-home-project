import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from podemos.models.base_model import BaseModel
from dotenv import load_dotenv
from os import getenv

load_dotenv()
    
user = getenv("PODEMOS_DB_USER")
password = getenv("PODEMOS_DB_PASS")
db_url = getenv("PODEMOS_DB_URL")
db_port = getenv("PODEMOS_DB_PORT")

engine = create_engine(f"mysql+pymysql://{user}:{password}@{db_url}:{db_port}")
db_session = scoped_session(sessionmaker(autocommit=False,autoflush=False,bind=engine))

BaseModel.query = db_session.query_property()

def init_db():
    import models

    BaseModel.metadata.create_all(bind=engine)