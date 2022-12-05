#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    '''
    Replace an element of `my_list` with 'element' at index idx
    Return the unchanged list if idx is negative or out of index
    range

    @my_list: a list of items
    @idx: an integer number
    @element: the element to replace
    '''

    if idx < 0 or idx > len(my_list):
        return my_list
    else:
        my_list[idx] = element
        return my_list
