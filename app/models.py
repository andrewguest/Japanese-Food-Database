from app import db


class Candy(db.Model):
    __tablename__ = "Candy"
    candy_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    taste = db.Column(db.String(50))
    region = db.Column(db.String(50))
    url = db.Column(db.String(200))
    date_added = db.Column(db.DATETIME)
    image_path = db.Column(db.String(50))

    def __repr__(self):
        return '<Candy: {}>'.format(self.name)
