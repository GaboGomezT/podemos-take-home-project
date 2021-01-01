from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()

class BaseModel(base):
    __abstract__ = True
    __table_args__ = {"schema": "podemos_eval"}