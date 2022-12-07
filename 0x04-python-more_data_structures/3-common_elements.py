#!/usr/bin/python3

def common_elements(set_1, set_2):
    common = []

    for val in set_1:
        for val1 in set_2:
            if val == val1:
                common.append(val)

    return common
