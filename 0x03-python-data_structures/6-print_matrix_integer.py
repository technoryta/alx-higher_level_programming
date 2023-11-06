#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """Function that prints all integers in a list"""
    for row in matrix:
        for count, column in enumerate(row):
            if count == len(row) - 1:
                print("{:d}".format(column), end="")
            else:
                print("{:d}".format(column), end=" ")
        print()
