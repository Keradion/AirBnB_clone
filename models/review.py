#!/usr/bin/python3
""" module holds class Review definition """
form models.base_model import BaseModel

class Review(BaseModel):
    """ Inherit from BaseModel class """
    place_id: str = ''  # it will be the place.id
    user_id: str = ''  # it wil be the user.id
    text: str = ''
