#!/usr/bin/python3
"""script that adds all arguments to a Python list"""
from sys import *


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    cont = load_from_json_file(filename)
except FileNotFoundError:
    cont = []

save_to_json_file(cont + argv[1:], filename)
