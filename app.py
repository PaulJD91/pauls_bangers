from flask import Flask, Blueprint
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

@app.route("/")
def home():
	return "This is the home page!"