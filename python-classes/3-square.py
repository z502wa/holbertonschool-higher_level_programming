#!/usr/bin/python3
# 3-square.py
"""
This module defines a Square class with a private size attribute and validation,
and provides a method to compute the area.
"""


class Square:
    """
    Represent a square with a validated private size attribute.
    """

    def __init__(self, size=0):
        """
        Initialize a new Square instance.

        Args:
            size (int): The size of the square (default 0).

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Compute and return the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
