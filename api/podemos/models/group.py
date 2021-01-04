from podemos.models import BaseModel
from sqlalchemy import Column, String
from database import db_session
from podemos.errors import GroupAlreadyExists

class GroupModel(BaseModel):
    __tablename__ = "Grupos"

    id = Column(String(7), primary_key=True)
    nombre = Column(String(60))

    def __init__(self, _id, nombre):
        self.id = _id
        self.nombre = nombre

    def json(self):
        return {"id": self.id, "nombre": self.nombre}
    
    def save_to_db(self):
        if GroupModel.get_group(self.id):
             raise GroupAlreadyExists()
        db_session.add(self)
        db_session.commit()

    @classmethod
    def get_group(cls, _id):
        return db_session.query(cls).get(_id)

