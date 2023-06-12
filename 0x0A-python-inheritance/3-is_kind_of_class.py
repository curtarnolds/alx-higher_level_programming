#!/usr/bin/python3
"""A simple module to check inheritance."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of or an instance of a class that
    inherited from a_class.

    Args:
        obj (object): An object
        a_class (type): A class
    """
    return isinstance(obj, a_class)
