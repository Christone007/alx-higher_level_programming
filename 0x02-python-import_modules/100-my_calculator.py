#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def myfunc(arguments):

    argc = len(arguments) - 1
    operators = "+-*/"

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operator = arguments[2]

    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(arguments[1])
    b = int(arguments[3])

    if operator == "+":
        print("{} {} {} = {}".format(a, operator, b, add(a, b)))
    elif operator == "-":
        print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
    elif operator == "*":
        print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
    elif operator == "/":
        print("{} {} {} = {}".format(a, operator, b, div(a, b)))


if __name__ == "__main__":
    myfunc(sys.argv)
