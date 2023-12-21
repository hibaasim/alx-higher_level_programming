#!/usr/bin/python3
'''Defines a square class'''


class Square:
    '''defines a square by: (based on 1-square.py)'''

    def __init__(self, size=0):
        '''instances with exceptions

        Args:
             size: the size of one side
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
