#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    vals = {}

    for i, j in a_dictionary.items():
        vals[i] = j * 2

    return vals
