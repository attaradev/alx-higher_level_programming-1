#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    vals = []

    for i, j in a_dictionary.items():
        vals.append(i)

    vals.sort()
    for val in vals:
        print("{}: {}".format(val, a_dictionary.get(val)))
