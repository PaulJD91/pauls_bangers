from app import db

class Car(db.Model):
    __tablename__ = "Cars"
    id = db.Column(db.Integer, primary_key=True)
    manufacturer = db.Column(db.String(64))
    model = db.Column(db.String(64))
    year = db.Column(db.Integer)
    owner_name = db.Column(db.String(64))
    owner_number = db.Column(db.Integer)
    mechanic_id = db.Column(db.Integer, db.ForeignKey("Mechanic.id"))
    