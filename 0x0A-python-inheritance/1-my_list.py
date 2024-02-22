#!/usr/bin/python3
"""This module makes a class inherit a list"""


class MyList(list):
    """This class inherits a list"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))

