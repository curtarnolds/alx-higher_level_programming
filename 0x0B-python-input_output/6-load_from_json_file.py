#!/usr/python3
"""A function that creates an object from a JSON file."""


def load_from_json_file(filename: str) -> object:
    """Create an object from a JSON file

    Args:
        filename: Name of the file to write to.
    """
    import json

    with open(filename) as json_file:
        return json.load(json_file)
