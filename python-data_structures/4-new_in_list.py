#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Return a new list with the element replaced at the specified index.
    If idx is negative or out of range, return a copy of the original list.
    """
    # create a shallow copy of the original list
    new_list = my_list[:]
    # check for invalid index
    if idx < 0 or idx >= len(new_list):
        return new_list
    # replace the element at the given index
    new_list[idx] = element
    return new_list

