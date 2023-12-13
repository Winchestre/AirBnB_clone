#!/usr/bi/python3
""" Unittest for console """
import unittest
import console
HBNBCmd = console.HBNBCommand
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class TestConsoleDocs(unittest.TestCase):
    """ console unittest class """
    def test_console_module_docstring(self):
        """ Test for the console.py module docstring """
        console_doc = console.__doc__
        self.assertIsNot(console_doc, None, "console.py needs a docstring")
        self.assertTrue(len(console_doc) >= 1, "console.py needs a docstring")

    def test_HBNBCommand_class_docstring(self):
        """ Test for the HBNBCommand class docstring """
        self.assertIsNot(HBNBCmd.__doc__, None, "HBNBCmd needs a docstring")
        self.assertTrue(len(HBNBCmd.__doc__) >= 1, "HBNBCmd needs a docstring")

if __name__ == '__main__':
    unittest.main()
