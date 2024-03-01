#!/usr/bin/python3
"""Forms Object from JSON"""
import json


def from_json_string(my_str):
    """function returns object from string"""
    return json.loads(my_str)
