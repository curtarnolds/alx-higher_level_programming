#!/usr/bin/python3
"""A simple 2-matrix_divided module.
matrix_divided: Divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """Divide matrix by div and return a matrix.

    Arguments:
        matrix (list): A list of lists of integers.
        div (int/float): An int or float.
    """
    if ((isinstance(matrix, list) and
            all(isinstance(item, list) for item in matrix)) and
            (all(isinstance(num, int) for item in matrix for num in item) or
             all(isinstance(num, int) for item in matrix for num in item)))\
            is False:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')

    if len(matrix) == 0:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')

    if (isinstance(div, int) or isinstance(div, float)) is False:
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    if all(len(item) == len(matrix[0]) for item in matrix) is False:
        raise TypeError("Each row of the matrix must have the same size")

    return list(list(map(lambda num: round(num/div, 2), item))
                for item in matrix)
