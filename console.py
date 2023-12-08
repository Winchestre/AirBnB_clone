#!/usr/bin/python3
""" Console module fo AirBnB Clone """
import cmd
import json
import re
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class for the console of AirBnB Clone"""

    prompt = "(hbnb) "
    _all_classes = {
            "BaseModel": BaseModel
    }

    def do_EOF(self, arg):
        """EOF (ctrl + d) command to exit the program
        """
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True
    
    def emptyline(self):
        """An empty line + ENTER command should not
        execute anything
        """
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
