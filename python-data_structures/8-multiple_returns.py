#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Return a tuple with the length of a string and its first character.
    If the string is empty, first character is None.
    """
    length = len(sentence)
    first_char = sentence[0] if length > 0 else None
    return (length, first_char)
