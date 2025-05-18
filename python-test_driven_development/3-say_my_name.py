#!/usr/bin/python3

"""Defines a name-printing function."""


def say_my_name(first_name, last_name=""):
    """Print a name.

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.
    Raises:
        TypeError: If either of first_name or last_name are not strings.
    """
    # Validate first_name is a string
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    # Validate last_name is a string
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    # Construct and output the greeting message with both names
    print("My name is {} {}".format(first_name, last_name))
