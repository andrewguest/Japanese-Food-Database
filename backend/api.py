import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

mariadb_uri = "mysql://{}:{}@localhost/Japan".format(
    os.getenv("MYSQL_USERNAME"), os.getenv("MYSQL_PASSWORD")
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
import schema
import models
import resources


@app.before_first_request
def create_tables():
    db.create_all()


##############################################
# Defining API endpoints and their functions #
##############################################
api.add_resource(resources.AllFood, "/v1/food/all")
api.add_resource(resources.SingleFood, "/v1/food/<int:food_id>")
api.add_resource(resources.FoodLimit, "/v1/food/limit/<int:number_of_results>")

api.add_resource(resources.AllDrinks, "/v1/drink/all")
api.add_resource(resources.SingleDrink, "/v1/drink/<int:drink_id>")

api.add_resource(resources.NotFound, "/v1/<path:invalidPath>")
