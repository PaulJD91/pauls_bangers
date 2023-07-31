from app import db

class Mechanic(db.Model):
    __tablename__ = "mechanic"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    cars = db.relationship('Car', backref='mechanic')