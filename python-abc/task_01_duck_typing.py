#!/usr/bin/env python3
# Suhail Al-aboud - 10675@holbertonstudents.com
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """
    Abstract base class representing a geometric shape.
    """
    @abstractmethod
    def area(self):
        """
        Calculate and return the area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Calculate and return the perimeter of the shape.
        """
        pass

class Circle(Shape):
    """
    Class representing a circle, inheriting from Shape.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculate and return the area of the circle.
        """
        return abs(math.pi * self.radius ** 2)

    def perimeter(self):
        """
        Calculate and return the perimeter of the circle.
        """
        return abs(2 * math.pi * self.radius)

class Rectangle(Shape):
    """
    Class representing a rectangle, inheriting from Shape.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate and return the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Print the area and the perimeter of a given shape.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
