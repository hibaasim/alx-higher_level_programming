#!/usr/bin/python3
'''defines the is_kind_of_class func'''


def is_kind_of_class(obj, a_class):
    '''Identifies origin of objects

    Args:
        obj: the object
        a_class: type of type check

    Returns:
        boolean: True or False
    '''
    return isinstance(obj, a_class)
