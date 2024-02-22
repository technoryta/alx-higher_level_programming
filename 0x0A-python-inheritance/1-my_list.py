#!/usr/bin/python3
"""This module makes a class inherit from list"""


class MyList(list):
    """This class inherits from list"""
    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))

