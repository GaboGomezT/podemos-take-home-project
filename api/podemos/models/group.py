from podemos.models import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from database import db_session
from podemos.errors import GroupAlreadyExists
from podemos.models.client import ClientModel

class GroupModel(BaseModel):
    __tablename__ = "Grupos"

    id = Column(String(5), primary_key=True)
    nombre = Column(String(20))

    members = relationship("MemberModel", lazy="dynamic")
    accounts = relationship("AccountModel", lazy="dynamic")

    def __init__(self, _id, nombre):
        self.id = _id
        self.nombre = nombre

    def json(self, with_members=False):
        group_dict = {"id": self.id, "nombre": self.nombre}
        if with_members:
            group_dict["members"] = [member.client.json() for member in self.members.all()]
        return group_dict
    
    def save_to_db(self):
        if GroupModel.get_group(self.id):
             raise GroupAlreadyExists()
        db_session.add(self)
        db_session.commit()

    @classmethod
    def get_group(cls, _id):
        return db_session.query(cls).get(_id)

class MemberModel(BaseModel):
    __tablename__ = "Miembros"

    grupo_id = Column(String(5), ForeignKey("podemos_eval.Grupos.id"), primary_key=True)
    cliente_id = Column(String(7), ForeignKey("podemos_eval.Clientes.id"), primary_key=True)

    group = relationship("GroupModel", foreign_keys=[grupo_id])
    client = relationship("ClientModel", foreign_keys=[cliente_id])

