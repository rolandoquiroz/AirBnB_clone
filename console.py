#!/usr/bin/python3
"""console contains the entry point of the command interpreter"""


import cmd

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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
