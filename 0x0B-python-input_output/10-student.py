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
        if attrs and len(attrs) > 0 and isinstance(attrs, list):
            attr_dict = {}
            for item in attrs:
                if hasattr(self, item) and isinstance(item, str):
                    attr_dict[item] = self.__dict__[item]
            return attr_dict
        return self.__dict__
