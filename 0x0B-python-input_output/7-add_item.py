#!/usr/bin/python3
'''A function that adds all arguments to Pyhton file'''


from sys import argv


save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

try:
    f = load_json('add_item.json')
except (ValueError, FileNotFoundError):
    f = []
for arg in argv[1:]:
    f.append(arg)

save_json(f, 'add_item.json')
