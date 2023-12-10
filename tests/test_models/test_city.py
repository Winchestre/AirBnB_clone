#!/usr/bin/python3
""" unittest for City class """
import unittest
from models.city import City
from datetime import datetime


class CityTestCase(unittest.TestCase):
    """ class for City test """

    def test_city(self):
        """ check for instance attributes """
        new = City()
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "state_id"))
        self.assertTrue(hasattr(new, "name"))

        "type test"
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.state_id, str)
        self.assertIsInstance(new.name, str)


if __name__ == "__main__":
    unittest.main()
