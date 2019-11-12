#!/usr/bin/python3
"""console contains the entry point of the command interpreter"""


import cmd
import models
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """class HBNB"""
    prompt = '(hbnb) '

    def do_EOF(self, line):
        """End of file"""
        return True

    def emptyline(self):
        """an empty line + ENTER shouldnt execute anything"""
        pass

    def do_quit(self, line):
        """Quit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        options = ["BaseModel"]
        arg = line.split()
        if len(arg) == 0:
            print("** class name missing **")
        if arg[0] in options:
            inst = arg[0]
        else:
            print("** class doesn't exist **")
        print(inst.id)
        inst.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
