#!/usr/bin/python3
""" Module holds entry point of the command interpreter """
import cmd


class HBNBCommand(cmd.Cmd):
    """
    Defines functionalities for our interpreter
    to create and retrieve an object , to update or destroy an object
    or to do any other operations on an object

    arg: argument passed in the shell """

    prompt = ('(hbnb) ')  # Interpreter Prompt

    def do_quit(self, arg):
        """ quit the interpreter """
        return True

    def help_quit(self):
        """ help for quit command """
        print("Quit command to exit the running interpreter ")

    def do_EOF(self, arg):
        """ Handle ctrl-D to quit the interpreter """
        return True

    def help_EOF(self):
        """ help for EOF command """
        print("Quit command when (Ctrl-D) entered")

    def emptyline(self):
        """
        overriding empty() to return nothing when 'Enter' pressed
        rather than repeting the last command by default
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
