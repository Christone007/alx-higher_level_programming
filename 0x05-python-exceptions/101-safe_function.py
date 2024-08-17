#!/usr/bin/python3

import sys


def safe_function(fct, *args):
    """Safely executes a function"""
    try:
        result = fct(*args)
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
    else:
        return result
