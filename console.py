#!/usr/bin/python3
""" Module holds entry point of the command interpreter or console program """
import cmd
from models.base_model import BaseModel
import models
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity


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

    def do_create(self, arg):
        """
        create a new instance , save it to json and print its id
        """
        classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'City': City, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}

        if len(arg) == 0:
            print('** class name missing **')
            return
        args = arg.split()
        if args[0] not in classes:
            print('** class doesn\'t exist **')
            return

        # create an instance
        instance = classes[args[0]]()

        # instance saved to json
        instance.save()

        # print instance id
        print(instance.id)

    def do_show(self, arg):
        """
        prints the string representation of an instance
        based on the class name
        """

        classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'City': City, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}

        if len(arg) == 0:
            print('** class name missing **')
            return

        args = arg.split()

        if args[0] not in classes:
            print('** class doesn\'t exist **')
            return

        if len(args) == 1:
            print('** instance id missing **')
            return

        # dict storing all objects based on class name and id
        obj_dic = models.storage.all()

        key = args[0] + '.' + args[1]

        if key in obj_dic:
            print(obj_dic[key])
            return

        print('** no instance found **')

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name
        and id , save the change into JSON file
        """

        classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'City': City, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}

        if len(arg) == 0:
            print('** class name missing **')
            return

        args = arg.split()

        if args[0] not in classes:
            print('** class doesn\'t exist **')
            return

        if len(args) == 1:
            print('** instance id missing **')
            return

        # dict storing all objects based on class name and id
        obj_dic = models.storage.all()
        # key
        key = args[0] + '.' + args[1]

        if key in obj_dic:
            del obj_dic[key]
            models.storage.save()
            return
        print('** no instance found **')

    def do_all(self, arg):
        """
        prints all string representation of all instances based or not
        on the class name
        """

        classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'City': City, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}

        instance_list = []  # to store string representation in a list
        obj_dic = models.storage.all()

        if len(arg) > 0:
            args = arg.split()
            if args[0] != 'BaseModel':  # if class name exist with the command
                print('** class doesn\'t exist **')
                return

        for instance in obj_dic.values():  # appending instance to the list
            instance_list.append(str(instance))

        print(instance_list)

    def do_update(self, arg):
        """
        updates an instance based on the class name and id
        by adding or updating attribute and save changes to
        JSON File.
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        classes = {'BaseModel': BaseModel, 'User': User, 'State': State,
                   'City': City, 'Amenity': Amenity, 'Place': Place,
                   'Review': Review}

        if len(arg) == 0:  # if class name is missing
            print('** class name is missing **')
            return

        args = arg.split()

        if args[0] not in classes:  # if class name doesn't exist
            print('** class doesn\'t exist **')
            return

        if len(args) < 2:  # if id is missing
            print('** instance id missing **')
            return

        obj_dic = models.storage.all()
        key = args[0] + '.' + args[1]   # key constructing

        # checking if an instance is found with given id

        if key not in obj_dic:
            print('** no instance found **')
            return

        if len(args) == 2:  # attribute name is missing
            print('** attribute name missing *')
            return

        if len(args) == 3:  # attribute value is missing
            print('** value missing **')
            return

        # updating an exsisting attribute value

        if args[2] in obj_dic[key].__dict__:
            obj = getattr(obj_dic[key], args[2])  # getting the attribute value
            attr_type = type(obj)  # determining the attribute type

            if not isinstance(attr_type, args[3]):
                # casting the new value to the existing attribute type
                value = attr_type(args[3])
            setattr(obj_dic[key], args[2], value)
            # setting a new value for the attribute
            models.storage.save()
            return

        # adding a new attribute
        args[3] = args[3].replace('"', "")
        setattr(obj_dic[key], args[2], args[3])
        models.storage.save()  # saving changes to JSON File


if __name__ == '__main__':
    HBNBCommand().cmdloop()
