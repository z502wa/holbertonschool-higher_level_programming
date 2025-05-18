#!/usr/bin/python3

def safe_print_integer(value):
    """
    Prints an integer value using "{:d}" format.
    Returns True if the value was printed successfully (it is an integer),
    otherwise returns False.
    """
    try:
        print("{:d}".format(value))  # attempt to format and print as integer
        return True
    except Exception:
        # value is not an integer or formatting failed
        return False
