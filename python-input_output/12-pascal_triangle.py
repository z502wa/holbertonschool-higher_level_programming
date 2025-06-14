#!/usr/bin/python3
# 10675@holbertonstudents.com
# Suhail Alaboud
"""
Module: 12-pascal_triangle
Function that returns Pascal's triangle of size n.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle of n rows.

    Args:
        n (int): Number of rows in the triangle.

    Returns:
        list of lists: Pascal's triangle represented as nested lists.
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        row = [1]
        for j in range(1, len(prev)):
            row.append(prev[j-1] + prev[j])
        row.append(1)
        triangle.append(row)

    return triangle
