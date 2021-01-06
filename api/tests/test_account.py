
import pytest
from podemos.models.account import AccountModel
from podemos.models.group import GroupModel
from podemos.models.transaction import TransactionModel
from podemos.models.calendar import CalendarModel
from database import db_session
from podemos.models.utils import get_all_accounts
from podemos.constants import DISBURSED, CLOSED, PAID, PENDING
from datetime import datetime, timedelta

def test_get_all_accounts_given_group_id():
    payments = []
    first_payment_date = datetime.strptime("2020-10-5", "%Y-%m-%d")
    for i in range(1,6):
        payday = first_payment_date + timedelta(weeks=i-1)
        payment_status = PAID if i == 1 else PENDING
        payments.append(CalendarModel(
            payment_num=i, 
            amount=20_000, 
            payment_date=payday, 
            status=payment_status))

    transaction_1 = TransactionModel(date="2020-10-2", amount=20_000)
    second_account = AccountModel(
        _id="LKJH", 
        status=DISBURSED,
        amount=100_000, 
        balance=80_000, 
        calendar_payments=payments,
        transactions=[transaction_1])


    group = GroupModel(_id="ABCD", nombre="Team Rocket", accounts=[first_account, second_account])
    group.save_to_db()
    accounts = get_all_accounts(group_id=group.id)
