#!/usr/bin/python3
""" Module that defines class Basemodel """
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """ Defines common attributes/methods shared among other classes """

    def __init__(self, *args, **kwargs):
        """ Initialize Instance """

        if kwargs:
            # recreate an instance
            for key, value in kwargs.items():
                if key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.fromisoformat(value))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            # adding new instance to __objects
            models.storage.new(self)

    def __str__(self):
        """ Return String Representation """
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """ updtaes updated_at with current datetime """
        self.updated_at = datetime.now()
        # call to FileStorage save() to link BasModel and FileStorage
        models.storage.save()

    def to_dict(self):
        """ Returns a dictionary contaning all keys/values of/
        __dict__ of the instance """
        new_dict = {}

        for key, value in self.__dict__.items():
            if (key == 'created_at' or key == 'updated_at'):
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value

        new_dict['__class__'] = self.__class__.__name__
        return new_dict
