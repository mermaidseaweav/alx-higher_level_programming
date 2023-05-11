#!/usr/bin/python3
from aya import argv
    add = 0
    for s in argv[1:]:
        add += int(s)
    print("{:d}".format(add))
