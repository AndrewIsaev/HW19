from flask import request
from flask_restx import Namespace, Resource

from implemented import auth_service

auth_ns = Namespace("auth")


@auth_ns.route("/")
class AuthView(Resource):
    def post(self):
        request_json = request.json
        username = request_json.get("username")
        password = request_json.get("password")

        if None in [username, password]:
            return "", 401

        token = auth_service.generate_token(username, password)
        return token, 201

    def put(self):
        request_json = request.json
        token = request_json.get("refresh_token")
        tokens = auth_service.check_token(token)
        return tokens, 201
