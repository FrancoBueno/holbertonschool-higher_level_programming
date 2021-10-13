#!/usr/bin/python3
"""Objct string to Json String"""
import json


def from_json_string(my_str):
    """return an object represented by a Json String"""
    return json.loads(my_str)
