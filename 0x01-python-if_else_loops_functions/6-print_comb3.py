#!/usr/bin/python3
for ten in range(10):
    for coin in range(ten, 10):
        sepp = "\n"
        if ten < 8:
            sepp = ", "
        if coin != ten:
            print("{}{}{}".format(ten, coin, sepp), end="")
