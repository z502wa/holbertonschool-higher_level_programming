#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.
"""

class Square:
    """
    Represent a square by its size.
    """

    def __init__(self, size):
        """
        Initialize a new Square instance with a private size attribute.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
