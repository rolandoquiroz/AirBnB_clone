#!/usr/bin/python3
"""
FileStorage Unit test
"""
import models
import unittest
import pep8
import os
import sys
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class Test_FileStorage(unittest.TestCase):
    """
    class FileStorage tests
    """

    @classmethod
    def setUpClass(cls):
        """
        SetUp
        """
        cls.usr1 = User()
        cls.usr1.first_name = "John"
        cls.usr1.last_name = "Doe"
        cls.usr1.email = "johndoe@gmail.com"
        cls.storage = FileStorage()
        fs = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """
        tearDown
        """
        pass

    def test_pep8_conformance_FileStorage(self):
        """
        Test that we conform to PEP8.
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_FileStorage_docs(self):
        """
        Test FileStorage documentation
        """
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)

    def test_FileStorage_instantiation(self):
        """Tests instantiation"""
        temp_storage = FileStorage()
        self.assertIsInstance(temp_storage, FileStorage)

    def test_FileStorage_saves_new_instance(self):
        """Tests if JSON file was created"""
        def touch(file_path):
            with open(file_path, 'a'):
                os.utime(file_path, None)

        obj = BaseModel()
        models.storage.new(obj)
        models.storage.save()
        touch(file_path="file.json")
        file_exist = os.path.exists(self.file_path)
        self.assertTrue(file_exist)

    def test_Filestorage_all(self):
        """Tests all method"""
        tmpstor = FileStorage()
        tmpdic = tmpstor.all()
        self.assertIsNotNone(tmpdic)
        self.assertEqual(type(tmpdic), dict)

    def test_Filestorage_new(self):
        """Tests new method"""
        tmpstor = FileStorage()
        tmpdic = tmpstor.all()
        Bob = User()
        Bob.id = 1996
        Bob.name = "Robert"
        tmpstor.new(Bob)
        k = "{}.{}".format(Bob.__class__.__name__, str(Bob.id))
        self.assertIsNotNone(tmpdic[k])

    def test_FileStorage_attributes(self):
        """Test FileStorage class attributes"""
        self.assertTrue(isinstance(storage._FileStorage__objects, dict))
        self.assertTrue(isinstance(storage._FileStorage__file_path, dict))

    def test_Filestorage_reload(self):
        """Tests reaload method """
        Bob = FileStorage()
        sizeofobj = len(Bob._FileStorage__objects)
        self.assertGreater(sizeofobj, 0)

if __name__ == "__main__":
    unittest.main()
