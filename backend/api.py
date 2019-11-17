import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_jwt_extended import JWTManager


app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('JAWSDB_MARIA_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_POOL_RECYCLE'] = 500
app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

jwt = JWTManager(app)


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return models.RevokedTokenModel.is_jti_blacklisted(jti)


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
api.add_resource(resources.AllJapanFood, '/api/japan/food/all')
api.add_resource(resources.SingleJapanFood, '/api/japan/food')

api.add_resource(resources.AllJapanDrinks, '/api/japan/drinks/all')

api.add_resource(resources.UserRegistration, '/api/registration')
api.add_resource(resources.UserLogin, '/api/login')
api.add_resource(resources.UserLogoutAccess, '/api/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/api/logout/refresh')
api.add_resource(resources.TokenRefresh, '/api/token/refresh')

api.add_resource(resources.NotFound, '/api/<path:invalidPath>')
