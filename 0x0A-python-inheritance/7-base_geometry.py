#!/usr/bin/python3
"""Module to hold an empty BaseGeometry class.
"""


class BaseGeometry:
    """An empty BaseGeometry class."""

    def area(self):
        """Raises an exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self,  name, value):
        """Validates `value`.

        Args:
            name (str): A name
            value (int): An int
    """
        if not isinstance(name, str):
            raise TypeError()
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
