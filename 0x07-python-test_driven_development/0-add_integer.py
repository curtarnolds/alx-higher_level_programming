#!/usr/bin/python3
"""A simple add_integer module.
add_integer: Return the sum of two integers or floats
"""


def add_integer(a, b=98):
    """Return the sum of two integers or floats.

    Arguments:
        a: An integer or float.
        b: Another integer or float (default 98).
    """
    if (isinstance(a, int) or isinstance(a, float)) is False:
        raise TypeError('a must be an integer')
    if (isinstance(b, int) or isinstance(b, float)) is False:
        raise TypeError('b must be an integer')

    return (int(a) + int(b))
