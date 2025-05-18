#!/usr/bin/python3
"""
Module 2-matrix_divided.
Provides the matrix_divided function to divide all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div and return a new matrix.

    Args:
        matrix (list of list of int/float): the matrix to divide.
        div (int/float): the divisor.

    Returns:
        list of list of floats: new matrix with each element rounded to 2 decimals.

    Raises:
        TypeError: if matrix is not a list of lists of ints/floats,
                   if rows are not of the same size,
                   or if div is not a number.
        ZeroDivisionError: if div is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if (not isinstance(matrix, list) or
        matrix == [] or
        not all(isinstance(row, list) for row in matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    new_matrix = []

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
