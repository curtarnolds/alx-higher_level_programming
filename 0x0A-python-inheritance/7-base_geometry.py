#!/usr/bin/python3

"""Defines a base geometry class BaseGeometry.
"""


class BaseGeometry:
    """Represent BaseGeometry.
    """
    def area(self):
        """Raise an Exception message

        Raise:
           An Exception with message `area() is not implemented`
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value.

        Args:
           name (str): A string
           value (int): An integer value

        Raise:
           TypeError: Raise Exception with message `<name> must be an integer`
           ValueError: Raise Exception with message
`<name> must be greater than 0`
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
