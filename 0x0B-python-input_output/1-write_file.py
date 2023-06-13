#!/usr/bin/python3
"""Defines a function to write to a file."""


def write_file(filename="", text=""):
    """Writes `text` to `filename` and returns the number of characters written

    Args:
        filename (str): The name of the file
        text (str):     The string to be written to file
    """
    with open(filename, mode='w', encoding='utf-8') as txt_file:
        txt_file.write(text)
