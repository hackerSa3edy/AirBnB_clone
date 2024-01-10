#!/usr/bin/python3
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        """To quit the program."""
        return True

    # aliases
    do_EOF = do_quit

    def precmd(self, line):
        if not sys.stdin.isatty():
            print()
        if '.' in line:
            command = line.split(".")
            line = f"{command[1]} {command[0]}"
        return cmd.Cmd.precmd(self, line)

    def emptyline(self):
        # an empty line + ENTER does not execute anything
        pass


if __name__ == '__main__':
    console = HBNBCommand()

    # Check if the script is running in interactive mode
    if sys.stdin.isatty():
        try:
            console.cmdloop()
        except KeyboardInterrupt:
            print("Exiting due to KeyboardInterrupt.")
    else:
        # Read commands from non-interactive source (e.g., file or pipe)
        for line in sys.stdin:
            console.onecmd(line.strip())
