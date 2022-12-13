#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or len(roman_string) == 0:
        return 0

    roman_dict = {}
    roman_dict['I'] = 1
    roman_dict['V'] = 5
    roman_dict['X'] = 10
    roman_dict['L'] = 50
    roman_dict['C'] = 100
    roman_dict['D'] = 500
    roman_dict['M'] = 1000

    int_value = 0
    pre_sum = 0
    length = len(roman_string)

    for i in range(length):
        if pre_sum == 0 or pre_sum >= roman_dict[roman_string[i]]:
            int_value += pre_sum
            pre_sum = roman_dict[roman_string[i]]
        else:
            pre_sum = roman_dict[roman_string[i]] - pre_sum
            int_value += pre_sum
            pre_sum = 0
    int_value += pre_sum
    return int_value
