from flask import request
from flask_restx import Resource, Namespace

from dao.model.user import UserSchema
from implemented import user_service

user_ns = Namespace("users")

@user_ns.route("/")
class UsersViews(Resource):
    def get(self):
        users = user_service.get_all()
        return UserSchema(many=True).dump(users), 200

    def post(self):
        req_json = request.json
        user = user_service.create(req_json)
        return "", 201, {"location": f"/users/{user.id}"}

@user_ns.route("/")
class UserViews(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        return UserSchema().dump(user), 200

    def put(self, uid):
        req_json = request.json
        user_service.update(req_json)
        return "", 204
