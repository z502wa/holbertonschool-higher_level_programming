#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number and returns a new matrix.

    Args:
        matrix: A list of lists containing integers or floats.
        div: The number to divide all elements of the matrix by.

    Returns:
        A new matrix with all elements divided by div and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                  or if each row of the matrix doesn't have the same size,
                  or if div is not a number.
        ZeroDivisionError: If div is equal to 0.
    """
    # Check if matrix is a list of lists of integers/floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all elements are integers or floats
    for row in matrix:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if all rows have the same size
    if len(matrix) > 0:
        row_size = len(matrix[0])
        if not all(len(row) == row_size for row in matrix):
            raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Divide each element by div and round to 2 decimal places
    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]
    
    return new_matrix
