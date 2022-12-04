#!/usr/bin/python3
def multiple_returns(sentence):
    count = len(sentence)
    first_char = ""
    if count == 0:
        first_char = None
    else:
        first_char = sentence[0]

    return (count, first_char)
