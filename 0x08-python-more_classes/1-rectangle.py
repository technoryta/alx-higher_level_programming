#!/usr/bin/python3
""" CLass defines rectangle """


class Rectangle:
    """
    Rectangle class"""

    def __init__(self, width=0, height=0):
        """Initialisation
        Args:
            width: width of rect
            height: height of rect
        Raises:
            TypeError: if inputs not int
            ValueError: if inputs negative
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ returns w"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets w"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >=0")
        else:
            self.__width = value

    @property
    def height(self):
        """returns h"""
        return self__.height

    @height.setter
    def height(self, value):
        """sets h"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >=0")
        else:
            self.__height = value
