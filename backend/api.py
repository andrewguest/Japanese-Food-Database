import os
import logging

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)
logging.basicConfig(
    filename="/var/log/food-myjapandb.log",
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s",
)

mariadb_uri = "mysql://{username}:{password}@localhost/Japan".format(
    username=os.getenv("MYSQL_USERNAME"), password=os.getenv("MYSQL_PASSWORD")
)

app.config["SQLALCHEMY_DATABASE_URI"] = mariadb_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_POOL_RECYCLE"] = 500

######################################################
# Cross Origin Resource Sharing (CORS) configuration #
######################################################
CORS(app, resources={r"/api/*": {"origins": "*"}})


#####################################################
# These are imported here to avoid circular imports #
#####################################################
import models
import schema
import resources


@app.before_first_request
def create_tables():
    db.create_all()


##############################################
# Defining API endpoints and their functions #
##############################################
api.add_resource(resources.AllFood, "/v1/food/all")
api.add_resource(resources.SingleFood, "/v1/food/<int:food_id>")

api.add_resource(resources.AllDrinks, "/v1/drink/all")
api.add_resource(resources.SingleDrink, "/v1/drink/<int:drink_id>")

api.add_resource(resources.NotFound, "/v1/<path:invalidPath>")
