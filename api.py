from os import getenv

from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)

mysql_name = getenv('MYSQL_USERNAME')
mysql_password = getenv('MYSQL_PASSWORD')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@localhost/Japan'.format(mysql_name, mysql_password)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

#####################
# SQLAlchemy models #
#####################
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


#######################
# Marshmallow Schemas #
#######################
class CandySchema(ma.ModelSchema):
    class Meta:
        model = Candy
        # Fields to expose
        # fields = ('name', 'taste', 'region', 'url', 'date_added')


candy_schema = CandySchema()


####################################
# Defining flask_restful functions #
####################################
class GetAllJapanCandy(Resource):
    def get(self):
        candies_schema = CandySchema(many=True)
        all_candy = Candy.query.all()
        result = candies_schema.dump(all_candy)
        return jsonify(result)

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
#################################################
# API endpoints mapped to their Python function #
#################################################
api.add_resource(GetAllJapanCandy, '/japan/candy')
