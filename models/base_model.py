#!/usr/bin/python3
"""BaseModel is a class that encapsulates shared attributes
and method, serving as a bluprint for other classes. It
manages the initialization, serialization, and deserial-
ization of future instances, ensuring consistent their
consistent handling
"""
from uuid import uuid4
from datetime import datetime

class BaseModel():
    """Base class for other classes in the AirBnB clone"""

    def __init__(self, *args, **kwargs):
        """Constructor for the BaseModel class.
        Args:
            *args: Variable number of positional arguments.
            **kwargs: Keyword arguments.
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        format = "%Y-%m-%dT%H:%M:%S.%f"
                        value = datetime.strptime(value, format)
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
      """Returns official string representation

      Returns:
        str: A string containing the class name, the objects ID,
        and its attributes.
      """

      return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        """Updates the "updated_at" attribute with the current
        timestamp.

        Returns:
            None
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary representation of the object.

         Returns:
            dict: A dictionary containing the objects attributes and
            the "__class__" key with the class name. Datetime objects
            are converted to ISO formatted strings.
        """

        dictionary = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                dictionary[key] = value.isoformat()
            else:
                dictionary[key] = value
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
