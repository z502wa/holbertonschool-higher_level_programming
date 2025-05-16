#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Delete key in a dictionary if it exists.
    If key doesn't exist, dictionary remains unchanged.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
