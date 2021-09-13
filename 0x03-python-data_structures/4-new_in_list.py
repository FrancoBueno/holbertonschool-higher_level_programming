#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    listn = list(my_list)
    if idx < 0 or idx >= len(my_list):
        return listn
    else:
        listn[idx] = element
        return listn
