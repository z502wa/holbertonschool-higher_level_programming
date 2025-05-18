#!/usr/bin/python3
"""
Module 2-matrix_divided.
Provides the matrix_divided function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns a new matrix.

    Args:
        matrix (list of lists of int/float): matrix to divide.
        div (int/float): divisor.

    Returns:
        list of lists of floats: new matrix with each element=
        round(element/div, 2).

    Raises:
        TypeError: if matrix is not a list of lists of ints/floats,
                   or rows are not of the same size,
                   or div is not a number.
        ZeroDivisionError: if div is zero.
    """
    # validate divisor
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # validate matrix structure and content
    if (not isinstance(matrix, list) or
            matrix == [] or
            not all(isinstance(row, list) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])
    new_matrix = []

    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )
            new_row.append(round(element / div, 2))
        new_matrix.append(new_row)

    return new_matrix
