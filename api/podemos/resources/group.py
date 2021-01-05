from flask_restful import Resource
from podemos.models.group import GroupModel
from podemos.models.utils import get_all_groups
from flask import request
from database import db_session
from podemos.errors import GroupAlreadyExists

class GroupList(Resource):
    def get(self):
        with_members = request.args.get("with-members", type=bool, default=False)
        return {"groups": get_all_groups(with_members)}

class Group(Resource):
    def get(self):
        _id = request.args.get("id", type=str)
        if _id:
            group = GroupModel.get_group(_id)
            return group.json()
        return {"message": "id cannot be empty"}

    def post(self):
        _id = request.args.get("id", type=str)
        nombre = request.args.get("nombre", type=str)
        if _id and nombre:
            group = GroupModel(_id, nombre)
            try:
                group.save_to_db()
            except GroupAlreadyExists:
                return {"message": "Group already exists in DB"}, 400
            return {"message": "New Group Sucessfully Created"}
        return {"message": "Both id and nombre are neccesary"}, 400

