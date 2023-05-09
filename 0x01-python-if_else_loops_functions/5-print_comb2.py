#!/usr/bin/python3
charend = ","
for i in range(0, 100):
    if i < 10:
        print("{}{}".format(0, 1), end=charend)
    else:
        if i == 99:
            charend = "\n"
            print(i, end=charend)
