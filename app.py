from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from models import db, User, Favorite, Character, Planet, Vehicle


app = Flask(__name__)
# Sqlite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///starwars.db"
db.init_app(app)

#with app.app_context():
#    db.create_all()




app.run(host="localhost", port=8080)
