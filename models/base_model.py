#!/usr/bin/python3

"""The base class of all our models"""

import uuid
from datetime import datetime


class BaseModel:
    """Defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """The class constructor method for the class instance"""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    self.created_at = datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != '__class__':
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """Public instance method for human readable
        representation of the instance.

        Return: a string"""

        return "[{}] ({}) {}".format(type(
            self).__name__, self.id, self.__dict__)

    def save(self):
        """Public instance method that updates
        the public instance attribute."""

        self.updated_at = datetime.now()

    def to_dict(self):
        """Public instance method that updates and returns
        a dictionary containing all keys/values of __dict__ of the instance.

        Returns: a dictionary."""

        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict


my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))