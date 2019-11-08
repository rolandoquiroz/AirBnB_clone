#!/usr/bin/python3
"""
module class BaseModel
"""
import uuid
from datetime import datetime, date, time
import json

class BaseModel:
    """
    The class BaseModel defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize instance attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """
        String representation of class BaseModel instance
        """
        return ('[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        my_dict = {}
        my_dict = self.__dict__.copy()
        my_dict.update(__class__ = self.__class__.__name__)
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()

        return my_dict
