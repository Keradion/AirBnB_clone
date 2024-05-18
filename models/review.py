#!/usr/bin/python3
""" module holds class Review definition """
from models.base_model import BaseModel

class Review(BaseModel):
    """ Inherit from BaseModel class """
    place_id = ''  # it will be the place.id
    user_id = ''  # it wil be the user.id
    text = ''
