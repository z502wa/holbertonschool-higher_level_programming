#!/usr/bin/python3
"""
Module for converting Python objects to JSON strings.

Author: Suhail Alaboud
Email: 10675@holbertonstudents.com
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    Args:
        my_obj: Python object to be converted to JSON string.

    Returns:
        str: JSON string representation of the object.
    """
    return json.dumps(my_obj)
