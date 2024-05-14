#!/usr/bin/python3
""" Module that defines class Basemodel """
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ Defines common attributes/methods shared among other classes """

    def __init__(self):
        """ Initialize Instance """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.update_at = self.created_at

    def __str__(self):
        """ Return String Representation """
        return ('([{}] ({}) {})'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ updtaes updated_at with current datetime """
        self.update_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary contaning all keys/values of/
        __dict__ of the instance """
        new_dict = {}

        for key, value in self.__dict__.items():
            if (key == 'created_at' or key == 'update_at'):
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value

        new_dict['__class__'] = self.__class__.__name__
        return new_dict
