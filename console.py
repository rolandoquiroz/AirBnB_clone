#!/usr/bin/python3
"""console contains the entry point of the command interpreter"""


import cmd

    options = [


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

    def to_create(self, line):
        """Creates a new instance of BaseModel"""
        if line[0] == 0:
            print("** class name missing **")
        if line[0] is not in options:
            print("** class doesn't exist **)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
