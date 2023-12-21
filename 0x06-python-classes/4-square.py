#!/usr/bin/python3
'''Defines a square class'''


class Square:
    '''defines a square by: (based on 3-square.py)'''

    def __init__(self, size=0):
        '''instances

        Args:
            size: the size of one side
        '''
        self.__size = size

    @property
    def size(self):
        '''gets the size'''
        return self.__size

    @size.setter
    def size(self, value):
        '''sets the size to a certain value

        Args:
             size: the size of one side
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        '''calculates the arer of the square'''
        return (self.__size ** 2)
