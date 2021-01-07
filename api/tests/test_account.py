
import pytest
from podemos.models.account import AccountModel
from podemos.models.group import GroupModel
from podemos.models.transaction import TransactionModel
from podemos.models.calendar import CalendarModel
from database import db_session
from podemos.models.utils import get_all_accounts
from podemos.constants import DISBURSED, CLOSED, PAID, PENDING
from datetime import datetime, timedelta

def test_get_account_with_all_information():
    payments = []
    first_payment_date = datetime.strptime("2020-10-5", "%Y-%m-%d")
    for i in range(1,6):
        payday = first_payment_date + timedelta(weeks=i-1)
        payment_status = PAID if i == 1 else PENDING
        calendar_payment = CalendarModel()
        calendar_payment.num_pago = i
        calendar_payment.monto = 20_000
        calendar_payment.fecha_pago = payday
        calendar_payment.estatus = payment_status
        payments.append(calendar_payment)

    transaction = TransactionModel()
    transaction.fecha = datetime.strptime("2020-10-2", "%Y-%m-%d")
    transaction.monto = 20_000

    account = AccountModel()
    account.id = "IIII"
    account.estatus = DISBURSED
    account.monto = 100_000
    account.saldo = 80_000
    account.calendar_payments = payments
    account.transactions = [transaction]

    group = GroupModel(_id="SSSS", nombre="Modern Family")
    group.accounts = [account]
    group.save_to_db()

    saved_account = AccountModel.get_account(account.id)
    account_dict = saved_account.json(with_calendar=True, with_transactions=True)

    saved_group = GroupModel.get_group(group.id)
    for transaction in saved_account.transactions.all():
            db_session.delete(transaction)
    for calendar_payment in saved_account.calendar_payments.all():
        db_session.delete(calendar_payment)
    db_session.delete(saved_account)
    db_session.delete(saved_group)
    db_session.commit()

    expected_keys = ["id", "grupo_id", "estatus", "monto", "saldo", "calendar_payments", "transactions"]
    assert type(account_dict) is dict
    assert len(set(account_dict.keys()) and set(expected_keys)) == len(expected_keys)
    assert len(account_dict["calendar_payments"]) == 5
    assert len(account_dict["transactions"]) == 1
    assert account_dict["transactions"][0]["monto"] == 20_000
    assert account_dict["calendar_payments"][0]["estatus"] == PAID

def test_get_all_accounts_given_group_id():

    first_account = AccountModel()
    first_account.id = "JJJJJ"
    first_account.estatus = CLOSED
    first_account.monto = 100_000
    first_account.saldo = 0

    second_account = AccountModel()
    second_account.id = "HHHHH"
    second_account.estatus = DISBURSED
    second_account.monto = 100_000
    second_account.saldo = 80_000

    group = GroupModel(_id="ZZZZZ", nombre="Modern Family")
    group.accounts = [first_account, second_account]
    group.save_to_db()

    accounts = get_all_accounts(group_id=group.id)

    saved_group = GroupModel.get_group(group.id)
    for account in saved_group.accounts.all():
        db_session.delete(account)
    db_session.delete(saved_group)
    db_session.commit()

    assert type(accounts) is list
    assert len(accounts) == 2
    assert type(accounts[0]) is dict
