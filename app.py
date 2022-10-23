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
    user.name = "Francisca"
    user.email = "c@c.com"
    user.password = "c12345"

    db.session.add(user)
    db.session.commit()

def add_favorite():
    favorite = Favorite()
    favorite.name = "Luke Skywalker"
    favorite.user_id = 2

    db.session.add(favorite)
    db.session.commit()

def add_character():
    character = Character()
    character.name = "Darth Vader"
    character.hair_color = "unknow"
    character.birth_year = "41.9BBY"

    db.session.add(character)
    db.session.commit()

def add_planet():
    planet = Planet()
    planet.name = "Alderaan"
    planet.population = 200000000
    planet.character_id = 2

    db.session.add(planet)
    db.session.commit()

def add_vehicle():
    vehicle = Vehicle()
    vehicle.name = "Death Star"
    vehicle.crew = 1000000
    vehicle.character_id = 2

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

def select_user():
    users = User.query.all()
    users = list(map(lambda user: user.name, users))

    print(users)

def select_favorite():
    favorites = Favorite.query.all()
    favorites = list(map(lambda favorite: favorite.name, favorites))

    print(favorites)

def select_character():
    characters = Character.query.all()
    characters = list(map(lambda character: character.name, characters))

    print(characters)

def select_planet():
    planets = Planet.query.all()
    planets = list(map(lambda planet: planet.name, planets))

    print(planets)

def select_vehicle():
    vehicles = Vehicle.query.all()
    vehicles = list(map(lambda vehicle: vehicle.name, vehicles))

    print(vehicles)

#funciones delete

def delete_favorite(id):
    favorite = Favorite.query.get(id)

    db.session.delete(favorite)
    db.session.commit()

def delete_user(id):
    user = User.query.get(id)

    db.session.delete(user)
    db.session.commit()

def delete_character(id):
    character = Character.query.get(id)

    db.session.delete(character)
    db.session.commit()

def delete_planet(id):
    planet = Planet.query.get(id)

    db.session.delete(planet)
    db.session.commit()

def delete_vehicle(id):
    vehicle = Vehicle.query.get(id)

    db.session.delete(vehicle)
    db.session.commit()



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
    #select_user()
    #select_favorite()
    #select_character()
    #select_planet()
    #select_vehicle()
    #delete_favorite(2)
    #delete_user(2)
    delete_character(2)
    delete_planet(2)
    delete_vehicle(2)




app.run(host="localhost", port=8080)
