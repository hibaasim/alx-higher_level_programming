#!/usr/bin/python3
'''Defines a class that inherits from another'''


class MyList(list):
    '''Inherits from list

    Args:
        list: list to sort in ascending order
    '''
    def print_sorted(self):
        '''Prints list in ascending order
        '''
        lis = self[:]
        lis.sort()
        print(lis)
