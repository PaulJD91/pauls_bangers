from flask import Flask, Blueprint, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

import os
from dotenv import load_dotenv

load_dotenv()
PASSWORD = os.getenv('PASSWORD')

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://postgres:{PASSWORD}@localhost:5432/pauls_bangers"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
from models.mechanic import Mechanic
from models.car import Car

from controllers.car_controller import cars_blueprint
app.register_blueprint(cars_blueprint)

@app.route("/")
def home():
	return render_template("index.jinja")

