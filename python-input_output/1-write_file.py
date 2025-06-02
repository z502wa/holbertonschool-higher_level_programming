#!/usr/bin/python3
"""
Module for writing strings to text files.

Author: Suhail Alaboud
Email: 10675@holbertonstudents.com
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns number of characters
    written.
    
    Args:
        filename (str): Path to the file to write. Defaults to empty string.
        text (str): Text content to write to file. Defaults to empty string.
        
    Returns:
        int: Number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        characters_written = file.write(text)  # Write text and get count
        return characters_written  # Return number of characters written
