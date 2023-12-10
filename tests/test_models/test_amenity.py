#!/usr/bin/python3
""" unittest for Amenity class """
import unittest
from models.amenity import Amenity
from datetime import datetime


class AmenityTestCase(unittest.TestCase):
    """ class for Amenity test """

    def test_amenity(self):
        """ check for instance attributes """
        new = Amenity()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "name"))

        "type test"
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.name, str)


if __name__ == "__main__":
    unittest.main()
