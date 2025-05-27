#!/usr/bin/python3
"""
Suhail Alaboud
10675@holbertonstudents.com

This module contains a function that returns the list of available
attributes and methods of an object
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object
    
    Args:
        obj: Any Python object (int, str, class, etc.)
    
    Returns:
        list: A list containing all available attributes and methods names
    """
    return dir(obj)
