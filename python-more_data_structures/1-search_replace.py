#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """
    Return a new list with all occurrences of 'search' replaced by 'replace'.
    """
    # Create a new list replacing matching elements
    new_list = [replace if item == search else item for item in my_list]
    return new_list
