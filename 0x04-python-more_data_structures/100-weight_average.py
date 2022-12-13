#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    sum_of_values = 0
    number_of_values = 0

    for i in range(len(my_list)):
        current_sum = my_list[i][0] * my_list[i][1]
        sum_of_values += current_sum
        current_freq = my_list[i][1]
        number_of_values += current_freq

    average = sum_of_values / number_of_values
    return average
