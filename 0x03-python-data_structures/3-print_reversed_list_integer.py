#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """Reverses a list and print"""
    if isinstance(my_list, list):
        my_list.reverse()
        for lists in my_list:
            print("{:d}".format(lists))
