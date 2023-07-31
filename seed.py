from app import db
from models.mechanic import Mechanic
from models.car import Car
import click

from flask.cli import with_appcontext

@click.command(name='seed')
@with_appcontext
def seed():
    Mechanic.query.delete()
    Car.query.delete()
    mechanic1 = Mechanic(name="Jimmy Bob Bill")
    mechanic2 = Mechanic(name="Dougal")
    mechanic3 = Mechanic(name="Cletus")
    car1 = Car(manufacturer="Peugeot", model="106", year=1995, owner_name="Paul", owner_number="01311234567", mechanic_id=mechanic1.id)
    car2 = Car(manufacturer="Vauxhall", model="Corsa", year=2004, owner_name="Elle", owner_number="07144455566", mechanic_id=mechanic2.id)
    car3 = Car(manufacturer="Renault", model="Megane", year=1999, owner_name="Daniel", owner_number="01318889999", mechanic_id=mechanic3.id)
    car4 = Car(manufacturer="Seat", model="Leon", year=2014, owner_name="Kirsty", owner_number="01316667777", mechanic_id=mechanic1.id)
    car5 = Car(manufacturer="Mini", model="Cooper", year=2012, owner_name="Craig", owner_number="07112101999", mechanic_id=mechanic2.id)
    car6 = Car(manufacturer="Audi", model="A3", year=2007, owner_name="Mr Baines", owner_number="07498745600", mechanic_id=mechanic3.id)

    db.session.add(mechanic1)
    db.session.add(mechanic2)
    db.session.add(mechanic3)
    db.session.add(car1)
    db.session.add(car2)
    db.session.add(car3)
    db.session.add(car4)
    db.session.add(car5)
    db.session.add(car6)
    
    db.session.commit()