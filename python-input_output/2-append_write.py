#!/usr/bin/python3
"""
Module for appending strings to text files.

Author: Suhail Alaboud
Email: 10675@holbertonstudents.com
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8) and returns number
    of characters added.
    
    Args:
        filename (str): Path to the file to append to. Defaults to empty
                       string.
        text (str): Text content to append to file. Defaults to empty string.
        
    Returns:
        int: Number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        characters_added = file.write(text)  # Append text and get count
        return characters_added  # Return number of characters added
