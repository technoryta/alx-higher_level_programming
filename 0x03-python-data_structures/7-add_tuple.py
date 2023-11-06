#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """Returns a tuple of 2 integers"""
    tuple_a = tuple_a + (0,0)
    tuple_b = tuple_b + (0,0)
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
