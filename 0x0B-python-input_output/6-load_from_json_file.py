#!/usr/bin/python3
"""Module Creates Object from JSON file"""
import json


def load_from_json_file(filename):
    """Creates object"""
    with open(filename) as f:
        return json.load(f)
