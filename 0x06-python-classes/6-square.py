#!/usr/bin/python3
'''Defines a square class'''


class Square:
    '''defines a square by: (based on 3-square.py)'''

    def __init__(self, size=0, position=(0, 0)):
        '''instances

        Args:
            size: the size of one side
            position: shows position of the square
        '''
        self.size = size
        self.position = position

    @property
    def size(self):
        '''gets the size'''
        return self.__size

    @property
    def position(self):
        '''gets the position'''
        return self.__position

    @size.setter
    def size(self, value):
        '''sets the size to a certain value

        Args:
             value: the value of size to be set
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        '''sets the position to certain values

        Args:
            value: the opsition value to be set
        '''
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        for val in value:
            if val < 0:
                raise TypeError("position must be a tuple of 2 positive integer")
            if not isinstance(val, int):
                raise TypeError("position must be a tuple of 2 positive integer")
            self.__position = value

    def area(self):
        '''calculates the arer of the square'''
        return (self.__size ** 2)

    def my_print(self):
        '''prints the value of the size using #'''
        if self.__size == 0:
            print("")
        for p in range(self.__position[1]):
            print("")
        for i in range(self.__size):
            for j in range(self.__position[0]):
                print(" ", end="")
            print("#" * (self.__size))
