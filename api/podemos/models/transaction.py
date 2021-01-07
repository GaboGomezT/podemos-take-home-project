from podemos.models import BaseModel
from podemos.models.account import AccountModel
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

    cuenta = relationship("AccountModel", foreign_keys=[cuenta_id])
