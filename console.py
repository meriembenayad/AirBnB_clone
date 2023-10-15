#!/usr/bin/python3
""" Command Interpreter """
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """  """
    prompt = '(hbnb) '

    __classes = {
        "BaseModel": BaseModel,
    }

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def do_EOF(self, arg):
        """ EOF command to exit the program """
        return True

    def emptyline(self):
        """ An empty line + ENTER shouldn't execute anything """
        pass

    def do_create(self, arg):
        """
            Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id
            Usage: create <class name>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            my_model = HBNBCommand.__classes[args[0]]()
            my_model.save()
            print(my_model.id)

    def do_show(self, arg):
        """
             Prints the string representation of an instance based on the class name and id.
             Ex: $ show BaseModel 1234-1234-1234.
             Usage: show <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
            Deletes an instance based on the class name and id
            (save the change into the JSON file).
            Usage: destroy <class name> <id>
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
            Prints all string representation of all instances
            based or not on the class name.
            Usage: all [class name]
        """
        args = arg.split()
        objects = storage.all()
        if not args:
            result = []
            for obj in objects.values():
                result.append(str(obj))
            print(result)
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            class_name = args[0]
            if class_name in HBNBCommand.__classes:
                class_objs = []
                for key, obj in objects.items():
                    if key.startswith(class_name + "."):
                        class_objs.append(str(obj))
                print(class_objs)
            else:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """
            Updates an instance based on the class name and id,
            by adding or updating attribute (save the change into the JSON file).
            Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        objects = storage.all()
        args = arg.split()
        if not args:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            find_key = args[0] + '.' + args[1]
            obj = objects.get(find_key)
            if obj is None:
                print("** no instance found **")

            setattr(obj, args[2], args[3].lstrip('"').rstrip('"'))
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
