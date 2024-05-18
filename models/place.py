#!/usr/bin/python3
""" module holds class Place definition """
from model.base_model import BaseModel


class Place(BaseModel):
    """ Inherit from BaseModel class """
    city_id: str = ''  # it will be the City.id
    user_id: str = ''  # it will be the user.id
    name: str = ''
    description: str = ''
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longtiude: float = 0.0
    amenity_ids: []  # it will be the list of Amenity.id
