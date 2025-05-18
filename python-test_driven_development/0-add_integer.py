#!/usr/bin/python3
"""
Module add_integer: perform addition of two values.
Casts float inputs to integers before addition.
Raises TypeError for non-numeric inputs.
"""


def add_integer(a, b=98):
    """
    Add two numbers after converting floats to ints.

    Args:
        a (int or float): first operand.
        b (int or float): second operand (default 98).

    Returns:
        int: sum of converted integer values.

    Raises:
        TypeError: if a or b is not int or float.
    """
    if not isinstance(a, (int, float)):  # validate operand a
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):  # validate operand b
        raise TypeError("b must be an integer")
    try:
        return int(a) + int(b)
    except OverflowError:
        raise OverflowError("float overflow")
