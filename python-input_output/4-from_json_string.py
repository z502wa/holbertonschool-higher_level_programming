#!/usr/bin/python3
"""
Module: 4-from_json_string
Function that returns the Python object represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Convert a JSON string to a Python data structure.

    Args:
        my_str (str): A string representing a JSON object or array.

    Returns:
        The Python object (dict, list, etc.) represented by the JSON string.
    """
    return json.loads(my_str)
