#!/usr/bin/python3
"""A function that returns the dictionary description of with simple
data structue for JSON serialization of an object."""


def class_to_json(obj: object) -> dict:
    """Return the dictionary description of a simple
    JSON serializable data structure.

    Args:
        obj: Python object to be serialized.
    """
    return obj.__dict__
