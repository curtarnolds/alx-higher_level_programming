#!/usr/bin/python3

"""Class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """A rectangle class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize an instance of Rectangle.
         This Rectangle class inherits its id from the Base super class
         """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        """Set width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Compute the area of Rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """Print to stdout the Rectangle instance with character #"""
        for yposition in range(self.y):
            print('')
        for height in range(self.__height):
            for xposition in range(self.x):
                print(' ', end='')
            for width in range(self.__width):
                print("#", end='')
            print()

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute.

        Args:
            *args: variable length argument to be attached to id, width,
                height, x and y
        """
        if len(args) >= 5:
            self.y = args[4]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 1:
            self.id = args[0]
        if not args:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """__str__ method"""
        return f'[{self.__class__.__name__}] ({self.id}) {self.x}/\
{self.y} - {self.width}/{self.height}'
