#!/usr/bin/python3
def no_c(my_string):
    """removes all c characters"""
    new_list = [x for x in my_string if x != 'c' and x != 'C']
    new_list = "".join(new_list)
    return new_list
