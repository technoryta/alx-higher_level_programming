#!/usr/bin/python3

def islower(c):
    """Checks if character is lower case"""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
