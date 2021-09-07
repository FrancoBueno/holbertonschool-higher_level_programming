#!/usr/bin/python3
for charac in range(97, 123):
    if chr(charac) not in "qe":
        print("{}".format(chr(charac)), end='')
