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
    if hasattr(obj, "__dict__"):
        # Set the new attribute using setattr
        setattr(obj, attr_name, attr_val)
    else:
        # Raise a TypeError exception with the message
        raise TypeError("can't add new attribute")
