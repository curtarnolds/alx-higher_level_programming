#!/usr/bin/python3
"""A module to define a class `Rectangle` based on `0-rectangle.py"""


class Rectangle:
    """Define a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width: int = 0, height: int = 0):
        """Initialize with optionnal width and height."""
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1

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

    def __str__(self):
        """Return a string representation of the rectangle.

        Rectangle is printed with the character `#`
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        for i in range(self.__height):
            if i < self.__height - 1:
                print(str(self.print_symbol) * self.__width)
            else:
                print(str(self.print_symbol) * self.__width, end='')
        return ''

    def __repr__(self) -> str:
        """Return a `repr` representation of the rectangle."""
        return f'Rectangle({self.__width}, {self.__height})'

    def __del__(self) -> None:
        """Delete `Rectangle` instance."""
        print('Bye rectangle...')
        __class__.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the biggest rectangle based on area

        Raises:
            TypeError if either `rect_1` or `rect_2` is not a `Rectangle`.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_2 if rect_2.area() > rect_1.area() else rect_1
