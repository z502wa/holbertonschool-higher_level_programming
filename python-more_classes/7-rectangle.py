#!/usr/bin/python3
# Suhail Al-aboud
# 10675@holbertonstudents.com
"""
This module defines a Rectangle class with private width and height.
It tracks instances and allows a custom print symbol.
"""


class Rectangle:
    """
    Represent a rectangle by width and height, track the number of instances,
    and customize the print symbol for string representation.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle instance and update instance count.

        Args:
            width (int): rectangle width (default 0).
            height (int): rectangle height (default 0).
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
        Retrieve the width of the rectangle.

        Returns:
            int: the current width.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width with validation.

        Args:
            value (int): new width.

        Raises:
            TypeError: if width is not an integer.
            ValueError: if width < 0.
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
            int: the current height.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height with validation.

        Args:
            value (int): new height.

        Raises:
            TypeError: if height is not an integer.
            ValueError: if height < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate and return area of the rectangle.

        Returns:
            int: area (width * height).
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate and return perimeter of the rectangle.

        Returns:
            int: 2*(width + height) or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return the string representation using print_symbol.

        Returns:
            str: lines of print_symbol or empty string if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        lines = [symbol * self.__width for _ in range(self.__height)]
        return "\n".join(lines)

    def __repr__(self):
        """
        Return a string to recreate a new instance via eval().

        Format: Rectangle(width, height)
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """
        Print a message on deletion and update instance count.
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
