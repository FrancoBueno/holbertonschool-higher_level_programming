#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        print("{}".format(value))
        return True
    except Exception as i:
        print("Exception:", e, file=sys.stderr)
        return False
