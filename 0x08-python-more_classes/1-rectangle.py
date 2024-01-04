#!/usr/bin/python3
"""class that define rectangle """


class Rectangle:
    """rectange"""

    def __init__(self, width=0, height=0):
        """ Initialization of rectangle

        args:
            width: width of rectangle
            height: height of rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrive width"""
        return self.__width

    def width(self, width):
        """setter of width"""
        if not isinstance(width, int):
            raise TypeError("zidth must be an integr")
        if width < 0:
            raise ValueError("must be >=0")
        self.__width = width

    @property
    def height(self):
        """retrive height"""
        return self.__height

    def height(self, height):
        """setter of height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integr")
        if height < 0:
            raise ValueError("must be >=0")
        self.__width = height
