#!/bin/usr/python3
def search_replace(my_list, search, replace):
    listup = []
    listup = list(map(lambda a: replace if a is search else a, my_list))
    return listup
