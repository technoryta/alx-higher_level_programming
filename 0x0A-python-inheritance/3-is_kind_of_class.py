#!/usr/bin/python3
"""Module that checks if object is a instance of parent"""


def is_kind_of_class(obj, a_class):
    """Returns true if object is instance of parent class
    otherwise, returns false
    """
    return isinstance(obj, a_class)
