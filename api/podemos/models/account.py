from podemos.models import BaseModel
from podemos.models.group import GroupModel
from sqlalchemy import Column, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from database import db_session

class AccountModel(BaseModel):
    __tablename__ = "Cuentas"

    id = Column(String(5), primary_key=True)
    grupo_id = Column(String(5), ForeignKey("podemos_eval.Grupos.id"))
    estatus = Column(String(15))
    monto = Column(Numeric(15,2))
    saldo = Column(Numeric(15,2))

    group = relationship("GroupModel", foreign_keys=[grupo_id])
    calendar_payments = relationship("CalendarModel", lazy="dynamic")
    transactions = relationship("TransactionModel", lazy="dynamic")

    def json():
        return {
            "id": self.id,
            "grupo_id": self.grupo_id,
            "estatus": self.estatus,
            "monto": self.monto,
            "saldo": self.saldo
        }
