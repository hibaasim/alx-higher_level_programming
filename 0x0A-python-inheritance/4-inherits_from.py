#!/usr/bin/python3
'''defines the inherits_from func'''


def inherits_from(obj, a_class):
    '''Identifies the type of an object

    Args:
        obj: object
        a_class: type of type check

    Returns:
        boolean: True or False
    '''
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
