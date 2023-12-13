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

    class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        del self.console
        storage.reset()

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_show(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help show")
            self.assertIn("Display the string representation", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))

    def test_emptyline(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertIsNone(self.console.emptyline())

    @patch('sys.stdout', new_callable=StringIO)
    def test_method_error(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.method__error("create", "User")
            self.assertIn("** instance id missing **", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_default(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.default("create User")
            self.assertIn("created", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            self.assertIn(user_id, storage.all(User).keys())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            self.console.onecmd("show User {}".format(user_id))
            self.assertIn(user_id, mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            self.console.onecmd("destroy User {}".format(user_id))
            self.assertNotIn(user_id, storage.all(User).keys())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            self.console.onecmd("create State")
            self.console.onecmd("all")
            self.assertIn("User", mock_stdout.getvalue().strip())
            self.assertIn("State", mock_stdout.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            self.console.onecmd('update User {} name "John"'.format(user_id))
            self.assertIn("John", storage.all(User)[user_id].name)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_by_attribute(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            self.console.update_by_attribute("User", user_id, "name", "John")
            self.assertIn("John", storage.all(User)[user_id].name)

    @patch('sys.stdout', new_callable=StringIO)
    def test_update_by_dictionary(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create User")
            user_id = f.getvalue().strip()
            attribute_dict = {"name": "John", "age": 25}
            self.console.update_by_dictionary("User", user_id, attribute_dict)
            self.assertIn("John", storage.all(User)[user_id].name)
            self.assertEqual(25, storage.all(User)[user_id].age)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_count(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd('User.count()')
            self.assertIn("0", mock_stdout.getvalue().strip())
            self.console.onecmd("create User")
            self.console.onecmd('User.count()')
            self.assertIn("1", mock_stdout.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
