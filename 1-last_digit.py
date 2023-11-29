#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    number_positive = number * (-1)
else:
    number_positive = number

last_digit = number_positive % 10

str1 = "Last digit of {} is {} "

if last_digit > 5:
    str2 = "and is greater than 5"
elif last_digit == 0:
    str2 = "and is 0"
else:
    str2 = "and is less than 6 and not 0"

print((str1 + str2).format(number, last_digit))
