from os import getenv
from datetime import datetime

from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
mysql_name = getenv('MYSQL_USERNAME')
mysql_password = getenv('MYSQL_PASSWORD')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@localhost/Japan'.format(mysql_name, mysql_password)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_RECYCLE'] = 500

api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

#####################################################
# These are imported here to avoid circular imports #
#####################################################
import models
import schema

candy_schema = schema.CandySchema()
candies_schema = schema.CandySchema(many=True)
parser = reqparse.RequestParser()


############################################
# Functions that the API endpoints trigger #
############################################
class AllJapanCandy(Resource):
    def get(self):
        all_candy = models.Candy.query.all()
        result = candies_schema.dump(all_candy)
        return jsonify(result)
 

class SingleJapanCandy(Resource):
    def put(self):
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('taste', type=str, required=True)
        parser.add_argument('region', type=str, required=True)
        parser.add_argument('url', type=str, required=True)
        parser.add_argument('image_path', type=str)
        current_time = datetime.now()

        args = parser.parse_args()
        args['date_added'] = current_time.strftime("%Y-%m-%d %H:%M:%S")

        new_candy = models.Candy(name=args['name'], taste=args['taste'],
                                 region=args['region'], url=args['url'],
                                 image_path=args['image_path'],
                                 date_added=args['date_added'])

        db.session.add(new_candy)
        db.session.commit()

        return jsonify(name=args['name'], taste=args['taste'],
                       region=args['region'], url=args['url'],
                       image_path=args['image_path'],
                       date_added=args['date_added'])


class NotFound(Resource):
    def get(self, invalidPath=''):
        return jsonify(status=404, path=invalidPath,
                       message="This URL is not a valid API endpoint")


##############################################
# Defining API endpoints and their functions #
##############################################
api.add_resource(AllJapanCandy, '/api/japan/candy/all')
api.add_resource(SingleJapanCandy, '/api/japan/candy')
api.add_resource(NotFound, '/api/<path:invalidPath>')
