#!/usr/bin/python3
# 10675@holbertonstudents.com
# Suhail Alaboud
"""
Module: 8-class_to_json
Function that returns the dictionary description with simple data structures
for JSON serialization of an object.
"""

def class_to_json(obj):
    """
    Return the attribute dictionary of an object for JSON serialization.

    Args:
        obj: An instance of a class with serializable attributes.

    Returns:
        dict: Mapping of attribute names to their values.
    """
    return obj.__dict__.copy()
