from datetime import datetime

from flask_restful import Resource, reqparse
from flask import jsonify

from api import db
from schema import FoodSchema, DrinkSchema
from models import Food, Drink


parser = reqparse.RequestParser()

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


##################################################
# 'Catch all' function for invalid API endpoints #
##################################################
class NotFound(Resource):
    def get(self, invalidPath=''):
        return jsonify(status=404, path=invalidPath,
                       message="This URL is not a valid API endpoint")
