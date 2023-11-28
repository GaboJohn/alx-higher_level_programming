#!/usr/bin/python3

'''Defines a matrix division function.'''


def matrix_divided(matrix, div):
    '''
    Divide all elements of a matrix by a number.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide the matrix elements by.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix doesn't have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    Returns:
        list of lists: A new matrix with elements divided by div, rounded to 2 decimal places.
    '''
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform matrix division and rounding
    result_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return result_matrix
