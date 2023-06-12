#!/usr/bin/python3
"""A module that implements a Rectangle class."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A class that inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle

        Raises:
            TypeError if width or height are not integers.
            ValueError if width or height are not greater than 0.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of this Rectangle.

        Returns:
            Area of rectangle instance.
        """
        return self.__width * self.__height

    def __str__(self):
        """Return the string representation of Rectangle."""
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
