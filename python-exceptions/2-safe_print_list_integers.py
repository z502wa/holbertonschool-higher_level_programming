#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of my_list if they are integers (using "{:d}" format).
    Skips non-integer values silently.
    Returns the number of integers printed.
    """
    count = 0  # number of integers printed
    idx = 0    # current index in list

    while idx < x:
        try:
            # try to format and print the element as integer
            print("{:d}".format(my_list[idx]), end="")
            count += 1
        except (TypeError, ValueError):
            # skip non-integer values silently
            pass
        # do not catch IndexError: let it propagate if idx >= len(my_list)
        idx += 1

    print()  # newline after printing all valid integers
    return count
