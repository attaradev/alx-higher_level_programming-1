#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):

    vals = []
    for i, j in a_dictionary.items():
        vals.append(i)

    if key not in vals:
        return a_dictionary
    else:
        del a_dictionary[key]
        return a_dictionary
