#!/usr/bin/python3
'''A function that converts to JSON'''


import json
def to_json_string(my_obj):
    '''Gives JSON representation of object

        Args:
            my_obj: oject to be converted

        Returns:
            str: the JSON repreentation
    '''
    return json.dumps(my_obj)
