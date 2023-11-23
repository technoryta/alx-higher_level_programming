#!/usr/bin/python3
"""Define a square"""


class Square:
    """Instantiate with option"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialise the square class

            Args:
                size(int): size of square
                position(tuple): coordinates of 2 postive integers

            Raises:
                TypeError: if size is not integer
                ValueError: if size is negative
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def postion(self, position):
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    def area(self):
        """Calculates square area

        Return: The size of square
        """
        return (self.__size * self.__size)

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            for x in range(self.__size):
                print("{}{}".format(" " * self.position[0], "#" * self.size))
