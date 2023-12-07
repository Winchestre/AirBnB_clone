#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime

class BaseModel():
    """Base class for other classes in the AirBnB clone"""

    def __init__(self, *args, **kwargs):
        """Initialize a new instance of the BaseModel"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
      """Returns official string representation"""

      return "[{}] ({}) {}".\
          format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        dictionary = dict(self.__dict__)
        dictionary["__class__"] = self.__class__.__name__
        for key, value in dictionary.items():
            if isinstance(value, datetime):
                dictionary[key] = datetime.isoformat(value)
        return dictionary
