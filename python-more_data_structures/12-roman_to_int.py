#!/usr/bin/python3

def roman_to_int(roman_string):
    """
    Convert a Roman numeral to an integer (1 to 3999).
    If input is not a string or is None, return 0.
    """
    if not isinstance(roman_string, str):
        return 0
    # Mapping of single Roman numerals to their integer values
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0
    # Process characters from right to left
    for char in reversed(roman_string):
        value = roman_map.get(char, 0)
        if value < prev_value:
            total -= value
        else:
            total += value
            prev_value = value
    return total
