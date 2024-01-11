#!/usr/bin/python3
'''A function to convert to JSON and add to file'''


import json


def save_to_json_file(my_obj, filename):
    '''Convert object to JSON and add to file

        Args:
            my_obj: the obect to be coverted
            filename: the file
    '''
    with open(filename, 'w', encoding="utf-8") as f:
        json_obj = json.dumps(my_obj)
        return f.write(json_obj)
