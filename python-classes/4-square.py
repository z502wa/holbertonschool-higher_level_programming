#!/usr/bin/python3
"""
Provides the Square class to represent a square by its side length.
"""


class Square:
    """
    Define a square shape and handle its size attribute securely.
    """

    def __init__(self, size=0):
        """
        Set up a Square instance with an initial side length.

        Args:
            size (int): The initial length of each side of the square.
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the current length of the square's side.

        Returns:
            int: The side length of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Update the side length, enforcing type and value constraints.

        Args:
            value (int): The new side length of the square.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than zero.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square based on its side length.

        Returns:
            int: The computed area of the square.
        """
        return self.__size * self.__size
