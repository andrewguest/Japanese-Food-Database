from api import db, ma


class Food(db.Model):
    food_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(150))
    taste = db.Column(db.String(50))
    region = db.Column(db.String(50))
    url = db.Column(db.String(200))
    date_added = db.Column(db.DATETIME)
    image_path = db.Column(db.String(50))

    def __init__(self, name, taste, region, url, date_added, image_path):
        self.name = name
        self.taste = taste
        self.region = region
        self.url = url
        self.date_added = date_added
        self.image_path = image_path

    def __repr__(self):
        return "<Food: {}>".format(self.name)


class Drink(db.Model):
    drink_id = db.Column(db.Integer, primary_key=True, unique=True, autoincrement=True)
    name = db.Column(db.String(150))
    taste = db.Column(db.String(50))
    region = db.Column(db.String(50))
    url = db.Column(db.String(200))
    date_added = db.Column(db.DATETIME)
    image_path = db.Column(db.String(50))

    def __init__(self, name, taste, region, url, date_added, image_path):
        self.name = name
        self.taste = taste
        self.region = region
        self.url = url
        self.date_added = date_added
        self.image_path = image_path

    def __repr__(self):
        return "<Drink: {}>".format(self.name)


class FoodSchema(ma.ModelSchema):
    class Meta:
        model = Food


class DrinkSchema(ma.ModelSchema):
    class Meta:
        model = Drink
