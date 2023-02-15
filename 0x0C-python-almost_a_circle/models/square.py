#!/usr/bin/python3

"""Class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square class.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize an instance of square

        Args:
          size: The length of any side of the square
           x, y: Offsets to the x and y direction
        """
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """Return the size of the Square instance
        """
        return self.width

    @size.setter
    def size(self, size):
        """Set the width and height of the Square instance to size.
        Args:
            size (int): The size of a side of the square.
        """
        if not isinstance(size, int):
            raise TypeError("width must be an integer")
        if size < 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """Assign attributes.

        Args:
            args (tuple):
                * First argument is id attribute
                * Second argument is size attribute
                * Third argument is x attribute
                * Fourth argument is y attribute
            kwargs (dict):
                * keyworded arguments. Must be skipped if *args is not empty
        """
        if len(args) >= 4:
            self.y = args[3]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 1:
            self.id = args[0]
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Square"""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """__str__ method"""
        return f'[{self.__class__.__name__}] ({self.id}) <{self.x}>/<{self.y}>\
 - <{self.height}>'
