#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    re = number % 10
else:
    re = ((number * -1) % 10) * -1
reneg = "0"
if re != 0:
    reneg = "less than 6 and not 0"
    if re > 5:
        reneg = "greater than 5"
print("Last digit of {:d} is {:d} and is {}".format(number, re, reneg))
