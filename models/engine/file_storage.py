#!/usr/bin/python3
""" Module holds class FileStorage Definition """
import os.path
import json
from models.base_model import BaseModel


class FileStorage:
    """ serializes/deserializes instances to or from json file """
    __file_path = "json.file"
    __objects = {}

    def all(self):
        """ returns __objects """
        return self.__objects

    def new(self, obj):
        """ set in __objects dict the obj with key <obj class name>.id """

        # key constructing
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to JSON file """
        new_dict = {}

        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()

        json_string = json.dumps(new_dict)

        with open(FileStorage.__file_path, "w") as jsonfile:
            # writing json string to file
            jsonfile.write(json_string)

    def reload(self):
        """ deserializes the JSON File to __objects """

        if os.path.exists(FileStorage.__file_path):
            # only if the JSON File exists
            try:
                with open(FileStorage.__file_path, "r") as jsonfile:
                    json_string = jsonfile.read()

                    my_dict = json.loads(json_string)

                    for key, value in my_dict.items():
                        # obj_class, obj.split()
                        # object class determining
                        # instance recreation
                        reloaded_object = BaseModel(**value)
                        # storing recreated instance to __object
                        FileStorage.new(self, reloaded_object)
            except FileNotFoundError:
                pass
