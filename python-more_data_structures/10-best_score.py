#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Return the key with the highest integer value in a dictionary.
    If the dictionary is None or empty, return None.
    """
    if not a_dictionary:
        return None
    best = None
    max_val = None
    for key, value in a_dictionary.items():
        if max_val is None or value > max_val:
            max_val = value
            best = key
    return best
