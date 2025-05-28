#!/usr/bin/env python3
# Suhail Alaboud - 10675@holbertonstudents.com
"""
Module demonstrating mixins with Dragon class.
"""


class SwimMixin:
    """Mixin that provides swimming capability."""

    def swim(self):
        """Print swimming behavior."""
        print("The creature swims!")


class FlyMixin:
    """Mixin that provides flying capability."""

    def fly(self):
        """Print flying behavior."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Dragon class that can both swim and fly."""

    def roar(self):
        """Print dragon's roar."""
        print("The dragon roars!")
