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


class Candy(db.Model):
    __tablename__ = 'Candy'
    candy_id = db.Column(db.Integer, primary_key=True, unique=True)
    name = db.Column(db.String(150))
    taste = db.Column(db.String(50))
    region = db.Column(db.String(50))
    url = db.Column(db.String(200))
    date_added = db.Column(db.DATETIME)
    image_path = db.Column(db.String(50))

    def __init__(self, candy_id, name, taste, region, url, date_added, image_path):
        self.candy_id = candy_id
        self.name = name
        self.taste = taste
        self.region = region
        self.url = url
        self.date_added = date_added
        self.image_path = image_path

    def __repr__(self):
        return "<Candy: {}>".format(self.name)


class CandySchema(ma.ModelSchema):
    class Meta:
        model = Candy
        # Fields to expose
        # fields = ('name', 'taste', 'region', 'url', 'date_added')


candy_schema = CandySchema()
candies_schema = CandySchema(many=True)
parser = reqparse.RequestParser()


# endpoint to add new candy
class AllJapanCandy(Resource):
    def get(self):
        all_candy = Candy.query.all()
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

        return jsonify(name=args['name'], taste=args['taste'],
                       region=args['region'], url=args['url'],
                       image_path=args['image_path'],
                       date_added=args['date_added'])


class NotFound(Resource):
    def get(self, invalidPath=''):
        return jsonify(status=404, path=invalidPath, message="This URL is not a valid API endpoint")


'''
# endpoint to get user detail by id
@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)


# endpoint to update user
@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    user = User.query.get(id)
    name = request.json['name']
    taste = request.json['taste']

    user.taste = taste
    user.name = name

    db.session.commit()
    return user_schema.jsonify(user)


# endpoint to delete user
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)


if __name__ == '__main__':
    app.run(debug=True)
'''

api.add_resource(AllJapanCandy, '/api/japan/candy/all')
api.add_resource(SingleJapanCandy, '/api/japan/candy')
api.add_resource(NotFound, '/api/<path:invalidPath>')
