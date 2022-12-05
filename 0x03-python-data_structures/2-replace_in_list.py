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
        for i in range(len(my_list) - 1):
            if i == idx:
                my_list[i] = element
                return my_list
