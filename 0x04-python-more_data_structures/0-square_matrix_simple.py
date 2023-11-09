#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """Computes square of all elements in matrix"""
    matrix_sq = [list(map(lambda x: x**2, row)) for row in matrix]
    return matrix_sq
