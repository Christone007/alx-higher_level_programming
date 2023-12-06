#!/usr/bin/python3


def roman_to_int(roman_string):
    """Convert roman numeral to integer"""

    if roman_string is None or type(roman_string) is not str:
        return 0

    base_numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}

    numeral_length = len(roman_string)

    arabic_number = 0
    counter = 0

    while counter < numeral_length:
        temp1 = base_numerals[roman_string[counter]]
        temp2 = 0

        if (counter + 1) < numeral_length:
            temp2 = base_numerals[roman_string[counter + 1]]

        if temp1 >= temp2:
            arabic_number += temp1
            counter += 1
        else:
            arabic_number += (temp2 - temp1)
            counter += 2

    return arabic_number
