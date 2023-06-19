#!/usr/bin/python3
"""A Rectangle module."""
from models.base import Base


class Rectangle(Base):
    """A Rectangle class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance.

        Args:
            width:
            height:
            x:
            y:
            id:
        """
        args = {"width": width, "height": height, "x": x, "y": y}
        for arg_name, arg_value in args.items():
            if type(arg_value) is not int:
                raise TypeError(f"{arg_name} must be an integer")

            if arg_name in ("width", "height") and arg_value <= 0:
                raise ValueError(f"{arg_name} must be > 0")

            if arg_name in ("x", "y") and arg_value < 0:
                raise ValueError(f"{arg_name} must be >= 0")
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def set_width(self, value):
        """Set the width of the rectangle instance.

        Args:
            value: An integer given as the width.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    def get_width(self):
        """Get the width of the rectangle instance."""
        return self.__width

    def set_height(self, value):
        """Set the height of the rectangle instance.

        Args:
            value: An integer given as the height.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    def get_height(self):
        """Get the height of the rectangle instance."""
        return self.__height

    def set_x(self, value):
        """Set the x-coordinate of the rectangle instance.

        Args:
            value: An integer given as the x-coordinate.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def get_x(self):
        """Get the x-offset of the rectangle instance."""
        return self.__x

    def set_y(self, value):
        """Set the y-coordinate of the rectangle instance.

        Args:
            value: An integer given as the y-coordinate.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def get_y(self):
        """Get the y-offset of the rectangle instance."""
        return self.__y

    def area(self):
        """Return the area of the Rectangle instance."""
        return self.__width * self.__height

    def display(self):
        """Print the Rectangle instance with the character `#`."""
        for y_pos in range(self.__y):
            print()
        for char in range(self.__height):
            for x_pos in range(self.__x):
                print(end=" ")
            for char in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """Override the `__str__` method."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__x}/\
{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """Update Rectangle instance with argument to each attribute.

        Args:
            args (int): Variable arguments.
            kwargs (int): Key-word arguments.
        """
        if not args:
            for key, value in kwargs.items():
                self.__setattr__(key, value)

        if len(args) > 0:
            self.id = args[0]
        if len(args) > 1:
            self.__width = args[1]
        if len(args) > 2:
            self.__height = args[2]
        if len(args) > 3:
            self.__x = args[3]
        if len(args) > 4:
            self.__y = args[4]

    def to_dictionary(self):
        """Return a dictionary representation of Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    width = property(fget=get_width, fset=set_width, fdel=None, doc=None)
    height = property(fget=get_height, fset=set_height, fdel=None, doc=None)
    x = property(fget=get_x, fset=set_x, fdel=None, doc=None)
    y = property(fget=get_y, fset=set_y, fdel=None, doc=None)
