#!/usr/bin/env python3
# Suhail Alaboud - 10675@holbertonstudents.com
"""
Module for VerboseList class that extends the built-in list class.
"""


class VerboseList(list):
    """A list that prints notifications when modified."""

    def append(self, item):
        """Add an item to the list and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list with items from iterable and print a notification."""
        size = len(iterable)
        super().extend(iterable)
        print(f"Extended the list with [{size}] items.")

    def remove(self, item):
        """Remove an item from the list and print a notification."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list and print a notification."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
