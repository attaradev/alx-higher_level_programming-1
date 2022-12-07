#!/usr/bin/python3

def number_keys(a_dictionary):
    vals = []

    for val, other in a_dictionary.items():
        vals.append(val)

    return len(vals)
