from datetime import datetime
import os

from flask_restful import Resource, reqparse
from flask import jsonify, json

from api import db, app

# from schema import FoodSchema, DrinkSchema
from models import Food, Drink, FoodSchema, DrinkSchema


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
class AllFood(Resource):
    def get(self):
        all_food = Food.query.all()
        result = foods_schema.dump(all_food)
        return jsonify(result)


class FoodLimit(Resource):
    def get(self, number_of_results):
        results = Food.query.limit(number_of_results).all()
        data = foods_schema.dump(results)
        return jsonify(data)


class SingleFood(Resource):
    def get(self, food_id):
        food_entry = Food.query.filter_by(food_id=food_id)
        result = food_schema.dump(food_entry)
        return jsonify(result)

    def post(self):
        parser.add_argument("key", type=str, required=True)
        parser.add_argument("name", type=str, required=True)
        parser.add_argument("taste", type=str, required=True)
        parser.add_argument("region", type=str, required=True)
        parser.add_argument("url", type=str, required=True)
        parser.add_argument("image_path", type=str)
        current_time = datetime.now()

        args = parser.parse_args()

        if args["key"] != os.getenv("API_KEY") or args["key"] is None:
            data = {"message": "Unauthorized"}
            return app.response_class(
                response=json.dumps(data), status=401, mimetype="application/json",
            )
        else:
            args["date_added"] = current_time.strftime("%Y-%m-%d %H:%M:%S")

            new_food = Food(
                name=args["name"],
                taste=args["taste"],
                region=args["region"],
                url=args["url"],
                image_path=args["image_path"],
                date_added=args["date_added"],
            )

            db.session.add(new_food)
            db.session.commit()
            db.session.close()

            return jsonify(
                status=200,
                message="Successfully added FOOD entry to the database:",
                name=args["name"],
                taste=args["taste"],
                region=args["region"],
                url=args["url"],
                image_path=args["image_path"],
                date_added=args["date_added"],
            )


#######################################
# 'Drink' functions for API endpoints #
#######################################
class AllDrinks(Resource):
    def get(self):
        all_drinks = Drink.query.all()
        result = drinks_schema.dump(all_drinks)
        return jsonify(result)


class SingleDrink(Resource):
    def get(self, drink_id):
        drink_entry = Drink.query.filter_by(drink_id=drink_id).limit(1)
        result = drink_schema.dump(drink_entry)
        return jsonify(result)

    def post(self):
        parser.add_argument("key", type=str, required=True)
        parser.add_argument("name", type=str, required=True)
        parser.add_argument("taste", type=str, required=True)
        parser.add_argument("region", type=str, required=True)
        parser.add_argument("url", type=str, required=True)
        parser.add_argument("image_path", type=str)
        current_time = datetime.now()

        args = parser.parse_args()

        if args["key"] != os.getenv("API_KEY") or args["key"] is None:
            data = {"message": "Unauthorized"}
            return app.response_class(
                response=json.dumps(data), status=401, mimetype="application/json",
            )
        else:
            args["date_added"] = current_time.strftime("%Y-%m-%d %H:%M:%S")

            new_drink = Drink(
                name=args["name"],
                taste=args["taste"],
                region=args["region"],
                url=args["url"],
                image_path=args["image_path"],
                date_added=args["date_added"],
            )

            db.session.add(new_drink)
            db.session.commit()
            db.session.close()

            return jsonify(
                status=200,
                message="Successfully added DRINK entry to the database:",
                name=args["name"],
                taste=args["taste"],
                region=args["region"],
                url=args["url"],
                image_path=args["image_path"],
                date_added=args["date_added"],
            )


##################################################
# 'Catch all' function for invalid API endpoints #
##################################################
class NotFound(Resource):
    def get(self, invalidPath=""):
        data = {"path": invalidPath, "message": "This URL is not a valid API endpoint"}
        return app.response_class(
            response=json.dumps(data), status=404, mimetype="application/json"
        )
