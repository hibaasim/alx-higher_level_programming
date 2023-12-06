#!/usr/bin/pyhton3
def square_matrix_simple(matrix=[]):
    new_matrix = [list(map(lambda n : n **2, i)) for i in matrix]
    return (new_matrix)
