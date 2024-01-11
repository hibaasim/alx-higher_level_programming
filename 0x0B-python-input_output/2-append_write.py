#!/usr/bin/python3
'''A function to append text to a file'''


def append_write(filename="", text=""):
    '''Appends text to a file and if the file
        doesnt exist it creates the file

        Args:
            filename: name of file
            text: text to be added

        Returns:
            int: the number of characters added
    '''
    with open(filename, 'a', encoding="utf-8") as af:
        return af.write(text)
