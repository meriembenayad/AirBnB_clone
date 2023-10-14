#!/usr/bin/python3
""" Command Interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """  """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        return True

    def emptyline(self):
        """ emptyline + ENTER shouldn't execute anything """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
