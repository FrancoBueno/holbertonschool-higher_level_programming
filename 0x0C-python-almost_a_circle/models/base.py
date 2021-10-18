#!/usr/bin/python3
"""Class Base """
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """ Init constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    def to_json_string(list_dictionaries):
            if list_dictionaries == 0 or list_dictionaries == None:
                return ("[]")
            else:
                return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs"""

        if list_objs is None:

