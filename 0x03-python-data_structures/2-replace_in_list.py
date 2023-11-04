#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """replaces an element in a list"""
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    else:
        my_list[idx] = element
        return my_list
