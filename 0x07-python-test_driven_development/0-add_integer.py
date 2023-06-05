#!/usr/bin/python3

"""
Adds two integers.

Args:
   a (int): First integer
   b (int): Second integer

Returns:
   The addition of a and b
"""


def add_integer(a, b=98):
    """
    Function add_integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    elif not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
