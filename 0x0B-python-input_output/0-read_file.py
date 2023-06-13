#!/usr/bin/python3
"""A simple file reading function.
"""


def read_file(filename=""):
    """Read a text file.

    Args:
        filename (str): Name of file.
    """
    if isinstance(filename, str):
        with open(filename, mode='r', encoding='utf-8') as txt_file:
            print(txt_file.read(), end="")
