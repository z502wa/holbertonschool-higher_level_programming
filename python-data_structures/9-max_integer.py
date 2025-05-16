#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Find and return the biggest integer in a list.
    If the list is empty, return None.
    """
    if not my_list:
        return None

    max_val = my_list[0]
    for num in my_list:
        # update max_val if current number is larger
        if num > max_val:
            max_val = num
    return max_val
