#!/usr/bin/python3
"""
Suhail Alaboud
10675@holbertonstudents.com

This module contains Square class that inherits from Rectangle
"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size):
        """
        Initializes Square with size

        Args:
            size: size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns string representation of the square

        Returns:
            str: String in format [Square] <width>/<height>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
