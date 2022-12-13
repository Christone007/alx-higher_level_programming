#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    to_delete = []
    for i, a in a_dictionary.items():
        if a == value:
            to_delete.append(i)

    for x in to_delete:
        del a_dictionary[x]
    return a_dictionary
