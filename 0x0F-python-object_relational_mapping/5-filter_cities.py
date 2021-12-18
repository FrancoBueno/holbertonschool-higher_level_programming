#!/usr/bin/python3
"""
0. Get all states
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    argumento = argv[4]
    mouse = db.cursor()
    mouse.execute("SELECT cities.name FROM cities INNER JOIN states \
                  ON cities.state_id = states.id WHERE \
                  states.name = %s ORDER BY cities.id ASC",
                  (argumento,))
    parr = mouse.fetchall()
    print(", ".join(idx[0] for idx in parr))
    mouse.close()
    db.close()
