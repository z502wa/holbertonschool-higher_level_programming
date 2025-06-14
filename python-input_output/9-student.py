#!/usr/bin/python3
# 10675@holbertonstudents.com
# Suhail Alaboud
"""
Module: 9-student
Defines a Student class with public attributes and to_json method.
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

    def to_json(self):
        """
        Retrieve a dictionary representation of a Student instance.

        Returns:
            dict: Dictionary with keys first_name, last_name, and age.
        """
        return self.__dict__.copy()
