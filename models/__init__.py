#!/usr/bin/python
""" creates an instance of FilStorage class """
from .engine.file_storage import FileStorage
storage = FileStorage() #object inistantiated 
storage.reload() #calling reload method to deserialize objects 
