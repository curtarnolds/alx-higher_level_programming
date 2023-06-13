#!/usr/bin/python3
"""A module to define an add_attribute function.
"""


def add_attribute(obj, attr_name, attr_val):
    """Adds a new attribute to an object.

    Args:
        obj (objec): An object
        attr_name (str): Attribute name
        attr_val (str): Attribute value

    Raises:
        TypeError if object can't have new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Can't add new attribute")

    if not isinstance(attr_name, str):
        raise ValueError("Attribute name must be a string")

    setattr(obj, attr_name, attr_val)
