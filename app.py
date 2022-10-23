from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from models import db, User, Favorite, Character, Planet, Vehicle


app = Flask(__name__)
# Sqlite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///starwars.db"
db.init_app(app)
    

def add_user():
    user = User()
    user.name = "Camila"
    user.email = "c@c.com"
    user.password = "c12345"

    db.session.add(user)
    db.session.commit()

def add_favorite():
    favorite = Favorite()
    favorite.name = "Luke Skywalker"
    favorite.user_id = 1

    db.session.add(favorite)
    db.session.commit()

def add_character():
    character = Character()
    character.name = "Luke Skywalker"
    character.hair_color = "blond"
    character.birth_year = "19BBY"

    db.session.add(character)
    db.session.commit()

def add_planet():
    planet = Planet()
    planet.name = "Tatooine"
    planet.population = 200000
    planet.character_id = 1

    db.session.add(planet)
    db.session.commit()

def add_vehicle():
    vehicle = Vehicle()
    vehicle.name = "X wing"
    vehicle.crew = 1
    vehicle.character_id = 1

    db.session.add(vehicle)
    db.session.commit()


with app.app_context():
    db.create_all()
    #add_user()
    #add_favorite()
    #add_character()


app.run(host="localhost", port=8080)
