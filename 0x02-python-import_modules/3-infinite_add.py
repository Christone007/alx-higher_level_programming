#!/usr/bin/python3

import sys

if __name__ == "__main__":
    nargs = len(sys.argv)
    sum = 0

    if nargs > 1:
        for i in range(1, nargs):
            sum = sum + int(sys.argv[i])
    print("{:d}".format(sum))
