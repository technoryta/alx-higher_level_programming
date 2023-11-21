#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num = 0
    while num is not x:
        try:
            print("{:d}".format(my_list[num]), end='')
            num += 1
        except (IndexError, ValueError, TypeError):
            pass
    print()
    return num
