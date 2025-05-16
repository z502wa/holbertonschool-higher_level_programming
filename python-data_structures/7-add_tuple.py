#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add two tuples, returning a new tuple of two elements.
    The first is the sum of the first elements.
    The second is the sum of the second elements.
    Missing values treated as 0; extras ignored.
    """
    # get first two values from tuple_a (or default to 0)
    a0 = tuple_a[0] if len(tuple_a) > 0 else 0
    a1 = tuple_a[1] if len(tuple_a) > 1 else 0
    # get first two values from tuple_b (or default to 0)
    b0 = tuple_b[0] if len(tuple_b) > 0 else 0
    b1 = tuple_b[1] if len(tuple_b) > 1 else 0
    return (a0 + b0, a1 + b1)
