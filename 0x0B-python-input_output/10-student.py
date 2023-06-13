#!/usr/bin/python3
"""A Student class."""


class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student instance.

        Args:
            attrs (list): List of attributes to return

        Description:
            If `attrs` is given, only attribuutes in `attrs` are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(item, str)
                                           for item in attrs):
            attr_dict = {}
            for item in attrs:
                if isinstance(item, str) and hasattr(self, item):
                    attr_dict[item] = self.__dict__[item]
            return attr_dict
        return self.__dict__
