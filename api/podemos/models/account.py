from podemos.models import BaseModel
from podemos.models.calendar import CalendarModel
from podemos.models.transaction import TransactionModel
from sqlalchemy import Column, String, Numeric
from sqlalchemy.orm import relationship
from database import db_session

class AccountModel(BaseModel):
    __tablename__ = "Cuentas"

    id = Column(String(5), primary_key=True)
    grupo_id = Column(String(5))
    estatus = Column(String(15))
    monto = Column(Numeric(15,2))
    saldo = Column(Numeric(15,2))

    calendar_payments = relationship("CalendarModel", lazy="dynamic")
    transactions = relationship("TransactionModel", lazy="dynamic")
