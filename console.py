#!/usr/bin/python3
import cmd
import sys
from models.engine.file_storage import models_dict


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
        if '.' in line:
            command = line.split(".")
            line = f"{command[1]} {command[0]}"
        return super().precmd(line)

    def emptyline(self):
        """an empty line + ENTER does not execute anything"""
        pass

    # task 7 adding (create, show, all, and destroy) commands
    def do_create(self, my_model):
        """Creates a new instance of BaseModel, saves it (to the JSON file)
        and prints the id.
        USAGE: <create> <BaseModel> / <BaseModel>.<create>
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
        # Must be developed
        print('this is show')

    def do_all(self, args):
        # Must be developed
        print('this is all')

    def do_update(self, args):
        # Must be developed
        print('this is update')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
