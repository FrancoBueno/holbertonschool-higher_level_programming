#!/usr/bin/python3
def safe_print_division(a, b):
    count = 0
    res = None
    try:
        res = a/b
    except (ValueError,ZeroDivisionError):
        pass
    finally:
            print("Inside result:", res)
            return res

