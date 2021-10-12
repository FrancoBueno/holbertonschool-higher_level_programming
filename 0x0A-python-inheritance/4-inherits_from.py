#!/usr/bin/python3
""" functiont that verifi si es una subclasse"""
def inherits_from(obj, a_class):
    """functiont that verify is subclass"""
    if a_class is bool:
        return()
    else:
        return issubclass(type(obj), a_class)
