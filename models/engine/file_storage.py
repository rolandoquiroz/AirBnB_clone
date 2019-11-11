#!/usr/bin/python3
"""
class FileStorage serializes instances to a JSON
file and deserializes JSON file to instances
"""
from models.base_model import BaseModel
import json

class FileStorage:
    """
    class FileStorage serializes instances to a
    JSON file and deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns all the dictionary __objects (instances)
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj (instance) with
        key <obj class name>.id value <obj>
        """
        self.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        Serializes __objects to JSON objects
        in the JSON file (path: __file_path)
        formatting obj by to_dict method
          """
        JSON_objects = {}
        for key, value in self.__objects.items():
            JSON_objects[key] = value.to_dict()
        with open(self.__file_path, mode='w', encoding='utf-8') as FILE:
            json.dump(JSON_objects, FILE)

    def reload(self):
        """
        Deserializes the JSON objects in the JSON file
        to __objects (only if the JSON file (__file_path) exists;
        otherwise, do nothing.)

        """
        try:
            with open(self.__file_path, mode="r", encoding = 'utf-8') as FILE:
                JSON_objects = json.load(FILE)
                for key, value in sorted(JSON_objects.items()):
                    class_name = value['__class__']
                    del value['__class__']
                    self.__objects[key] = eval(class_name)(**value)
        except FileNotFoundError:
            pass
