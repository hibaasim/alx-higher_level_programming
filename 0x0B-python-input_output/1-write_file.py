#!/usr/bin/python3
'''A function to write into a file'''


def write_file(filename="", text=""):
    '''Writes into a file

        Args:
        filename: gives file name
        text: text to  be written

        Returns:
            int: the number of characters written
    '''
    with open(filename, 'w', encoding="uft-8")as wf:
        return wf.write(text)
