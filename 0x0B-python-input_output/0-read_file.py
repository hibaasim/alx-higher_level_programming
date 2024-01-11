#!/usr/bin/python3
'''A function to read files'''


def read_file(filename=""):
    ''' Reads open files

        Args:
            filename: name of file
    '''

    with open(filename, encoding="utf-8") as newfile:
        info = newfile.read()
        print(info, end="")
