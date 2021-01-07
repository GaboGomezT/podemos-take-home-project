from flask_restful import Resource
from podemos.models.account import AccountModel
from podemos.models.calendar import CalendarModel
from podemos.models.utils import get_all_accounts
from flask import request
from database import db_session
from podemos.errors import AccountAlreadyExists, MissingGroup
from podemos.constants import DISBURSED, PENDING
from datetime import datetime, timedelta

class AccountList(Resource):
    def get(self):
        _id = request.args.get("group-id", type=str)
        if _id:
            return {"accounts": get_all_accounts(_id)}
        else:
            return {"message": "group-id is neccesary"}, 400

class Account(Resource):
    def get(self):
        _id = request.args.get("id", type=str)
        with_calendar = request.args.get("with-calendar", type=bool, default=False)
        with_transactions = request.args.get("with-transactions", type=bool, default=False)
        if _id:
            account = AccountModel.get_account(_id)
            return account.json(with_calendar, with_transactions)
        return {"message": "id cannot be empty"}

    def post(self):
        _id = request.args.get("id", type=str)
        amount = request.args.get("amount", type=int)
        group_id = request.args.get("group-id", type=str)
        payment_weeks = request.args.get("payments", type=int)
    
        if _id and amount and group_id and payment_weeks:

            payments = []
            disbursed_date = datetime.now()
            amount_per_payment = amount / payment_weeks
            for i in range(1, payment_weeks+1):
                payday = disbursed_date + timedelta(weeks=i)
                calendar_payment = CalendarModel()
                calendar_payment.num_pago = i
                calendar_payment.monto = amount_per_payment
                calendar_payment.fecha_pago = payday
                calendar_payment.estatus = PENDING
                payments.append(calendar_payment)
            
            account = AccountModel()
            account.id = _id
            account.grupo_id = group_id
            account.estatus = DISBURSED
            account.monto = amount
            account.saldo = amount
            account.calendar_payments = payments
            try:
                account.save_to_db()
            except AccountAlreadyExists:
                return {"message": "Account already exists in DB"}, 400
            except MissingGroup:
                return {"message": "Cannot create account for non existent group"}, 400
            return {"message": "New Account Sucessfully Created"}
        return {"message": "if, amount, group-id and payments are neccesary"}, 400

