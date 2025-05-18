#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of my_list on the same line if they are integers.
    Skips non-integer values silently.
    Returns the number of integers printed.
    """
    count = 0
    idx = 0
    while idx < x:
        try:
            print("{:d}".format(my_list[idx]), end="")
            count += 1
        except (TypeError, ValueError):
            pass
        idx += 1
    print()
    return count
