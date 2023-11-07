#!/usr/bin/python3

def max_integer(my_list=[]):
    """Find max of integer"""
    if len(my_list) == 0:
        return None
    else:
        maximum = my_list[0]
        for x in my_list:
            maximum = x if x > maximum else maximum
    return maximum
