#!/usr/bin/python3

import sys

if __name__ == "__main__":
    nargs = len(sys.argv)

    if nargs == 1:
        print("0 arguments.")
    elif nargs == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(nargs - 1))

    for i in range(1, nargs):
        print("{}: {}". format(i, sys.argv[i]))
