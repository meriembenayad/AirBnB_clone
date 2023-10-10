#!usr/bin/python3
""" Import uuid & datetime modules """
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ Define a BaseModel class """

    def __init__(self):
        """
        Initilize a new instance of BaseModel class
        """
        # assign unique id to the instance
        self.id = str(uuid4())
        # Setting the creation time of the instance to the current time
        self.created_at = datetime.now()
        # Setting the updated time of the instance to the current time
        self.updated_at = datetime.now()

    def __str__(self):
        """
        String representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Method to update the 'updated_at' attribute to the current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Method to return a dictionary representation of the BaseModel instance
        """
        dictionary = {}
        dictionary['__class__'] = self.__class__.__name__
        for key, value in self.__dict__.items():
            dictionary[key] = value
            if key == 'created_at' or key == 'updated_at':
                dictionary[key] = value.isoformat()
        return dictionary
