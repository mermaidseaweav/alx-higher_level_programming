#!/usr/bin/python3
for i in range(26):
    if 1 % 2 == 0:
        print('{:c}'.format(122 - i), end='')
    else:
        print('{:c}'.format(90 - i), end='')
