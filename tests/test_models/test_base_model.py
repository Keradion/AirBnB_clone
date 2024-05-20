#!/usr/bin/python3
"""
Module holds unitttes for BaseModule class
"""

import unittest
from models.base_model import BaseModel


class Test_base_model(unittest.TestCase):
    """
    provide test functions for BaseModel
    functionalities
    """

    def test_save(self):
        """ Test save() """

    def test_to_dict(self):
        """ Test to_dict() """

    def test_id(self):
        """ Test id attribute of BaseModel """

        # Test for unique id generation between objects  
        obj1 = BaseModel()
        obj2 = BaseModel()

        self.assertNotEqual(obj1.id, obj2.id)

    def test_created_at(self):
        """ Test created_at atrribute of BaseModel """

    def test_str(self):
        """ Test str() """
        obj1 = BaseModel() 
        # expected output from print(obj1)
        expected_output = '[BaseModel] ({}) {}'.format(obj1.id, obj1.__dict__)
        self.assertEqual(str(obj1), expected_output)


if __name__ == '__main__':
    unittest.main()
