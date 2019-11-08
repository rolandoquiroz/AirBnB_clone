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

    def __str__(self):
        """
        String representation of class BaseModel instance
        """
        return ('[{:s}] ({}) {}'.format(cls.__name__, self.id, self.__dict__))

    def save(self):
        """

        """
        self.updated_at = datetime.now()
        pass

    def to_dict(self):
        pass
