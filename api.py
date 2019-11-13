from os import getenv

from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


#########################
# Configuration / setup #
#########################
mysql_username = getenv('MYSQL_USERNAME')
mysql_password = getenv('MYSQL_PASSWORD')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@localhost/Japan'.format(mysql_username, mysql_password)

api = Api(app)
db = SQLAlchemy(app)





class TestPing(Resource):
    def get(self):
        return jsonify(username=mysql_username, password=mysql_password, URI=app.config['SQLALCHEMY_DATABASE_URI'])


api.add_resource(TestPing, '/test/ping')
