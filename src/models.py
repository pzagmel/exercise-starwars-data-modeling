import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    email = Column(String(20), nullable=False)
    sub_date = Column(DateTime)
    password = Column(String(20), nullable=False)

class FavoriteCharacter(Base):
    __tablename__ = 'favoritecharacter'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('user.id'))
    Charcter_id = Column(Integer, ForeignKey('characters.id'))
    Add_date = Column(DateTime)
    Characters_relation = relationship('characters')
    User_relation = relationship('user')

    
class FavoritePlanet(Base):
    __tablename__ = 'favoriteplanet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('user.id'))
    Planets_id = Column(Integer, ForeignKey('planets.id'))
    Add_date = Column(DateTime)
    Planets_relation = relationship('planets')
    User_relation = relationship('user')
    
class Characters(Base):    
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True) 
    Name = Column(String(20), nullable=False)
    Age = Column(Integer, nullable=False)
    Birth_year = Column(Integer, nullable=False)
    Height = Column(Integer, nullable=False)
    Mass = Column(String(20), nullable=False)
    Hair_color = Column(String(10), nullable=False)
    Skin_color = Column(String(10), nullable=False)
    Eye_color = Column(String(10), nullable=False)
    Gender = Column(String(10), nullable=False)

class Planets(Base):    
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True) 
    Name = Column(String(50), nullable=False)
    Diameter = Column(Integer, nullable=False)
    Rotation_period = Column(Integer, nullable=False)
    Orbital_period = Column(Integer, nullable=False)
    Gravity = Column(String(20), nullable=False)
    Population = Column(Integer, nullable=False)
    Climate = Column(String(20), nullable=False)
    Terrain = Column(String(20), nullable=False)
    Surface_water = Column(Integer, nullable=False)
    
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
