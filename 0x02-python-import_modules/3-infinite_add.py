#!/usr/bin/python3
import sys


def myfunc(argument):
    sum = 0
    for i in range(1, len(argument)):
        sum +=int(argument[i])

    print("{:d}".format(sum))
        


if __name__ == "__main__":
    myfunc(sys.argv)
