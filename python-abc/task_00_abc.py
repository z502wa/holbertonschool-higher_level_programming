#!/usr/bin/env python3
"""
Suhail Alaboud
10675@holbertonstudents.com

This module contains abstract Animal class and its subclasses Dog and Cat
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class for animals
    """

    @abstractmethod
    def sound(self):
        """
        Abstract method that must be implemented by subclasses
        """
        pass


class Dog(Animal):
    """
    Dog class that inherits from Animal
    """

    def sound(self):
        """
        Returns the sound a dog makes

        Returns:
            str: "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    Cat class that inherits from Animal
    """

    def sound(self):
        """
        Returns the sound a cat makes

        Returns:
            str: "Meow"
        """
        return "Meow"
