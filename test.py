#!/usr/bin/python3

# test_basemodel_creation.py
from models.base_model import BaseModel

def test_basemodel_creation():
    print("Creating BaseModel instance without kwargs...")
    instance = BaseModel()
    print("Instance created:", instance)

    print("Creating BaseModel instance with kwargs...")
    kwargs = {
        'id': '12345',
        'created_at': '2023-05-18T12:00:00',
        'updated_at': '2023-05-18T12:00:00',
        'name': 'test'
    }
    instance_with_kwargs = BaseModel(**kwargs)
    print("Instance with kwargs created:", instance_with_kwargs)

if __name__ == '__main__':
    test_basemodel_creation()
