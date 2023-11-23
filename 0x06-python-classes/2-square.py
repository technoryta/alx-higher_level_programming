#!/usr/bin/python3
"""Define a square"""


class Square:
    """Instantiate with option"""

    def __init__(self, size=0):
        """Initialise the square class

            Args:
                size(int): size of square

            Raises:
                TypeError: if size is not integer
                ValueError: if size is negative
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >=0')

        self.__size = size
