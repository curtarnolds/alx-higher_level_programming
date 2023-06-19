#!/usr/bin/pyton3
"""A Square Module.
Depends on the Rectangle module.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize an instance of Square.

        Args:
            size (int): Size of a side
            x (int):	x-offset
            y (int):	y-offset
            id (int):	id of the instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Override the `__str__` method."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - \
{self.width}"

    def get_size(self):
        """Get the size of the Square instance."""
        return self.width

    def set_size(self, value):
        """Set the size of the Square instance."""
        self.width = value
        self.height = value

    size = property(fget=get_size, fset=set_size, fdel=None, doc=None)

    def update(self, *args, **kwargs):
        """Update the Square instance attributes."""
        if not args:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.size = args[1]
        if len(args) > 2:
            self.x = args[2]
        if len(args) > 3:
            self.y = args[3]

    def to_dictionary(self):
        """Return dictionary representation of Square."""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
