#!/usr/bin/python3
"""Module that checks if object is a class instance"""


def is_same_class(obj, a_class):
    """Returns true if object is class instance
    otherwise, returns false
    """
    return (type(obj) == a_class)
