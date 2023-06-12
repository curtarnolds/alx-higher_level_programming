#!/usr/bin/python3
"""A simple module to check single inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that directly or indirectly
    inherited from a_class
    Args:
        obj (object): An object
        a_class (type): A class
    """
    obj_class = type(obj)
    if obj_class is a_class:
        return False

    for base_class in obj_class.__bases__:
        if base_class is a_class or inherits_from(base_class, a_class):
            return True

    return False
