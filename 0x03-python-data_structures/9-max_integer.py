#!/usr/bin/python3
def max_integer(my_list=[]):
    '''
        Return the maximum integer of a list

        @my_list: the list of integers
    '''
    max_val = 0
    for val in my_list:
        if val > max_val:
            max_val = val
    return max_val
