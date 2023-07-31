from app import db
from models.mechanic import Mechanic

class Car(db.Model):
    __tablename__ = "cars"
    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String(64))
    model = db.Column(db.String(64))
    year = db.Column(db.Integer)
    owner_name = db.Column(db.String(64))
    owner_number = db.Column(db.String(64))
    mechanic_id = db.Column(db.Integer, db.ForeignKey("mechanic.id"))
    