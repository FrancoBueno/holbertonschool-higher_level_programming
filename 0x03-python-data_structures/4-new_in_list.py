#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new = list(my_list)
    if idx < 0 and idx >= len(my_list):
        return my_list
    else:
        new[idx] = element
        return new
