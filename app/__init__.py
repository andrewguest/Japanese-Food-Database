from os import getenv

from flask import Flask, jsonify
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


mysql_username = getenv('MYSQL_USERNAME')
mysql_password = getenv('MYSQL_PASSWORD')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@localhost/Japan'.format(mysql_username, mysql_password)

api = Api(app)
db = SQLAlchemy(app)

from app import models, routes

api.add_resource(routes.GetAllJapanCandy, '/japan/candy/all')
