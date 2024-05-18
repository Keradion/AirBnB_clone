#!/usr/bin/python
""" creates an instance of FilStorage class """
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
