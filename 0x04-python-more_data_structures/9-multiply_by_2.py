#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    listnew = []
    listnew = dict(a_dictionary)
    for i in listnew:
        listnew[i] = a_dictionary[i] * 2
    return listnew
