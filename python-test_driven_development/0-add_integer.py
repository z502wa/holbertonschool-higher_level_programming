#!/usr/bin/python3
"""Module add_integer_3.
This module provides the add_integer function.
It casts floats to ints and raises TypeError on invalid types.
Returns the sum of two integer values.
"""


def add_integer(a, b=98):
    """Add two integers after casting floats to ints.
    Raises TypeError for non-int or non-float inputs.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
