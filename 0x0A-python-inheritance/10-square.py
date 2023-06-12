#!/usr/bin/python3
"""A module to hold a Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize a Square instance with side  `size`.

        Args:
            size (int): The size of each side of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
