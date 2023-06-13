#!/usr/bin/python3
"""A function to deserialize a JSON string to object."""


def from_json_string(my_str: str) -> object:
    """Return a python data structure represented by a JSON string.

    Args:
        my_str (str): A JSON string

    Returns:
        A Python object.
    """
    import json

    return json.loads(my_str)
