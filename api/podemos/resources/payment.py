from flask_restful import Resource
from podemos.models.account import AccountModel
from flask import request
from database import db_session
from podemos.errors import PaymentExceedsDebt

class Payment(Resource):
    def get(self):
        account_id = request.args.get("account-id", type=str)
        payment_amount = request.args.get("payment-amount", type=int)
        
        if account_id and payment_amount:
            account = AccountModel.get_account(account_id)
            try:
                account.pay_account(amount=payment_amount)
                return {"message": "Payment Successful"}
            except PaymentExceedsDebt:
                return {"message": "Payment Exceeds Debt, Payment REJECTED"}, 400

        return {"message": "account-id and payment-amount required"}