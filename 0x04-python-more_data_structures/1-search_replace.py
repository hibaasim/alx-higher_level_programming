#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for n in range(len(my_list)):
        if my_list[n] == search:
            new[n] = replace
    return (new)
