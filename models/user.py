#!/usr/bin/python3 
""" module holds definition of class User """ 
from models.base_model import BaseModel

class User(BaseModel):
    """ Extends BaseModel class """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
