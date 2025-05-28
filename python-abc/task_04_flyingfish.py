#!/usr/bin/env python3
# Suhail Alaboud - 10675@holbertonstudents.com
"""
Module demonstrating multiple inheritance with FlyingFish class.
"""


class Fish:
    """Fish class with swimming and habitat methods."""

    def swim(self):
        """Print swimming behavior of fish."""
        print("The fish is swimming")

    def habitat(self):
        """Print habitat of fish."""
        print("The fish lives in water")


class Bird:
    """Bird class with flying and habitat methods."""

    def fly(self):
        """Print flying behavior of bird."""
        print("The bird is flying")

    def habitat(self):
        """Print habitat of bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """FlyingFish class inheriting from both Fish and Bird."""

    def fly(self):
        """Print flying behavior of flying fish."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print swimming behavior of flying fish."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print habitat of flying fish."""
        print("The flying fish lives both in water and the sky!")
