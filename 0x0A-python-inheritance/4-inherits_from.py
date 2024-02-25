#!/usr/bin/python3
"""Module that checks if object inherits"""


def inherits_from(obj, a_class):
    """Returns true if object is inherits a class
    directly or indirectly; otherwise, returns false
    """
    return (isinstance(obj, a_class) and type(obj) != a_class)
