#!/usr/bin/python3
FIZZ = "Fizz"
BUZZ = "Buzz"


def fizzbuzz():
    for number in range(1, 101):
        if (number % 3 == 0):
            print("%s" % (FIZZ), end=' ')
        elif (number % 5 == 0):
            print("%s" % (BUZZ), end=' ')
        else:
            print("%d" % (number), end=' ')
