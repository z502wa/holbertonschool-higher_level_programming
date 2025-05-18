#!/usr/bin/python3
"""
Module 2-matrix_divided: provides matrix_divided function.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a divisor.

    Args:
        matrix (list of lists of int/float): matrix to divide.
        div (int/float): divisor value.

    Returns:
        list of lists of float: new matrix with each element divided and rounded to 2 decimals.

    Raises:
        TypeError: if matrix structure/types are invalid or div is not a number.
        ZeroDivisionError: if div is zero.
    """
    # Validate div is a number
    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    # Check for division by zero
    if div == 0:
        raise ZeroDivisionError('division by zero')
    # Validate matrix is a list of lists
    if not isinstance(matrix, list):
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats'
        )
    # Determine the size of the first row
    row_length = len(matrix[0])

    for tab in matrix:
        # Check each row is a list
        if not isinstance(tab, list):
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats'
            )
        # Check for consistent row size
        if len(tab) != row_length:
            raise TypeError('Each row of the matrix must have the same size')
        for num in tab:
            # Check each element is int or float
            if type(num) is not int and type(num) is not float:
                raise TypeError(
                    'matrix must be a matrix (list of lists) of integers/floats'
                )
    # Perform division and rounding
    return [
        list(map(lambda x: round(x / div, 2), tab))  # divide and round each element
        for tab in matrix
    ]
