#!/usr/bin/python3
"""
module class BaseModel
"""
import models
from datetime import datetime
from uuid import uuid4


class BaseModel:
    """
    The class BaseModel defines all common
    attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize instance attributes
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, time_format)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        String representation of class BaseModel instance
        """
        return ('[{}] ({}) {}'.format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """
        Updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values
        of __dict__ of the instance.
        """
        my_dict = {}
        my_dict = self.__dict__.copy()
        my_dict.update(__class__=self.__class__.__name__)
        my_dict['created_at'] = my_dict['created_at'].isoformat()
        my_dict['updated_at'] = my_dict['updated_at'].isoformat()
        return my_dict
