from podemos.models import BaseModel
from sqlalchemy import Column, String

class ClientModel(BaseModel):
    __tablename__ = "Clientes"

    id = Column(String(7), primary_key=True)
    nombre = Column(String(60))

    def __init__(self, _id, nombre):
        self.id = _id
        self.nombre = nombre

    def json(self):
        return {"id": self.id, "nombre": self.nombre}
