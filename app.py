from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from models import db, User, Favorite, Character, Planet, Vehicle


app = Flask(__name__)
# Sqlite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///starwars.db"
db.init_app(app)
    
#funciones para agregar una fila
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

#funciones update

def update_user(id):
    user = User.query.get(id)
    user.password = "C123M456"

    db.session.commit()

def update_favorite(id):
    favorite = Favorite.query.get(id)
    favorite.name = "Darth Vader"

    db.session.commit()

def update_character(id):
    character = Character.query.get(id)
    character.hair_color = "light brown"

    db.session.commit()

def update_planet(id):
    planet = Planet.query.get(id)
    planet.population = 100000

    db.session.commit()

def update_vehicle(id):
    vehicle = Vehicle.query.get(id)
    vehicle.crew = 2

    db.session.commit()

#funciones select




#funciones delete


with app.app_context():
    #db.create_all()
    #add_user()
    #add_favorite()
    #add_character()
    #add_planet()
    #add_vehicle()
    #update_user(1)
    #update_favorite(1)
    #update_character(1)
    #update_planet(1)
    #update_vehicle(1)






app.run(host="localhost", port=8080)
