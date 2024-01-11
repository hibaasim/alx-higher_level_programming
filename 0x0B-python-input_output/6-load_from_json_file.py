#!/usr/bin/python3
'''A function to load from json'''


import json


def load_from_json_file(filename):
    '''Cretes objectf rom json file

        Args:
            filename: name of json file

        Returns:
            type: object file
    '''
    with open(filename, 'w', encoding="utf-8") as jf:
        return json.load(jf)
