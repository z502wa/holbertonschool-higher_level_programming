#!/usr/bin/python3

def uniq_add(my_list=[]):
    """
    Add all unique integers in a list and return the sum.
    """
    # Use a set to eliminate duplicates, then sum
    return sum(set(my_list))
