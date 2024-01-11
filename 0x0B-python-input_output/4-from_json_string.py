#!/usr/bin/python3
'''A function to convert from json'''


import json


def from_json_string(my_str):
    '''Converts from json back to object

        Args:
            my_str: json representation of object

        Returns:
            type: object
    '''
    return json.loads(my_str)
