#!/usr/bin/env python3
# Suhail Alaboud - 10675@holbertonstudents.com
"""
Module for CountedIterator class that tracks iteration count.
"""


class CountedIterator:
    """An iterator that counts the number of items iterated."""

    def __init__(self, iterable):
        """Initialize the iterator and counter.

        Args:
            iterable: Any iterable object to iterate over.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Get the next item and increment the counter.

        Returns:
            The next item from the iterator.

        Raises:
            StopIteration: When there are no more items.
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Get the current count of items iterated.

        Returns:
            int: The number of items that have been iterated.
        """
        return self.count

    def __iter__(self):
        """Return the iterator object itself.

        Returns:
            CountedIterator: self
        """
        return self
