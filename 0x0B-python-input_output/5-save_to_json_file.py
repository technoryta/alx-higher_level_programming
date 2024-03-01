#!/usr/bin/python3
"""Writes Object to a Text File"""
import json


def save_to_json_file(my_obj, filename):
    """Saves to text using JSON"""
    with open(filename, "w") as f:
        json.dump(myobj, f)
