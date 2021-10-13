#!/usr/bin/python3
"""9. Student to JSON"""


class Student:
    def __init__(self, first_name, last_name, age):
        """iinit"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """representation"""
        if isinstance(attrs, list) and all(
                [isinstance(x, str) for x in attrs]):
            return{k: v for k, v in self.__dict__.items() if k in attrs}
        return (self.__dict__)

    def reload_from_json(self, json):
        """remplace attributes"""
        for i, f in json.items():
            self.__dict__[i] = f
