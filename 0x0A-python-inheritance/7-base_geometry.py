#!/usr/bin/python3
"""This module makes a base geometry"""


class BaseGeometry():
    """Base geometry class"""

    def area(self):
        """has not been implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """checks if value is int"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
