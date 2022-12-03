#!/usr/bin/python3
import sys


def myfunc(argument):
    argc = len(argument) - 1
    print("{:d} ".format(argc), end="")
    if argc == 1:
        print("argument", end="")
    else:
        print("arguments", end="")

    if argc == 0:
        print(".")
    else:
        print(":")
        for i in range(1, argc + 1):
            print("{:d}: {:s}".format(i, argument[i]))


if __name__ == "__main__":
    myfunc(sys.argv)
