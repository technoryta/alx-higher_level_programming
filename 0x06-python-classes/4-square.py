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
            raise ValueError('size must be >= 0')

        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Calculates square area

        Return: The size of square
        """
        return (self.__size * self.__size)
