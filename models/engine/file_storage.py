#!/usr/bin/python3

from datetime import datetime
import os
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review

class_names = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
    }


class FileStorage:
    """ this a file that serialize and deserialize object to json file
    and from a json file  """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ Sets in __objects the obj with key <obj class name>.id """
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path) """
        with open(FileStorage.__file_path, "w") as file:
            objects_dict = {}
            for key, value in FileStorage.__objects.items():
                objects_dict[key] = value.to_dict()
            json.dump(objects_dict, file)

    def reload(self):
        """ deserializes the JSON file to __objects """

        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r") as file:
            content = file.read()
            if content is None:
                return
            objects_dict = json.loads(content)
            FileStorage.__objects = {}
            for key, value in objects_dict.items():
                if "User" in key:
                    FileStorage.__objects[key] = User(**objects_dict[key])
                    continue
                elif "State" in key:
                    FileStorage.__objects[key] = State(**objects_dict[key])
                    continue
                elif "City" in key:
                    FileStorage.__objects[key] = City(**objects_dict[key])
                    continue
                elif "Place" in key:
                    FileStorage.__objects[key] = Place(**objects_dict[key])
                    continue
                elif "Amenity" in key:
                    FileStorage.__objects[key] = Amenity(**objects_dict[key])
                    continue
                elif "Review" in key:
                    FileStorage.__objects[key] = Review(**objects_dict[key])
                    continue
                FileStorage.__objects[key] = BaseModel(**objects_dict[key])
