#!/usr/bin/python3
"""
Module add_integer_3.

Provides a function to add two integers.
Casts floats to ints and raises TypeError for non-integer inputs.
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
