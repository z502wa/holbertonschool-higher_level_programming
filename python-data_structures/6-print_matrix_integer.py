#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix of integers.
    Each row prints its values separated by a space.
    """
    for row in matrix:
        # iterate through each number with its index
        for i, num in enumerate(row):
            # print number and decide on trailing space
            if i != len(row) - 1:
                print("{:d}".format(num), end=" ")
            else:
                print("{:d}".format(num), end="")
        # move to next line after each row
        print()
