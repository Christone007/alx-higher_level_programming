#!/usr/bin/python3

def safe_print_integer(value):
    """Safely prints an integer value"""

    try:
        print("{:d}".format(value))
    except Exception:
        return False
    else:
        return True
