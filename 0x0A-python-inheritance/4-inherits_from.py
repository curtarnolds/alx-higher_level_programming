#!/usr/bin/python3
"""A simple module to check single inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that directly or indirectly
    inherited from a_class
    Args:
        obj (object): An object
        a_class (type): A class
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
