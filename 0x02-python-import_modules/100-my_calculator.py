#!/usr/bin/python3
import sys
import calculator_1 as calc

def myfunc():
    nargs = len(sys.argv)
    operators = ['+', '-', '*', '/']
    functions = {"+": calc.add, "-": calc.sub, "*": calc.mul, "/": calc.div}
    
    #confirm proper usage
    if nargs != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    #confirm correct operator
    if sys.argv[2] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    #choose function based on operator
    function = functions[sys.argv[2]]

    #call function
    print("{} {} {} = {}".format(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), function(int(sys.argv[1]), int(sys.argv[3]))))


if __name__ == "__main__":
    myfunc()
