import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
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
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    date_sub = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

class FavoriteCharacter(Base):
    __tablename__ = 'favoritecharacter'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('User.id'))
    CharacterName = Column(String(250), nullable=False)
    
class FavoritePlanet(Base):
    __tablename__ = 'favoriteplanet'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('User.id'))
    PlanetName = Column(String(250), nullable=False)
    
class Characters(Base):    
    __tablename__ = 'Characters'
    id = Column(Integer, primary_key=True) 
    Name = Column(String(50), nullable=False)
    Age = Column(Integer, nullable=False)
    Birth_year = Column(Integer, nullable=False)
    Height = Column(Integer(50), nullable=False)
    Mass = Column(String(50), nullable=False)
    Hair_color = Column(String(10), nullable=False)
    Skin_color = Column(String(10), nullable=False)
    Eye_color = Column(String(10), nullable=False)
    Gender = Column(String(10), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
