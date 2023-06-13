#!/usr/bin/python3
"""A function that writes a object to a text file using a JSON representation.
"""


def save_to_json_file(my_obj: object, filename: str) -> None:
    """Write `my_obj` to `filename`.

    Args:
        my_obj: A Python object
        filename: Name of the file to write to.
    """
    import json

    with open(filename, mode='w', encoding='utf-8') as json_file:
        json.dump(my_obj, json_file)
