#!/usr/bin/python3
# 10675@holbertonstudents.com
# Suhail Alaboud
"""
Module: 5-save_to_json_file
Function that writes a Python object to a text file using its JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a file as JSON.

    Args:
        my_obj: The Python data structure to serialize (e.g., list, dict).
        filename (str): The path to the file where the JSON string will be written.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
