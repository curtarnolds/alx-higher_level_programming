#!/usr/bin/python3

"""Base class to manage `id` attribute.
"""
import json
import csv
import turtle


class Base():
    """Base class.
    """
    _nb_objects = 0
    id = 0

    def __init__(self, id=None):
        """Initialize by creating public attribute id"""
        if id:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries

        Args:
           list_dictionaries (list): List of dictiionaries.
        """
        if not list_dictionaries or list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of list_objs to a file

        Args:
            list_objs (list): list of instances who inherit Base
        """
        with open(f'{cls.__name__}.json', mode='w', encoding='utf-8')\
                as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                list_dict = [item.to_dictionary()
                             for item in list_objs]  # convert each object
                # in the list into a dictionary to avoid JSON serialize error
                json_file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of JSON string representation"""
        if json_string is None:
            return []
        else:
            for item in json_string:
                return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        # Differentiate between dummy Rectangle and Square
        # This creates a dummy instance of the class used to
        # call `create`
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(width=1, height=1, x=0, y=0,
                                 id=None)
        else:
            dummy_instance = cls(size=1, x=0, y=0,
                                 id=None)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances that depend on the current class using
        this method."""
        try:
            with open(f'{cls.__name__}.json', mode='r', encoding='utf-8') as f:
                return [cls.create(**item) for item in cls.from_json_string(
                    f.read())]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

            Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Return a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
