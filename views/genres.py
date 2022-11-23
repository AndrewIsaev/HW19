from flask import request
from flask_restx import Resource, Namespace

from dao.model.genre import GenreSchema
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        rs = genre_service.get_all()
        res = GenreSchema(many=True).dump(rs)
        return res, 200

    def post(self):
        request_json = request.json
        genre = genre_service.create(request_json)
        return "", 201, {"location": f"genre/{genre.id}"}


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        r = genre_service.get_one(gid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200

    def put(self, gid):
        request_json = request.json
        genre_service.update(request_json)
        return "", 204

    def delete(self, gid):
        genre_service.delete(gid)
        return "", 204

