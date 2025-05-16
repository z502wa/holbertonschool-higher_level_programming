#!/usr/bin/python3

def no_c(my_string):
    """
    Remove all characters 'c' and 'C' from a string.
    """
    new_str = ''
    for char in my_string:
        # skip lowercase 'c' and uppercase 'C'
        if char == 'c' or char == 'C':
            continue
        new_str += char
    return new_str
