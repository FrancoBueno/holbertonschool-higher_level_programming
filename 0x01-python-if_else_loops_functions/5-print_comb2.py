#!/usr/bin/python3
for number in range(100):
    coma = '\n'
    if (number < 99):
        coma = ", "
    print("{:02d}{}".format(number, coma), end="")
