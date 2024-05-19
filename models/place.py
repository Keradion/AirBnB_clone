#!/usr/bin/python3
""" module holds class Place definition """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Inherit from BaseModel class """
    city_id = ""  # it will be the City.id
    user_id = ""  # it will be the user.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitiude = 0.0
    amenity_ids = []  # it will be the list of Amenity.id
