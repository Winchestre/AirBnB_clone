#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
import models

class BaseModel():

    def __init__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__():
        print(f"[{self.__classname__}] ({self.id}) {self.__dict__}")

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = self.__class__.__name__
        for key, value in dictionary.items():
            if isinstance(value, datetime):
                dictionary[key] = datetime.isoformat(value)
        return dictionary
