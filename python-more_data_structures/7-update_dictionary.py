#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Replace or add key/value in a dictionary.
    If key exists, update its value; otherwise add new key/value.
    """
    a_dictionary[key] = value
    return a_dictionary
