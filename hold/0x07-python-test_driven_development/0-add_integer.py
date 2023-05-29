#!/usr/bin/python3

"""A function that performs an addition.

add_integer adds a and b (cast as integers) and returns the result
The function raises a TypeError when a or b are neither integers nor floats
"""


def add_integer(a, b=98):
    """Returns the result of adding two integers.

    b defaults to 98 if no value is passed in.
    a and b are cast to integers if they are floats

    Args:
        a (int): First value to add (must be cast as an integer if a float)
        b (int): Second value to add (must be cast as an integer if a float)

    Returns:
        An integer: the addition of a and b

    Raises:
        TypeError: if a or b are not integers or floats
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
