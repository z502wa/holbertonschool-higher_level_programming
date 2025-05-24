#!/usr/bin/python3
# Suhail Al-aboud
# 10675@holbertonstudents.com
"""
This module defines a Rectangle class with private width and height.
It provides methods for:
- area calculation
- perimeter calculation
- string representation
- recreation via eval()
"""


class Rectangle:
    """
    Represent a rectangle defined by its width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle with optional width and height.

        Args:
            width (int): rectangle width (default 0).
            height (int): rectangle height (default 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.

        Returns:
            int: the rectangle width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the rectangle width with validation.

        Args:
            value (int): new width.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Retrieve the height of the rectangle.

        Returns:
            int: the rectangle height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the rectangle height with validation.

        Args:
            value (int): new height.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return the rectangle area.

        Returns:
            int: area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return the rectangle perimeter.

        Returns:
            int: perimeter (2*(width + height)) or 0 if either is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return the string representation using '#'.

        Returns an empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        lines = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """
        Return an official string to recreate a new instance via eval().

        Example: Rectangle(width, height)
        """
        return f"Rectangle({self.__width}, {self.__height})"
