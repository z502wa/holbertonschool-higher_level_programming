#!/usr/bin/python3
# 10675@holbertonstudents.com
# Suhail Alaboud
"""
Module: task_03_xml
Functions to serialize a dictionary to XML and
deserialize an XML file back to a dictionary.
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a dictionary to an XML file.

    Args:
        dictionary (dict): Data to serialize.
        filename (str): Path to the output XML file.
    """
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a dictionary.

    Args:
        filename (str): Path to the input XML file.

    Returns:
        dict: Data reconstructed from XML elements.
    """
    tree = ET.parse(filename)
    root = tree.getroot()
    result = {}
    for child in root:
        result[child.tag] = child.text
    return result
