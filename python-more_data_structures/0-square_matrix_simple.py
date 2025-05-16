#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Compute the square of all integers in a matrix.
    Returns a new matrix without modifying the original.
    """
    # Use list comprehension to build new matrix with squared values
    return [[value ** 2 for value in row] for row in matrix]
