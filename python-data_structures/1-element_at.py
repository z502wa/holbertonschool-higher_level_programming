#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Return the element at a specific index in a list.
    If idx is negative or out of range, return None.
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
