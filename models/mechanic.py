from app import db

class Mechanic(db.Model):
    __tablename__ = "Mechanic"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    cars = db.relationship('Cars', backref='Mechanic')