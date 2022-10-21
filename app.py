from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from models import db


app = Flask(__name__)

# Sqlite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///starwars.db"

db.init_app(app)