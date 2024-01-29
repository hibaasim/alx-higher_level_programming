#!/usr/bin/python3
'''Defines the class Rectangle'''


class Rectangle:
    '''defines a rectangle by:(based on 2-rectangle.py)'''

    def __init__(self, width=0, height=0):
        '''instances

            Args:
                width: the rectangle width
                height: the rectangle height
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        '''Gets the rectangle width'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Sets the rectangle width

            Args:
                value: the width

            Raises:
                TypeError: if not int
                ValueError: if value <0
        '''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''Gets the rectangle height'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Sets the rectangle height

            Args:
                value: the height

            Raises:
                TypeError: if not int
                ValueError: if value < 0
        '''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''calculates rectangle area

            Returns:
                int: area
        '''
        return (self.__width) * (self.__height)
    
    def perimeter(self):
        '''calculates the rectangle perimeter

            Returns:
                int: 0 or perimeter
        '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2
    
    def __str__(self):
        '''prints rectangle with #

            Returns:
                str: rectangle
        '''
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                rect.append("#")
            rect.append("\n")

        rect.pop()
        return "".join(rect)
        
