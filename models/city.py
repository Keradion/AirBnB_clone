#!/usr/bin/python3
""" module holds class City definition """
from model.base_model import BaseModel


class City(BaseModel):
    """ Inherit from BaseModel class """
    state_id: str = ''
    name: str = ''
