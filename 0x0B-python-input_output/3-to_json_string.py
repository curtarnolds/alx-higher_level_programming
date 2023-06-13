#!/usr/bin/python3
"""A function to get the JSON representation of an object."""


def to_json_string(my_obj: str) -> str:
    """Return the JSON representation of an object (string).

    Args:
        my_obj (str): A string object
    """
    import json

    return json.dumps(my_obj)
