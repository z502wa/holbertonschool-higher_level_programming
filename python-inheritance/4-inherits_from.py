#!/usr/bin/python3
"""
Suhail Alaboud
10675@holbertonstudents.com

This module contains a function that checks if an object is an instance
of a class or an instance of a class that inherited from the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class

    Args:
        obj: The object to check
        a_class: The class to check against

    Returns:
        bool: True if obj is an instance of a_class or inherits from it,
              False otherwise
    """
    return isinstance(obj, a_class)
