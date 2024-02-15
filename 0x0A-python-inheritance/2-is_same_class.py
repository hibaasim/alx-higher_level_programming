#!/usr/bin/python3
'''defines the is_same_class funct'''

def is_same_class(obj, a_class):
    '''Identifies class instances

    Args:
        obj: the object
        a_class: type of type check

    Returns:
        boolean: True or False
    '''
    return type(obj) == a_class
