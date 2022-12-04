#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    count = len(my_string)
    for i in range(count):
        if my_string[i] not in "Cc":
            new_str += my_string[i]
    return new_str
