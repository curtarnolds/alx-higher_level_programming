#!/usr/bin/python3
"""A module to define an add_attribute function.
"""


def add_attribute(obj, attr_name, attr_val):
    """Adds a new attribute to an object.

    Args:
        attr_name (str): Attribute name
        attr_val (str): Attribute value

    Raises:
        TypeError if object can't have new attribute
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("Can't add new attribute")
    setattr(obj, attr_name, attr_val)
