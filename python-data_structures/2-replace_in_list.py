#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replace the element at a specific position in a list.
    If idx is negative or out of range, return the original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    # Replace the element at the given index
    my_list[idx] = element
    return my_list
