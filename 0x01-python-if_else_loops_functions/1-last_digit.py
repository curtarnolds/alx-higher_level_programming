#!/usr/bin/python3
from ast import If
import random
number = random.randint(-10000, 10000)
end_gtr = "and is greater than 5"
end_eq = "and is 0"
end_less = "and is less than 6 and not 0"
num_str_end = str(number)[-1]
num = int(num_str_end)

if number >= 0:
    if num > 5:
        print(f"Last digit of {number} is {num_str_end} {end_gtr}")
    elif num == 0:
        print(f"Last digit of {number} is {num_str_end} {end_eq}")
    elif (num < 6) and (num != 0):
        print(f"Last digit of {number} is {num_str_end} {end_less}")
elif number == 0:
    print(f"Last digit of {number} is {num_str_end} {end_eq}")
elif number < 0:
    if num != 0:
        print(f"Last digit of {number} is -{num_str_end} {end_less}")
    else:
        print(f"Last digit of {number} is {num_str_end} {end_less}")
try:
    int('a')
except ValueError:
    raise ValueError("String can't be changed into integer")
