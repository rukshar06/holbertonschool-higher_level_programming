#!/usr/bin/env python3
"""Module containg basic serialization"""
import json


def serialize_and_save_to_file(data, filename):
    """Save a Python dictionary to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)
    pass


def load_and_deserialize(filename):
    """Load JSON data and convert it into a Python dictionary."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
    pass
