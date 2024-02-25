#!/usr/bin/python3
"""Module that checks if object inherits"""


def inherits_from(obj, a_class):
    """Returns true if object is inherits from a class
    otherwise, returns false
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
