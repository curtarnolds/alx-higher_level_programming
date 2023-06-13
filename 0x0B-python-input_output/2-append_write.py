#!/usr/bin/python3
"""A function to append at the end of a file."""


def append_write(filename="", text=""):
    """Append `text` at the end of `filename`.

    Args:
        filename (str): Name/path to file to edit
        text (str):     The text to append to file
    """
    with open(filename, mode='a', encoding='utf-8') as txt_file:
        char_count = txt_file.write(text)
    return char_count
