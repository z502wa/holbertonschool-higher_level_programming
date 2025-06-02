#!/usr/bin/python3
"""
Suhail Alaboud
10675@holbertonstudents.com

Module for reading and printing text files to stdout.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints it to stdout.

    Args:
        filename (str): Path to the file to read. Defaults to empty string.
    """
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()  # Read entire file content
        print(content, end="")  # Print without extra newline
