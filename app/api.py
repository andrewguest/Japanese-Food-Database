from flask import jsonify
from flask_restful import Resource

from app import api, models


class GetAllJapanCandy(Resource):
    def get(self):
        all_candy = models.Candy.query.all()
        return jsonify(all_candy)


api.add_resource(GetAllJapanCandy, '/japan/candy/all')
