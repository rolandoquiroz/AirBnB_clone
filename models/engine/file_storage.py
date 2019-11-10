#!/usr/bin/python3
"""
class FileStorage serializes instances to a JSON
file and deserializes JSON file to instances
"""

from models.base_model import BaseModel
import json

class FileStorage:
    """
    class Filestorage serializes instances to a
    JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns all the dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path)
        """

        """
        with open(__file_path, mode='a+', encoding='utf-8') as f:
            json.dump(__objects, f)
        """
        pass

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
        otherwise, do nothing.)
        """

        """
        with open(__file_path, encoding = 'utf-8') as f:
        json.load(f)
        """
        pass
