#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            val = 32
        else:
            val = 0

        print("{:c}".format(ord(str[i]) - val), end='')

    print()
