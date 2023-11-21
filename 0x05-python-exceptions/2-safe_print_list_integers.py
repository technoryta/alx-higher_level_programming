#!/usr/bin/python3

def safe_print_list_list_integers(my_list=[], x=0):
    num = 0
    try:
        while num is not x:
            print(my_list[num], end='')
            num += 1
    except (IndexError, ValueError, TypeError):
        pass
    print()
    return num
