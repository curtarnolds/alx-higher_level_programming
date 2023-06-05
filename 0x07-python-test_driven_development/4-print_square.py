#!/usr/bin/python3
"""A simple 4-print_square module.

print_square: Prints a square with the character #.
"""


def print_square(size: str) -> None:
    """Print a square with of length size with `#`
    """
    # if isinstance(size, float) and size < 0:
    # raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print(size * '#')
