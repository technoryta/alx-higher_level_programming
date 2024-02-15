#!/usr/bin/python3
""" CLass defines rectangle """


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0
    print_symbol = '#'

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
        self.number_of_instances += 1

    @property
    def width(self):
        """ retrieves w"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets w"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves h"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets h"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2*(self.__width + self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle = ""
        horizontal = str(self.print_symbol) * self.__width
        for i in range(self.__height):
            rectangle += "\n" + horizontal
        return (rectangle)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.height})"

    def __del__(self):
        print("Bye rectangle...")
        if Rectangle.number_of_instances > 0:
            Rectangle.number_of_instances -= 1
