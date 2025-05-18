#!/usr/bin/python3
"""
Module add_integer: perform addition on two values.
Converts float inputs to integers before summation.
Raises TypeError for invalid input types.
"""

def add_integer(a, b=98):
    """
    Add two numbers after casting floats to ints.

    Args:
        a (int or float): first operand.
        b (int or float): second operand, defaults to 98.

    Returns:
        int: result of int(a) + int(b).

    Raises:
        TypeError: if a or b is not int or float.
        OverflowError: if conversion of floats overflows.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    try:
        return int(a) + int(b)
    except OverflowError:
        raise OverflowError("float overflow")
