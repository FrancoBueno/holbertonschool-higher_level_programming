#!/usr/bin/python3
"""
0. Get all states
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    mouse = db.cursor()

    mouse.execute("SELECT * FROM states ORDER BY id ASC")
    row = mouse.fetchall()
    for idx in row:
        print(idx)
    mouse.close()
    db.close()
