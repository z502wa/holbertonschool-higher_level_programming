#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of my_list if they are integers (using "{:d}" format).
    Skips non-integer values silently.
    Returns the number of integers printed.
    """
    count = 0
    idx = 0

    while idx < x:
        try:
            value = my_list[idx]
        except:
            # index out of range, re-raise to allow exception for x > list length
            raise
        try:
            print("{:d}".format(value), end="")
            count += 1
        except:
            # skip non-integer values silently
            pass
        idx += 1

    print()
    return count
