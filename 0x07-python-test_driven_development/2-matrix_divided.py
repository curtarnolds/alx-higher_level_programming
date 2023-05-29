"""This module contains the matrix_divided function

matrix_divided(matrix, div) divides all elements of the matrix `matrix` by
`div`. `matrix` has to be a list of lists of integers or floats otherwise raise
a TypeError
"""


def matrix_divided(matrix, div):
    """Divides each element of `matrix` by `div`.

    matrix must be a list of lists of integers or floats.
    Each row of `matrix` must be of the same size
    div must be an integer or a float
	 div cannot be equal to 0

	 Args:
	   matrix (list): A list of lists of integers or floats. Each row of matrix
		  must be of the same length
		div (int/float): Either a float or integer greater than 0

	 Raises:
	   TypeError:
			If matrix is not a list of lists of numbers, the rows of
			matrix are not the same size or div is not a number
	 	ZeroDivisionError:
			if div is equal to 0

	 Returns:
		A new matrix
    """
    if not all(isinstance(ele, list) for ele in matrix) or\
       (not all(isinstance(mem, int) for mem in ele for ele in matrix) and\
        not all(isinstance(mem, float) for mem in ele for ele in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
    elif not (len(row) == matrix[1] for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    elif not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    return list(lambda x: x/div for x in elm for elm in matrix)
