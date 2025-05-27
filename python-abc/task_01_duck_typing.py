#!/usr/bin/env python3
# Suhail Al-aboud - 10675@holbertonstudents.com
"""
Module for shapes, interfaces, and duck typing.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete Circle shape."""

    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        import math

        return math.pi * (self.radius**2)

    def perimeter(self):
        """Calculate the perimeter (circumference) of the circle."""
        import math

        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete Rectangle shape."""

    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of a shape using duck typing."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
