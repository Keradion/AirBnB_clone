#!/usr/bin/python3
""" module holds class City definition """


class City(BaseModel):
    """ Inherit from BaseModel class """
    state_id: str = ''
    name: str = ''
