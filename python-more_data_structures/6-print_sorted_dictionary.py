#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """
    Print a dictionary by ordered keys.
    Only first-level keys are sorted alphabetically.
    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
