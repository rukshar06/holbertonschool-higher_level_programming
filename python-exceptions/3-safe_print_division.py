#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("inside result: {}".format(result))
    except ZeroDivisionError:
        result = None
        print("inside result: {}".format(result))
    finally:
        return result
