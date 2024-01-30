#!/usr/bin/python3
'''Returns the lookup func'''


def lookup(obj):
    '''Returns  the list of available attributes and methods of an object

    Args:
        obj: the object

    Returns:
        list: list of attributes and methods for the object
    '''
    return dir(obj)
