#!/usr/bin/python3
"""
Module 0-add_integer.
This module provides a function to add two integers.
The function casts floats to ints.
It raises TypeError for non-integer inputs.
It returns the integer sum of a and b.
"""

def add_integer(a, b=98):
    """
    Adds two integers.
    Casts floats to ints before addition.
    Raises TypeError for non-integer inputs.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
