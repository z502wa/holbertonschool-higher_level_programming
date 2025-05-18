#!/usr/bin/python3

def safe_print_division(a, b):
    """
    Divides two integers and prints the result.
    Uses try/except/finally to handle division by zero.
    Prints the result in the finally block preceded by 'Inside result:'.
    Returns the division result or None on failure.
    """
    try:
        result = a / b  # perform division
    except ZeroDivisionError:
        result = None  # handle division by zero
    finally:
        # always execute: print the result or None
        print("Inside result: {}".format(result))
    return result  # return the result or None
