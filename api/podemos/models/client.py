from podemos.models import BaseModel
from sqlalchemy import Column, String
from database import db_session
from podemos.errors import ClientAlreadyExists

class ClientModel(BaseModel):
    __tablename__ = "Clientes"

    id = Column(String(7), primary_key=True)
    nombre = Column(String(60))

    def __init__(self, _id, nombre):
        self.id = _id
        self.nombre = nombre

    def json(self):
        return {"id": self.id, "nombre": self.nombre}
    
    def save_to_db(self):
        if ClientModel.get_client(self.id):
             raise ClientAlreadyExists()
        db_session.add(self)
        db_session.commit()

    @classmethod
    def get_client(cls, _id):
        return db_session.query(cls).get(_id)

