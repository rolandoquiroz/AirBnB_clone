#!/usr/bin/python3
"""
class FileStorage serializes instances to a JSON
file and deserializes JSON file to instances
"""
from models import BaseModel
import json

class FileStorage:

    __file_path = "file.json"

    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects
        """
        return __objects

    def new(self, obj):

        __objects[obj.self.id] = obj.__dict__

    def save(self):
        with open(__file_path, mode='a+', encoding='utf-8') as f:
            json.dump(__objects, f)

    def reload(self):
        with open(__file_path, encoding = 'utf-8') as f:
        json.load(f)
