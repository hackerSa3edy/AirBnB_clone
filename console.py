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
import json
import cmd
import re
import sys
from models.engine.file_storage import models_dict
from models import storage


def from_json_string(my_str):
    """

    :param my_str: a JSON string
    :return: an object
    """
    return json.loads(my_str)


class HBNBCommand(cmd.Cmd):
    """HBNBCommand Module to manage objects by interpreter

    Arguments:
        cmd -- Inherits cmd attributes and methods.

    """
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program\n"""
        return True

    # aliases
    do_EOF = do_quit

    def precmd(self, line):
        """print a new line if the console isn't
        in interactive mode.

        Arguments:
            line -- The remaining arguments

        Returns:
            The default behavior of the cmd.precmd method
        """
        if not sys.stdin.isatty():
            print("")

        # Handles commands given as:
        # case: <class name>.update(<id>, <attribute name>, <attribute value>)
        if '{' and '}' in line:
            line = line.replace('(', '.')
            line = line.replace(')', '')
            line = line.replace(',', '', 1)
            line = line.replace('.', ' ')
            args = line.split(' ', maxsplit=3)
            line = f'{args[1]} {args[0]} {args[2]} {args[3]}'
            return super().precmd(line)

        # case: <class name>.command(<id>)
        if '.' and '(' and ')' in line:
            line = line.replace('(', '.')
            line = line.replace(')', '')
            args = line.split('.')
            if len(args) >= 3:
                if '"' in args[2]:
                    args[2] = args[2].replace('"', '')
                line = f'{args[1]} {args[0]} {args[2]}'

        args = line.split()
        if len(args) >= 4:
            for x in range(2, 4):
                args[x] = args[x].replace('"', '')
                args[x] = args[x].replace(',', '')
            if len(args) > 4:
                line = f'{args[0]} {args[1]} {args[2]} {args[3]} {args[4]}'
            else:
                line = f'{args[0]} {args[1]} {args[2]} {args[3]}'

        # case <class name>.update(<id>, <dictionary representation>)

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

        if not my_model:
            print("** class name missing **")
        elif my_model not in models_dict:
            print("** class doesn't exist **")
        else:
            new_instance = models_dict[my_model]()
            new_instance.save()
            print(new_instance.id)

    def do_show(self, args):
        """Prints the string representation of an instance based on
        the class name and id.
        USAGE: <show> <BaseModel> <id>
        Ex: $ show BaseModel 1234-1234-1234
        """

        args = args.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance_key = "{}.{}".format(args[0], args[1])
            all_instances = storage.all()
            if instance_key not in all_instances:
                print('** no instance found **')
            else:
                print(all_instances[instance_key])

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

        args = args.split(' ', maxsplit=3)
        if args == ['']:
            print("** class name missing **")
        elif args[0] not in models_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print('** attribute name missing **')
        elif len(args) < 4:
            print('** value missing **')
        else:
            if '{' in args[2]:
                args[2] = args[2] + args[3]
                args.pop(3)
                args[2] = args[2].replace("\'", "\"")
                model_name = args[0]
                model_id = args[1].replace('"', "")
                new_attributes_dict = from_json_string(args[2])
                all_instances = storage.all()
                instance_key = f'{model_name}.{model_id}'
                if instance_key not in all_instances:
                    print('** no instance found **')
                    return
                else:
                    instance = all_instances[instance_key].__dict__
                    instance.update(new_attributes_dict)
                    all_instances.update()
                    new = all_instances[instance_key]
                    new.save()
                    return

            instance_key = "{}.{}".format(args[0], args[1])
            all_instances = storage.all()
            if instance_key not in all_instances:
                print('** no instance found **')
            else:
                attribute_name = args[2]
                attribute_value = args[3]
                pattern = r'^"?.+"?$'
                match = re.match(pattern, attribute_value)
                if not match:
                    return
                instance = all_instances[instance_key].__dict__

                attribute_value = attribute_value.replace('"', '')
                instance.update({attribute_name: attribute_value})
                all_instances.update()
                new = all_instances[instance_key]
                new.save()

    def do_destroy(self, args):
        """Deletes an instance based on the class name and id.
        USAGE: <destroy> <BaseModel> <id>
        Ex: $ destroy BaseModel 1234-1234-1234"""

        args = args.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in models_dict:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            instance_key = "{}.{}".format(args[0], args[1])
            all_instances = storage.all()
            if instance_key not in all_instances:
                print('** no instance found **')
            else:
                all_instances.pop(instance_key)
                storage.save()

    def do_count(self, my_model):
        """Retrieve the number of instances of a class
        USAGE:<class name>.count() / count <class name>
        EX: User.count() / count User"""
        number_of_instances = 0
        if not my_model:
            print("** class name missing **")
            return
        elif my_model not in models_dict:
            print("** class doesn't exist **")
            return
        else:
            all_instances_keys = list(storage.all().keys())
            for key in all_instances_keys:
                if my_model in key:
                    number_of_instances += 1
        print(number_of_instances)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
