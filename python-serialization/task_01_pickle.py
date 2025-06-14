#!/usr/bin/python3
# 10675@holbertonstudents.com
# Suhail Alaboud
"""
Module: task_01_pickle
Provides CustomObject class with pickle-based serialization and deserialization.
"""
import pickle


class CustomObject:
    """
    CustomObject class with attributes name, age, and is_student.
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a CustomObject instance.

        Args:
            name (str): The name of the object.
            age (int): The age of the object.
            is_student (bool): Whether the object represents a student.
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Print the object's attributes in a formatted way.
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the object to a file using pickle.

        Args:
            filename (str): Path to the output file.
        """
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a pickled object from a file.

        Args:
            filename (str): Path to the input file.

        Returns:
            CustomObject or None: Loaded object or None on failure.
        """
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
