from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(250))
    password = db.Column(db.String(10))
    favorites = db.relationship("Favorite")

class Favorite(db.Model):
    __tablename__ = "favorites"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False) 

class Character(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    hair_color = db.Column(db.String(100))
    birth_year = db.Column(db.String(100))
    planet = db.relationship("Planet", back_populates="character", uselist=False)
    vehicle = db.relationship("Vehicle", back_populates="character", uselist=False)

class Planet(db.Model):
    __tablename__ = "planets"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    population = db.Column(db.Integer)
    character_id = db.Column (db.Integer, db.ForeignKey("characters.id"))
    character = db.relationship("Character", back_populates="planet")

class Vehicle(db.Model):
    __tablename__ = "vehicles"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    crew = db.Column(db.Integer)
    character_id = db.Column(db.Integer, db.ForeignKey("characters.id"))
    character = db.relationship("Character", back_populates="vehicle")