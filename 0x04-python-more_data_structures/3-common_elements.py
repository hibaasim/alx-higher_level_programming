#!/usr/bin/pyhton3
def common_elements(set_1, set_2):
    com_set = {x for x in (set_1 & set_2)}
    return (com_set)
