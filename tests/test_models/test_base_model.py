#!/usr/bin/python3
""" unittest for bases """
import json
import unittest
from models.base_model import BaseModel
import datetime from datetime
import models
from io import StringIO
import sys
from unittest.mock import patch
get_out = StringIO()
sys.stdout = get_out


class BaseModelTestCase(unittest.TestCase):
    """ class for base test """

    def setUp(self):
        """ class for base test """
        self.filepath = models.storage.FileStorage.__file_path
        with open(self.filepath, 'w') as file:
            file.truncate(0)
        models.storage.all().clear()

    def tearDown(self):
        """ class for base test """
        print_out = get_out.getvalue()
        sys.stdout = sys.__stdout__

    def test_basemodel_init(self):
        """ class for base test """
        new = BaseModel()

        """ check for methods """
        self.assertTrue(hasattr(new, "__init__"))
        self.assertTrue(hasattr(new, "__str__"))
        self.assertTrue(hasattr(new, "save"))
        self.assertTrue(hasattr(new, "to_dict"))

        """ check for instance attributes """
        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))

        """ type test """
        self.assertIsInstance(new.id, str)

        """ check if save in storage """
        key_name = f'BaseModel.{new.id}'

        """ check if object exists by key_name """
        self.assertIn(key_name, models.storage.all())

        """ check if object in storage has correct id """
        self.assertTrue(models.storage.all()[key_name] is new)

        """ Test update """
        new.name = "My First Model"
        new.my_number = 89
        self.assertTrue(hasattr(new, "name"))
        self.assertTrue(hasattr(new, "my_number"))
        self.assertTrue(hasattr(models.storage.all()[key_name], "name"))
        self.assertTrue(hasattr(models.storage.all()[key_name], "my_number"))

        """ check if save() updates update_at attribute """
        init_time = new.updated_at
        new.save()
        self.assertNotEqual(init_time, new.updated_at)
        self.assertGreater(new.updated_at, init_time)

        """ check initial call of models.storage.save() """
        with patch('models.storage.save') as mock_func:
            obj = BaseModel()
            obj.save()
            mock_func.assert_called_once()

        """ check if file saved in file.json """
        with open(self.filepath, "r") as file:
            saved_json = json.load(file)

        """ check if object exists by key_name """
        self.assertIn(key_name, saved_json)

        """ check if json object is correct """
        self.assertEqual(saved_json[key_name], new.to_dict())

    def test_basemodel_init2(self):
        """ class for base test """

        new = BaseModel()
        new.name = "John"
        new.my_number = 89
        new2 = BaseModel(**new.to_dict())
        self.assertEqual(new.id, new2.id)
        self.assertEqual(new.name, "John")
        self.assertEqual(new.my_number, 89)
        self.assertEqual(new.to_dict(), new2.to_dict())

    def test_basemodel_init3(self):
        """ class for base test """
        new = BaseModel()
        new2 = BaseModel(new.to_dict())
        self.assertNotEqual(new, new2)
        self.assertNotEqual(new.id, new2.id)

        new = BaseModel()
        base_str = f'[BaseModel] ({new.id}) {new.__dict__}'
        self.assertEqual(str(new), base_str)

        init_time = new.updated_at
        new.save()
        self.assertGreater(new.updated_at, init_time)


if __name__ == "__main__":
    unittest.main()
