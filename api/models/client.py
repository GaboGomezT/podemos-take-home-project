from database import db

class ClientModel(db.Model):
    __tablename__ = "Clientes"
    __table_args__ = {"schema": "podemos_eval"}

    id = db.Column(db.String(7), primary_key=True)
    nombre = db.Column(db.String(60))

    def __init__(self, _id, nombre):
        self.id = _id
        self.name = name

    def json(self):
        return {"id": self.id, "nombre": self.nombre}
