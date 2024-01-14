#!/usr/bin/python3
""" This module is the entry point for the command interpreter in our app.

It defines a class called `HBNBCommand()`, which is a subclass
of the `cmd.Cmd` class. The purpose of this module is to provide abstractions
that allow manipulation of a robust storage system (FileStorage / DB).
These abstractions facilitate the seamless switching of storage types without
the need to update the entire codebase.

The functionality enables interactive and non-interactive operations, such as:
  - Creating a data model
  - Managing (create, update, destry, ...) objects by a console / interpreter
  - Storing and persisting objects to a file (JSON file)

Example of typical usage:

    $ ./console
    (hbnb)

    (hbnb) help
    Documented commands (type help <topic>):
    ========================================
    EOF  create  help  quit

    (hbnb)
    (hbnb) quit
    $
"""
import re
import cmd
import sys
from models.engine.file_storage import models_dict
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    # aliases
    do_EOF = do_quit

    def precmd(self, line):
        if not sys.stdin.isatty():
            print("")
        return super().precmd(line)

    def emptyline(self):
        """an empty line + ENTER does not execute anything"""
        pass

    # task 7 adding (create, show, all, and destroy) commands
    def do_create(self, my_model):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        USAGE: <create> <BaseModel>
        Ex: create BaseModel
        """

        if len(my_model) == 0:
            print("** class name missing **")
        else:
            if my_model not in models_dict:
                print("** class doesn't exist **")
            else:
                new = models_dict[my_model]()
                new.save()
                print(new.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on
        the class name and id.
        USAGE: <show> <BaseModel> <id>
        Ex: $ show BaseModel 1234-1234-1234
        """

        args = args.split(" ")
        if args[0] == '':
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in models_dict:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            if f'{args[0]}.{args[1]}' not in storage.all().keys():
                print('** no instance found **')
            else:
                print(storage.all()[f'{args[0]}.{args[1]}'])

    def do_all(self, model=''):
        """Prints all string representation of all instances based
        or not on the class name.
        USAGE: <all> / <all> <BaseModel>
        Ex: $ all   / $ all BaseModel"""

        list_instances = []
        if len(model) == 0:
            for val in storage.all().values():
                list_instances.append(str(val))
        else:
            if model not in models_dict:
                print("** class doesn't exist **")
                return
            for key, val in storage.all().items():
                if model in key:
                    list_instances.append(str(val))
        if not list_instances:
            return
        else:
            print(list_instances)

    def do_update(self, args):
        """Updates an instance based on the class name and id.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Ex:  $ update BaseModel 1234-1234-1234 email "airbnb@mail.com"
        """

        args = args.split(" ")
        if args[0] == '':
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in models_dict:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        elif len(args) == 2:
            if f'{args[0]}.{args[1]}' not in storage.all().keys():
                print('** no instance found **')
            else:
                print('** attribute name missing **')
        elif len(args) == 3:
            print('** value missing **')
        else:
            pattern = r'^"\w{1,}"$'
            match = re.match(pattern, args[3])
            if match:
                args[3] = args[3].replace('"', '')
                val = {
                    'model': args[0],
                    'id': args[1],
                    'attribute': args[2],
                    'value': args[3]
                }
                up_ob = storage.all()[f"{val['model']}.{val['id']}"].__dict__
                up_ob.update({val['attribute']: val['value']})
                new = storage.all()[f"{val['model']}.{val['id']}"]
                new.save()
            else:
                return

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id.
        USAGE: <destroy> <BaseModel> <id>
        Ex: $ destroy BaseModel 1234-1234-1234"""

        args = args.split(" ")
        if args[0] == '':
            print("** class name missing **")
        elif len(args) == 1:
            if args[0] not in models_dict:
                print("** class doesn't exist **")
            else:
                print("** instance id missing **")
        else:
            if f'{args[0]}.{args[1]}' not in storage.all().keys():
                print('** no instance found **')
            else:
                storage.all().pop(f'{args[0]}.{args[1]}')
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
