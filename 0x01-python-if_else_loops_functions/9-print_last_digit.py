#!/usr/bin/python3

def print_last_digit(number):
    if not isinstance(number, int):
        print('ValueError')

    last_digit = int(repr(number)[-1])
    if number < 0:
        last_digit *= -1

    print('{:d}'.format(last_digit), end='')
    return last_digit
