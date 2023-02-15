#!/usr/bin/python3

"""Base class to manage `id` attribute.
"""
import json


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
                as a_file:
            list_dict = [item.to_dictionary()
                         for item in list_objs]  # convert each object
            # in the list into a dictionary to avoid JSON serialize error
            a_file.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of JSON string representation"""
        for item in json_string:
            if not json_string or json_string is None:
                return []
            else:
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
        if f'{cls.__name__}.json':
            with open(f'{cls.__name__}.json', mode='r', encoding='utf-8') as f:
                return [cls.create(**item) for item in cls.from_json_string(
                    f.read())]
        else:
            return []
