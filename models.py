from app import db

class CarShop(db.Model):
    __tablename__ = "CarShop"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))


class Car(db.Model):
    __tablename__ = "Cars"
    id = db.column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    year = db.Column(db.DateTime)
    mileage = db.Column(db.Integer)
    