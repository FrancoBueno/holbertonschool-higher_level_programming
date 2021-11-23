#!/usr/bin/python3
"""Class Base """

import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ Init constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ Json string"""
        if list_dictionaries == "[]" or list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
