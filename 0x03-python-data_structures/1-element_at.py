#!/usr/bin/python3

def element_at(my_list, idx):
    '''
    Return the element at idx index position or None if idx is out of
    index range

    my_list: a list of items
    idx: an integer number
    '''
    if idx < 0 or idx > len(my_list):
        return None
    else:
        for i in range(len(my_list)):
            if i == idx:
                return my_list[i]
