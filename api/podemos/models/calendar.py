from podemos.models import BaseModel
from sqlalchemy import Column, String, Numeric, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database import db_session
from sqlalchemy.types import DateTime

class CalendarModel(BaseModel):
    __tablename__ = "CalendarioPagos"

    id = Column(Integer, primary_key=True)
    cuenta_id = Column(String(5), ForeignKey("podemos_eval.Cuentas.id"))
    num_pago = Column(Integer)
    monto = Column(Numeric(15,2))
    fecha_pago = Column(DateTime)
    estatus = Column(String(15))

    def json(self):
        return {
            "id": self.id,
            "cuenta_id": self.cuenta_id,
            "num_pago": self.num_pago,
            "monto": self.monto,
            "fecha_pago": self.fecha_pago,
            "estatus": self.estatus
        }