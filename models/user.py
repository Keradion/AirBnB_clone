#!/usr/bin/python3 
""" module holds definition of class User """ 
from model.base_model import BaseModel

class User(BaseModel):
    """ Extends BaseModel class """
    email: str = ''
    password: str = ''
    first_name: str = ''
    last_name: str = ''
