#!/usr/bin/pyhton3

def safe_print_list(my_list=[], x=0):
    i = 0

    for val in range(x):
        try:
            print("{}".format(my_list[val]), end="")
            i += 1
        except IndexError:
            break
    print("")
    return(i)
