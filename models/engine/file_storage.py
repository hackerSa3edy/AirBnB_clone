#!/usr/bin/env python
"""File storage class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity

# All models' name and class
models_dict = {
    'BaseModel': BaseModel,
    'User': User,
    'State': State,
    'Review': Review,
    'Place': Place,
    'City': City,
    'Amenity': Amenity
    }


class FileStorage():
    """Serialize instances to a JSON file and deserialize JSON file
        to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """All stored objects

        Returns:
            The dictionary objects
        """
        return self.__objects

    def new(self, obj):
        """Save a new object

        Arguments:
            obj -- The specified object to be saved
        """
        self.__objects.update({f'{obj.__class__.__name__}.{obj.id}': obj})

    def save(self):
        """Save all objects to a file
        """
        obj_to_json = {}
        for key, value in self.all().items():
            obj_to_json[key] = value.to_dict()

        with open(self.__file_path, 'w') as obj_to_json_file:
            json.dump(obj_to_json, obj_to_json_file, indent=3)

    def reload(self):
        """Reload all objects from a file.
        """
        try:
            with open(self.__file_path, 'r') as json_to_obj_file:
                json_objects = json.load(json_to_obj_file)
        except FileNotFoundError:
            return

        # Search for the specified class in models_dict dictionary
        #   with its name, then initialize it.
        for key, value in json_objects.items():
            self.__objects[key] = models_dict[value['__class__']](**value)
