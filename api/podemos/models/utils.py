from podemos.models.client import ClientModel
from podemos.models.group import GroupModel
from podemos.models.account import AccountModel
from database import db_session

def get_all_clients():
    return [client.json() for client in ClientModel.query.all()]

def get_all_groups(with_members=False):        
    return [group.json(with_members) for group in GroupModel.query.all()]

def get_all_accounts(group_id):
    accounts = db_session.query(AccountModel).filter(AccountModel.grupo_id==group_id).all()
    return [account.json() for account in accounts]
