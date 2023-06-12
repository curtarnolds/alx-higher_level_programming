#!/usr/bin/python3
"""A simple module to check object instance."""


def is_same_class(obj, a_class):
    """Return True if obj is an exact instance of a_class."""
    return (True if type(obj) == a_class else False)
