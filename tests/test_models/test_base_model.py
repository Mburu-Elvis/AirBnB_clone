#!/usr/bin/python3
import sys
import os
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel

""" Test case for BaseModel """


class TestBaseModel(unittest.TestCase):
    """ Test case for BaseModel """

    def test_init(self):
        """ Test case for class BaseModel __init__ method"""
        obj = BaseModel()
        my_dict = obj.to_dict()
        new_model = BaseModel(**my_dict)
        self.assertIsInstance(obj, BaseModel, msg=None)
        self.assertIsInstance(obj.id, str, msg=None)
        self.assertIsInstance(obj.created_at, datetime, msg=None)
        self.assertIsInstance(obj.updated_at, datetime, msg=None)
        self.assertEqual(obj.id, new_model.id)
        self.assertFalse(obj is new_model)

    def test_save(self):
        """ Test case for BaseModel save method """
        obj = BaseModel()
        original_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(original_updated_at, obj.updated_at, msg=None)

    def test_to_dict(self):
        """ Test case for BaseModel to_dict method """
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict, msg=None)
        self.assertIn('__class__', obj_dict, msg=None)
        self.assertEqual(obj_dict['__class__'], 'BaseModel', msg=None)
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_str(self):
        """Test the __str__ method of BaseModel."""
        obj = BaseModel()
        my_str = str(obj)
        my_test = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
        self.assertEqual(my_str, my_test)


if __name__ == '__main__':
    unittest.main()
