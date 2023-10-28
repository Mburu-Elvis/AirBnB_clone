#!/usr/bin/python3
"""Module containing class place"""
from models.base_model import BaseModel
from models.city import City
from models.user import User


class Place(BaseModel):
    """class Place definition"""

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0.0
    latitude = 0.0
    longitude = 0.0
    amenity_id = []