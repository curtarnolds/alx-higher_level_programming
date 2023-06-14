#!/usr/bin/python3
"""A function to compute Pascal's triangle"""


def pascal_triangle(n):
    """Return a list of lists of integers representing
    Pascal's triangle of n

    Args:
        n (int): A positive integer

    Returns:
        A list of lists
    """
    if n <= 1:
        return [n]
