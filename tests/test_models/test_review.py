#!/usr/bin/python3
"""
Review test for User
"""
import unittest
import pep8
from models.base_model import BaseModel
from models.review import Review
from datetime import datetime
from uuid import uuid4
import json


class testReview(unittest.TestCase):
    """
    class Review tests
    """

    @classmethod
    def setUpClass(cls):
        """
        SetUp
        """
        cls.obj1 = BaseModel()
        cls.obj1.name = "McLovin"
        cls.obj1.my_num = 666

    @classmethod
    def tearDownClass(cls):
        """
        tearDown
        """
        del cls.obj1

    def test_pep8_conformance(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_docs(self):
        """
        Test documentation
        """

        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_id(self):
        """
        test id
        """
        self.assertEqual(str, type(self.obj1.id))

    def test_created_at(self):
        """
        test created_at
        """
        self.assertEqual(datetime, type(self.obj1.created_at))

    def test_updated_at(self):
        """
        test updated_at
        """
        self.assertEqual(datetime, type(self.obj1.updated_at))

    def test_attributes(self):
        """
        test methods
        """
        self.assertTrue(hasattr(self.obj1, "__init__"))
        self.assertTrue(hasattr(self.obj1, "created_at"))
        self.assertTrue(hasattr(self.obj1, "updated_at"))
        self.assertTrue(hasattr(self.obj1, "id"))

    def test_to_dict(self):
        """
        test_to_dict
        """
        obj1_dict = self.obj1.to_dict()
        self.assertIsInstance(obj1_dict, dict)
        self.assertIsInstance(obj1_dict['id'], str)
        self.assertIsInstance(obj1_dict['updated_at'], str)
        self.assertIsInstance(obj1_dict['created_at'], str)
        self.assertEqual(obj1_dict['__class__'], self.obj1.__class__.__name__)


if __name__ == "__main__":
    unittest.main()
