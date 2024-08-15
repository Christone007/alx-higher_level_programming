#!/usr/bin/python3

def safe_print_division(a, b):
    """Print the quotient of a division"""
    try:
        quotient = a / b
    except ZeroDivisionError:
        quotient = None
    finally:
        print("Inside result: {}".format(quotient))
        return quotient
