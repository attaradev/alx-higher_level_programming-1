#!/usr/bin/python3

def uniq_add(my_list=[]):
    """ Compute for the sum of unique elements in a list """
    ans = 0
    uniques = []

    for i in sorted(set(my_list)):
        uniques.append(i)

    for i in uniques:
        ans += i

    return ans
