#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a_length = len(tuple_a)
    b_length = len(tuple_b)

    if a_length < 1:
        tuple_a = (0, 0)
    elif a_length < 2:
        tuple_a = tuple_a + (0,)

    if b_length < 1:
        tuple_b = (0, 0)
    elif b_length < 2:
        tuple_b = tuple_b + (0,)

    first_tuple = tuple_a[0] + tuple_b[0]
    second_tuple = tuple_a[1] + tuple_b[1]

    new_tuple = first_tuple, second_tuple
    return new_tuple
