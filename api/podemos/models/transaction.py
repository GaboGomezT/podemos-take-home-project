from podemos.models import BaseModel
from sqlalchemy import Column, String, Numeric, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import db_session
from sqlalchemy.types import DateTime

class TransactionModel(BaseModel):
    __tablename__ = "Transacciones"

    id = Column(Integer, primary_key=True)
    cuenta_id = Column(String(5), ForeignKey("podemos_eval.Cuentas.id"))
    fecha = Column(DateTime)
    monto = Column(Numeric(15,2))

    def json(self):
        return {
            "id": self.id,
            "cuenta_id": self.cuenta_id,
            "fecha": self.fecha.strftime('%d/%m/%Y'),
            "monto": float(self.monto)
        }
