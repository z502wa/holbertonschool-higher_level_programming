#!/usr/bin/env python3
"""
Suhail Alaboud
10675@holbertonstudents.com

This module demonstrates duck typing with abstract Shape class and its implementations
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for shapes
    """

    @abstractmethod
    def area(self):
        """
        Abstract method to calculate area
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Abstract method to calculate perimeter
        """
        pass


class Circle(Shape):
    """
    Circle class that inherits from Shape
    """

    def __init__(self, radius):
        """
        Initialize Circle with radius

        Args:
            radius: The radius of the circle
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle

        Returns:
            float: Area of the circle
        """
        return math.pi * self.radius**2

    def perimeter(self):
        """
        Calculate the perimeter of the circle

        Returns:
            float: Perimeter of the circle
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle class that inherits from Shape
    """

    def __init__(self, width, height):
        """
        Initialize Rectangle with width and height

        Args:
            width: The width of the rectangle
            height: The height of the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle

        Returns:
            int/float: Area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle

        Returns:
            int/float: Perimeter of the rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print area and perimeter of a shape using duck typing

    Args:
        shape: Any object with area() and perimeter() methods
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
