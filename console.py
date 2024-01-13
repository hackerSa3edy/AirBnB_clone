#!/usr/bin/python3
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
            print("** class doesn't exist **")
        else:
            print(list_instances)

    def do_update(self, args):
        """Updates an instance based on the class name and id.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        Ex: $ update BaseModel 1234-1234-1234 email "airbnb@mail.com"
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
            val = {
                'model': args[0],
                'id': args[1],
                'attribute': args[2],
                'value': args[3]
            }
            updated_obj = storage.all()[f"{val['model']}.{val['id']}"].__dict__
            updated_obj.update({val['attribute']: val['value']})
            new = storage.all()[f"{val['model']}.{val['id']}"]
            new.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
