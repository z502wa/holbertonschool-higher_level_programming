#!/usr/bin/python3
# Suhail Al-aboud
# 10675@holbertonstudents.com
"""
This module defines a Rectangle class with private width and height attributes.
It provides methods to compute area and perimeter.
"""


class Rectangle:
    """
    Represent a rectangle defined by width and height.
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle.

        Args:
            width (int): width of the rectangle (default 0).
            height (int): height of the rectangle (default 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.

        Returns:
            int: rectangle width.
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
            int: rectangle height.
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
            int: perimeter (2*(width + height)) or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
