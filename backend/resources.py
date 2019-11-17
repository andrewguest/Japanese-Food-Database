from datetime import datetime

from flask_restful import Resource, reqparse
from flask import jsonify
from flask_jwt_extended import (create_access_token, create_refresh_token,
                                jwt_required, jwt_refresh_token_required,
                                get_jwt_identity, get_raw_jwt)

from api import db
from schema import FoodSchema, DrinkSchema
from models import Food, Drink, UserModel, RevokedTokenModel


parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)

#######################
# Marshmallow schemas #
#######################
food_schema = FoodSchema()
foods_schema = FoodSchema(many=True)
drink_schema = DrinkSchema()
drinks_schema = DrinkSchema(many=True)


######################################
# 'Food' functions for API endpoints #
######################################
class AllJapanFood(Resource):
    def get(self):
        all_food = Food.query.all()
        result = foods_schema.dump(all_food)
        return jsonify(result)


class SingleJapanFood(Resource):
    @jwt_required
    def post(self):

        parser.add_argument('name', type=str, required=True)
        parser.add_argument('taste', type=str, required=True)
        parser.add_argument('region', type=str, required=True)
        parser.add_argument('url', type=str, required=True)
        parser.add_argument('image_path', type=str)
        current_time = datetime.now()

        args = parser.parse_args()
        args['date_added'] = current_time.strftime("%Y-%m-%d %H:%M:%S")

        new_food = Food(name=args['name'], taste=args['taste'],
                        region=args['region'], url=args['url'],
                        image_path=args['image_path'],
                        date_added=args['date_added'])

        db.session.add(new_food)
        db.session.commit()

        return jsonify(name=args['name'], taste=args['taste'],
                       region=args['region'], url=args['url'],
                       image_path=args['image_path'],
                       date_added=args['date_added'])


#######################################
# 'Drink' functions for API endpoints #
#######################################
class AllJapanDrinks(Resource):
    def get(self):
        all_drinks = Drink.query.all()
        result = drinks_schema.dump(all_drinks)
        return jsonify(result)


####################################
# Authentication related functions #
####################################
class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': 'User {} already exists'.format(data['username'])}

        new_user = UserModel(
            username=data['username'],
            password=UserModel.generate_hash(data['password'])
        )

        try:
            new_user.save_to_db()
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            return {
                'message': 'User {} was created'.format(data['username']),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = UserModel.find_by_username(data['username'])

        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}

        if UserModel.verify_hash(data['password'], current_user.password):
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])
            return {
                'message': 'Logged in as {}'.format(current_user.username),
                'access_token': access_token,
                'refresh_token': refresh_token
                }
        else:
            return {'message': 'Wrong credentials'}


class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Access token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class UserLogoutRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']
        try:
            revoked_token = RevokedTokenModel(jti=jti)
            revoked_token.add()
            return {'message': 'Refresh token has been revoked'}
        except:
            return {'message': 'Something went wrong'}, 500


class TokenRefresh(Resource):
    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}


##################################################
# 'Catch all' function for invalid API endpoints #
##################################################
class NotFound(Resource):
    def get(self, invalidPath=''):
        return jsonify(status=404, path=invalidPath,
                       message="This URL is not a valid API endpoint")
