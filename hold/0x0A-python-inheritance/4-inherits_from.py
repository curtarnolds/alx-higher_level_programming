#!/usr/bin/python3

"""Defines a function to check direct or indirect class inheritance
"""


def inherits_from(obj, a_class):
    """Checks if obj is an instance of a class that inherited directly or
    indirectly from a_class

    Args:
      obj (any): The object to check
      a_class (type): The class to match obj to

    Returns:
       If obj is an instance of a class that inherited directly or indirectly
    from a_class, return True
       Otherwise, return False
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
