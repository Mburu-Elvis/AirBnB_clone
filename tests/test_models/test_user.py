#!/usr/bin/python3
import sys
import os
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel
from models.user import User

""" Test case for User """


class TestUser(unittest.TestCase):
    """ Test case for User """

    def test_init(self):
        """ Test case for class User __init__ method"""
        obj = User()
        my_dict = obj.to_dict()
        new_model = User(**my_dict)
        self.assertIsInstance(obj, User, msg=None)
        self.assertIsInstance(obj.id, str, msg=None)
        self.assertIsInstance(obj.created_at, datetime, msg=None)
        self.assertIsInstance(obj.updated_at, datetime, msg=None)
        self.assertEqual(obj.id, new_model.id)
        self.assertFalse(obj is new_model)

    def test_attributes(self):
        """Test for attributes"""
        obj = User()
        self.assertEqual(obj.email, '')
        self.assertEqual(obj.password, '')
        self.assertEqual(obj.first_name, '')
        self.assertEqual(obj.last_name, '')

    def test_save(self):
        """ Test case for User save method """
        obj = User()
        original_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(original_updated_at, obj.updated_at, msg=None)

    def test_to_dict(self):
        """ Test case for User to_dict method """
        obj = User()
        obj_dict = obj.to_dict()
        self.assertIsInstance(obj_dict, dict, msg=None)
        self.assertIn('__class__', obj_dict, msg=None)
        self.assertEqual(obj_dict['__class__'], 'User', msg=None)
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_str(self):
        """Test the __str__ method of User."""
        obj = User()
        my_str = str(obj)
        my_test = f"[{obj.__class__.__name__}] ({obj.id}) {obj.__dict__}"
        self.assertEqual(my_str, my_test)


if __name__ == '__main__':
    unittest.main()
