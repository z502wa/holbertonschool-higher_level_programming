#!/usr/bin/python3
# 10675@holbertonstudents.com
# Suhail Alaboud
"""
Module: task_00_basic_serialization
Provides basic serialization and deserialization to JSON.
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save to a file.

    Args:
        data (dict): Python dictionary to serialize.
        filename (str): Path to the output JSON file.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize to a Python dictionary.

    Args:
        filename (str): Path to the JSON file.

    Returns:
        dict: Deserialized Python dictionary from the file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
