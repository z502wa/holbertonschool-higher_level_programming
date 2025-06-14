#!/usr/bin/python3
# 10675@holbertonstudents.com
# Suhail Alaboud
"""
Module: task_02_csv
Function to convert CSV data to JSON file data.json.
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Read a CSV file and serialize its rows to data.json.

    Args:
        csv_filename (str): Path to the input CSV file.

    Returns:
        bool: True on success, False on failure.
    """
    try:
        with open(csv_filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]
        with open('data.json', 'w', encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile)
        return True
    except Exception:
        return False
