#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = ''
    if length > 0:
        first = sentence[0]
    else:
        first = None
    tuple_t = length, first
    return tuple_t
