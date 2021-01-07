from podemos.models import BaseModel
from podemos.models.group import GroupModel
from podemos.models.calendar import CalendarModel
from podemos.models.transaction import TransactionModel
from sqlalchemy import Column, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from database import db_session
from podemos.errors import AccountAlreadyExists, MissingGroup, PaymentExceedsDebt
from podemos.constants import CLOSED, PAID, LATE, PARTIAL
from datetime import datetime

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

    def save_to_db(self):
        if db_session.query(AccountModel).get(self.id):
            raise AccountAlreadyExists()
        if not db_session.query(GroupModel).get(self.grupo_id):
            raise MissingGroup()
        db_session.add(self)
        db_session.commit()

    @classmethod
    def get_account(cls, _id):
        return db_session.query(cls).get(_id)

    def pay_account(self, amount):
        self.saldo -= amount
        if self.saldo < 0:
            raise PaymentExceedsDebt()
        if self.saldo == 0:
            self.estatus = CLOSED
        
        transaction = TransactionModel()
        transaction.fecha = datetime.now()
        transaction.monto = amount

        transactions = self.transactions.all()
        transactions.append(transaction)

        self.transactions = transactions
        db_session.commit()

    def json(self, with_calendar=False, with_transactions=False):
        account_dict = {
            "id": self.id,
            "grupo_id": self.grupo_id,
            "estatus": self.estatus,
            "monto": float(self.monto),
            "saldo": float(self.saldo)
        }
        if with_calendar:
            account_dict["calendar_payments"] = [calendar_payment.json() for calendar_payment in self.calendar_payments.all()]
        if with_transactions:
            account_dict["transactions"] = [transaction.json() for transaction in self.transactions.all()]
        return account_dict
