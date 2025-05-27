#!/usr/bin/python3
"""
Suhail Alaboud
10675@holbertonstudents.com

This module contains a function that checks if an object is an instance
of a class that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False

    Args:
        obj: The object to check
        a_class: The class to check inheritance from

    Returns:
        bool: True if obj inherits from a_class (but is not the same type),
              False otherwise
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
