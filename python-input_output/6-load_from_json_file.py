#!/usr/bin/python3
# 10675@holbertonstudents.com
# Suhail Alaboud
"""
Module: 6-load_from_json_file
Function that creates a Python object from a JSON file.
"""
import json


def load_from_json_file(filename):
    """
    Load a Python object from a JSON file.

    Args:
        filename (str): Path to the JSON file.

    Returns:
        The Python object represented by the JSON content.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
