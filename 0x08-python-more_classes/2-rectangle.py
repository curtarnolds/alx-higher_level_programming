#!/usr/bin/python3
"""A module to define a class `Rectangle` based on `0-rectangle.py"""


class Rectangle:
    """Define a rectangle"""

    def __init__(self, width: int = 0, height: int = 0):
        """Initialize with optionnal width and height."""
        self.width = width
        self.height = height

    @property
    def width(self) -> int:
        """Return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value: int) -> None:
        """Set the width of Rectangle to `value.

        Args:
            value - the value to set the width.
        Raises:
            ValueError if `value` < 0.
            TypeError if 'value` is not an integer.
        `"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self) -> int:
        """Return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value: int) -> None:
        """Set the height of Rectangle to `value`.

        Args:
            value - the value to set the height.
        Raises:
            ValueError if `value` < 0.
            TypeError if 'value` is not an integer.
        `"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self) -> int:
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self) -> int:
        """Return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))
    