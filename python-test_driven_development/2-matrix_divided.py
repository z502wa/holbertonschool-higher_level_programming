#!/usr/bin/python3
# 2-matrix_divided.py
# Brennan D Baraban <375@holbertonschool.com>
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by a divisor."""
    # Validate that matrix is non-empty list of lists of numbers
    if (not isinstance(matrix, list) or matrix == [] or
            not all(isinstance(row, list) for row in matrix) or
            not all(isinstance(ele, (int, float))
                    for row in matrix for ele in row)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Ensure all rows have the same length
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check that divisor is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Prevent division by zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Compute and return the new matrix with rounded division results
    return [
        [round(ele / div, 2) for ele in row]
        for row in matrix
    ]
