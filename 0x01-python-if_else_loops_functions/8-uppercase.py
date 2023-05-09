#!/usr/bin/python3
def uppercase(str):
    strtmp = ""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            ch = chr(ord(ch) - 32)
            print("{:s}".format(ch), end='')
    print('\n', end="")
