#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add two tuples and return a new tuple with 2 integers.

    The first element is the sum of the first elements of tuple_a and tuple_b.
    The second element is the sum of the second elements of tuple_a and tuple_b.
    If a tuple has fewer than 2 elements, missing values are treated as 0.
    If a tuple has more than 2 elements, extras are ignored.
    """
    # Get first two values from tuple_a, default to 0
    a0 = tuple_a[0] if len(tuple_a) > 0 else 0
    a1 = tuple_a[1] if len(tuple_a) > 1 else 0
    # Get first two values from tuple_b, default to 0
    b0 = tuple_b[0] if len(tuple_b) > 0 else 0
    b1 = tuple_b[1] if len(tuple_b) > 1 else 0
    # Return the new tuple
    return (a0 + b0, a1 + b1)
