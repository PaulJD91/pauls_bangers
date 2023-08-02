from flask import Flask, Blueprint, render_template, redirect, request
from app import db
from models.mechanic import Mechanic
from models.car import Car

cars_blueprint = Blueprint("cars", __name__)

@cars_blueprint.route("/cars")
def cars():
	cars = Car.query.all()
	return render_template("cars/list.jinja",
			cars = cars)

@cars_blueprint.route("/cars/<id>")
def show_car(id):
	car = Car.query.get(id)
	mechanic = Mechanic.query.get(car.mechanic_id)
	return render_template("cars/show.jinja", car=car, mechanic=mechanic)


@cars_blueprint.route("/cars/new", methods=['GET'])
def new_visit():
    car = Car.query.all()
    return render_template("cars/new.jinja", car=car)

@cars_blueprint.route("/cars", methods=['POST'])
def create_booking():
    manufacturer = request.form['manufacturer']
    model = request.form['model']
    year = request.form['year']
    owner_name = request.form['owner_name']
    owner_number = request.form['owner_number']
    from sqlalchemy.sql.expression import func

    mechanic = Mechanic.query.order_by(func.random()).first()

    
    car = Car(manufacturer=manufacturer, model=model, year=year, owner_name=owner_name, owner_number=owner_number, mechanic_id=mechanic.id)
    db.session.add(car)
    db.session.commit()
    return redirect("/cars")

@cars_blueprint.route("/cars/<id>/delete", methods=["POST"])
def delete_booking(id):
    car = Car.query.get(id)
    db.session.delete(car)

    db.session.commit()
    return redirect("/cars")

@cars_blueprint.route("/cars/<id>/edit", methods=['GET'])
def get_edit_page(id):
    car = Car.query.get(id)
    return render_template("cars/edit.jinja", car=car)

@cars_blueprint.route("/cars/<id>/edit", methods=["POST"])
def edit_booking(id):
    car = Car.query.get(id)
    car.manufacturer = request.form['manufacturer']
    car.model = request.form['model']
    car.year = request.form['year']
    car.owner_name = request.form['owner_name']
    car.owner_number = request.form['owner_number']

    db.session.commit()
    return redirect("/cars")
     

    
    
     



	
