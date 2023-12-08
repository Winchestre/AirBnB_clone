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

    def method__error(self, name, arg):
        """Handler for methods error (helper function)
        return 0 if no error found otherwise 1
        """
        args = arg.split()

        if len(args) < 1 and name != "all":
            print("** class name missing **")
            return 1

        classes = HBNBCommand._all_classes
        if len(args) > 0 and args[0] not in classes:
            print("** class doesn't exist **")
            return 1

        if len(args) < 2 and name not in ["create", "all"]:
            print("** instance id missing **")
            return 1

        if name not in ["create", "all"]:
            instance_key = f'{args[0]}.{args[1]}'
            if instance_key not in storage.all():
                print("** no instance found **")
                return 1

        if name == "update":
            if len(args) < 3:
                print()
                return 1
if __name__ == "__main__":
    HBNBCommand().cmdloop()
