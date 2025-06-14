#!/usr/bin/python3
# 10675@holbertonstudents.com
# Suhail Alaboud
"""
Module: 10-student
Defines a Student class with public attributes and
filters JSON serialization based on provided attribute list.
"""


class Student:
    """
    Student class defines a student by first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance.

        Args:
            first_name (str): First name of the student.
            last_name (str): Last name of the student.
            age (int): Age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve dictionary representation of a Student instance.

        If attrs is a list of strings, only include those attributes.
        Otherwise, include all public instance attributes.

        Args:
            attrs (list): Attribute names to filter by (optional).

        Returns:
            dict: Dictionary of attribute names and values.
        """
        obj_dict = self.__dict__.copy()
        if isinstance(attrs, list) and all(isinstance(a, str)
                                          for a in attrs):
            filtered = {}
            for key in attrs:
                if key in obj_dict:
                    filtered[key] = obj_dict[key]
            return filtered
        return obj_dict
