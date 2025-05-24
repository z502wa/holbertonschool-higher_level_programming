#!/usr/bin/python3
# Suhail Al-aboud
# 10675@holbertonstudents.com
"""
This module defines a Rectangle class with private width and height.
It tracks instances, allows a custom print symbol,
provides comparison by area, and a class method to create squares.
"""


class Rectangle:
    """
    Represent a rectangle by width and height.
    Track instances, customize print symbol,
    compare rectangles, and create square instances.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle and update instance count.

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
            ValueError: if width must be >= 0.
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
            ValueError: if height must be >= 0.
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
            int: 2*(width + height) or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return the string representation using print_symbol.

        Returns empty string if width or height is 0.
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the rectangle with the greater area.

        Args:
            rect_1 (Rectangle): first rectangle.
            rect_2 (Rectangle): second rectangle.

        Raises:
            TypeError: if rect_1 or rect_2 is not a Rectangle.

        Returns:
            Rectangle: the rectangle with the larger area or rect_1 if equal.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create and return a new Rectangle instance with width == height == size.

        Args:
            size (int): size of each side (default 0).

        Returns:
            Rectangle: new rectangle instance.
        """
        return cls(size, size)
