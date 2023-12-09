#!/usr/bin/python3
""" Console module fo AirBnB Clone """
import cmd
import json
import re
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class for the console of AirBnB Clone"""

    prompt = "(hbnb) "
    _all_classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
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

    def do_create(self, arg):
        """Usage: create <class>
        Create a new class instance and print its id.
        """
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand._all_classes:
            print("** class doesn't exist **")
        else:
            created_instance = eval(arg)()
            storage.save()
            print(created_instance.id)

    def do_show(self, arg):
        """Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in HBNBCommand._all_classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                key = "{}.{}".format(class_name, instance_id)
                objects = storage.all()
                if key in objects:
                    print(objects[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id."""
        if not arg:
            print("** class name missing **")
        else:
            args = arg.split()
            class_name = args[0]
            if class_name not in HBNBCommand._all_classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                instance_id = args[1]
                key = "{}.{}".format(class_name, instance_id)
                objects = storage.all()
                if key in objects:
                    del objects[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""

        objects = storage.all()

        if arg:
            args = arg.split()
            if args[0] not in HBNBCommand._all_classes:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects.values() if obj.__class__.__name__ == args[0]])
        else:
            print([str(obj) for obj in objects.values()])

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
        <class>.update(<id>, <attribute_name>, <attribute_value>) or
        <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""

        args = arg.split()
        if not args or len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in HBNBCommand._all_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        attribute_name = args[2]
        if len(args) == 3:
            print("** value missing **")
            return
        attribute_value = args[3]
        try:
            attribute_value = eval(attribute_value)
        except (NameError, SyntaxError):
            pass
        if attribute_name not in ["id", "created_at", "updated_at"]:
            setattr(objects[key], attribute_name, attribute_value)
            storage.save()
        else:
            print("** attribute cannot be updated **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
