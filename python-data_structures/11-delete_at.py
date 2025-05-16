#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Delete the item at a specific position in a list.
    If idx is negative or out of range, return the original list unchanged.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    # delete the item at the given index
    del my_list[idx]
    return my_list
