#!/usr/bin/python3
"""A simple 5-text_indentation module.

text_indentation: Prints a text with 2 new lines after each of the characters
`.`, `?` and `:`
"""


def text_indentation(text: str) -> None:
    """Print text with 2 new lines at each of the characters `.`, `?` and `:`.

    Arguments:
        text: The text to print
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    iter_text = iter(text)
    list_text = list(iter_text)
    skip_next = False
    next_char = ''

    for i, char in enumerate(list_text):
        if skip_next:
            skip_next = False
            continue

        if char in ('.', '?', ':'):
            if i + 1 < len(list_text):
                next_char = list_text[i + 1]
            print(char, end="")
            print()
            print()
            if next_char == ' ':
                skip_next = True
        else:
            print(char, end='')
