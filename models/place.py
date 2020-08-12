#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import String, Column, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    number_rooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    """
        Update Place: (models/place.py)

Place inherits from BaseModel and Base (respect the order)
Add or replace in the class Place:
class attribute __tablename__
    represents the table name, places
class attribute city_id
    represents a column containing a string (60 characters)
    can’t be null
    is a foreign key to cities.id
class attribute user_id
    represents a column containing a string (60 characters)
    can’t be null
    is a foreign key to users.id
class attribute name
    represents a column containing a string (128 characters)
    can’t be null
class attribute description
    represents a column containing a string (1024 characters)
    can be null
    class attribute number_rooms
represents a column containing an integer
    can’t be null
    default value: 0
    class attribute number_bathrooms
represents a column containing an integer
    can’t be null
    default value: 0
    class attribute max_guest
represents a column containing an integer
    can’t be null
    default value: 0
    class attribute price_by_night
represents a column containing an integer
    can’t be null
    default value: 0
class attribute latitude
    represents a column containing a float
    can be null
class attribute longitude
    represents a column containing a float
    can be null
"""
"""make sure in class USER-- class attribute places must represent a relationship with the class Place. If the User object is deleted, all linked Place objects must be automatically deleted. Also, the reference from a Place object to his User should be named user


in class CITY -- class attribute places must represent a relationship with the class Place. If the City object is deleted, all linked Place objects must be automatically deleted. Also, the reference from a Place object to his City should be named cities
"""
